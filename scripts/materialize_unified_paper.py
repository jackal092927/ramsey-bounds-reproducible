#!/usr/bin/env python3
"""Materialize the canonical unified manuscript from the four source parts.

The historical part manuscripts remain byte-stable source components.  This
script copies their section and appendix sources into ``papers/unified`` while
making two mechanical changes required by a single LaTeX document:

* labels and references receive ``up:``, ``low:``, ``fin:``, or ``qua:``
  namespaces;
* handwritten equation tags receive visible ``U``, ``L``, ``F``, or ``Q``
  prefixes and stable labels, so no two displayed equations share a tag.

The generated files are committed so that the paper can be inspected without
running this script.  Re-running the script must be deterministic.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
UNIFIED = PAPERS / "unified"

PARTS = {
    "upper": {"prefix": "up", "tag": "U"},
    "lower": {"prefix": "low", "tag": "L"},
    "finite": {"prefix": "fin", "tag": "F"},
    "quantum": {"prefix": "qua", "tag": "Q"},
}

SECTION_TITLES = {
    ("upper", "01_introduction.tex"): (
        "Introduction",
        "Diagonal upper bound: theorem and proof architecture",
    ),
    ("lower", "01_introduction.tex"): (
        "Introduction",
        "Fixed-ratio lower bound: theorem and proof architecture",
    ),
    ("finite", "01_introduction.tex"): (
        "Introduction",
        "Finite Ramsey barrier: problem and proof architecture",
    ),
    ("quantum", "01_introduction.tex"): (
        "Introduction",
        "Quantum constructive Ramsey search: theorem and contribution",
    ),
}


def namespace_labels(text: str, prefix: str) -> str:
    """Namespace ordinary LaTeX labels and all corresponding references."""

    text = re.sub(
        r"\\label\{([^}]+)\}",
        lambda match: rf"\label{{{prefix}:{match.group(1)}}}",
        text,
    )

    def replace_reference(match: re.Match[str]) -> str:
        command, payload = match.groups()
        keys = ",".join(
            f"{prefix}:{key.strip()}" for key in payload.split(",")
        )
        return rf"\{command}{{{keys}}}"

    return re.sub(
        r"\\(cref|Cref|ref|eqref)\{([^}]+)\}",
        replace_reference,
        text,
    )


def equation_replacements(
    texts: dict[str, str], *, prefix: str, visible_prefix: str, scope: str
) -> dict[str, tuple[str, str]]:
    """Return the label and visible tag for every handwritten tag in a scope."""

    tag_owner: dict[str, str] = {}
    explicit_labels: dict[str, str] = {}
    for name, text in texts.items():
        for match in re.finditer(
            r"\\tag\{([^}]+)\}(?:\s*\\label\{([^}]+)\})?", text
        ):
            tag, explicit_label = match.groups()
            if tag in tag_owner:
                raise ValueError(
                    f"duplicate equation tag {tag!r} in {tag_owner[tag]} and {name}"
                )
            tag_owner[tag] = name
            if explicit_label is not None:
                explicit_labels[tag] = explicit_label

    replacements: dict[str, tuple[str, str]] = {}
    for tag in tag_owner:
        slug = re.sub(r"[^A-Za-z0-9]+", "-", tag).strip("-").lower()
        label = explicit_labels.get(tag, f"{prefix}:{scope}:eq:{slug}")
        visible = f"{visible_prefix}{tag}"
        replacements[tag] = (label, visible)
    return replacements


def qualify_equation_tags(
    texts: dict[str, str],
    *,
    prefix: str,
    visible_prefix: str,
    scope: str,
    reference_replacements: dict[str, tuple[str, str]] | None = None,
) -> dict[str, str]:
    """Qualify handwritten tags and replace prose references across a part.

    A scope is either an entire main part or one appendix file. Tags must be
    unique inside that scope. ``reference_replacements`` may additionally
    contain tags from the other scopes in the same part, so appendix-to-main
    and main-to-appendix references receive the correct visible namespace.
    """

    replacements = equation_replacements(
        texts, prefix=prefix, visible_prefix=visible_prefix, scope=scope
    )
    references = reference_replacements or replacements

    rendered: dict[str, str] = {}
    for name, text in texts.items():
        def replace_tag(match: re.Match[str]) -> str:
            tag = match.group(1)
            label, visible = replacements[tag]
            return rf"\tag{{{visible}}}\label{{{label}}}"

        text = re.sub(
            r"\\tag\{([^}]+)\}(?:\s*\\label\{([^}]+)\})?",
            replace_tag,
            text,
        )
        for tag, (label, _visible) in references.items():
            # Canonical sources use bare ``(2.9)``-style prose references.
            # Do not rewrite the same byte sequence when it is a function
            # argument such as ``D(2.9)`` or ``D'(2.9)``.
            reference = re.compile(
                rf"(?<![A-Za-z0-9_}}\]',])\({re.escape(tag)}\)"
            )
            text = reference.sub(lambda _match: rf"\eqref{{{label}}}", text)
        rendered[name] = text
    return rendered


def read_group(source_dir: Path, *, prefix: str) -> dict[str, str]:
    texts: dict[str, str] = {}
    for source in sorted(source_dir.glob("*.tex")):
        texts[source.name] = namespace_labels(
            source.read_text(encoding="utf-8"), prefix
        )
    return texts


def write_group(destination: Path, texts: dict[str, str]) -> None:
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    banner = "% Generated by scripts/materialize_unified_paper.py; do not edit.\n"
    for name, text in texts.items():
        (destination / name).write_text(banner + text, encoding="utf-8")


def materialize_part(part: str, settings: dict[str, str]) -> None:
    prefix = settings["prefix"]
    tag_prefix = settings["tag"]
    source_root = PAPERS / part

    sections = read_group(source_root / "sections", prefix=prefix)
    for (title_part, filename), (old_title, new_title) in SECTION_TITLES.items():
        if title_part != part:
            continue
        sections[filename] = sections[filename].replace(
            rf"\section{{{old_title}}}", rf"\section{{{new_title}}}", 1
        )
        sections[filename] = sections[filename].replace("This paper", "This part")
        sections[filename] = sections[filename].replace("The paper", "This part")

    appendices = read_group(source_root / "appendices", prefix=prefix)
    main_replacements = equation_replacements(
        sections,
        prefix=prefix,
        visible_prefix=tag_prefix,
        scope="main",
    )
    appendix_replacements: dict[str, dict[str, tuple[str, str]]] = {}
    all_replacements = dict(main_replacements)
    for filename, text in appendices.items():
        source_appendix = filename.split("_", 1)[0]
        local = equation_replacements(
            {filename: text},
            prefix=prefix,
            visible_prefix=f"{tag_prefix}-{source_appendix}.",
            scope=f"app-{source_appendix}",
        )
        appendix_replacements[filename] = local
        # Bare numeric tags can legitimately repeat between the main part and
        # a self-contained appendix. Main tags take precedence for main-text
        # references; each appendix overrides this map with its own local tags
        # below. Cross-scope references with an ambiguous bare number must use
        # an explicit LaTeX label instead.
        for tag, replacement in local.items():
            all_replacements.setdefault(tag, replacement)

    sections = qualify_equation_tags(
        sections,
        prefix=prefix,
        visible_prefix=tag_prefix,
        scope="main",
        reference_replacements=all_replacements,
    )
    write_group(UNIFIED / "sections" / part, sections)

    rendered_appendices: dict[str, str] = {}
    for filename, text in appendices.items():
        source_appendix = filename.split("_", 1)[0]
        local_references = dict(all_replacements)
        local_references.update(appendix_replacements[filename])
        one = qualify_equation_tags(
            {filename: text},
            prefix=prefix,
            visible_prefix=f"{tag_prefix}-{source_appendix}.",
            scope=f"app-{source_appendix}",
            reference_replacements=local_references,
        )
        rendered_appendices[filename] = one[filename]
    write_group(UNIFIED / "appendices" / part, rendered_appendices)


def merge_bibliography() -> None:
    entries: dict[str, str] = {}
    for part in PARTS:
        bibliography = (PAPERS / part / "references.bib").read_text(
            encoding="utf-8"
        )
        for block in re.split(r"(?=^@)", bibliography, flags=re.MULTILINE):
            block = block.strip()
            if not block:
                continue
            match = re.match(r"^@[A-Za-z]+\{([^,]+),", block)
            if match is None:
                raise ValueError(f"cannot parse bibliography block: {block[:80]!r}")
            key = match.group(1)
            if key in entries and entries[key] != block:
                raise ValueError(f"conflicting bibliography entries for {key}")
            entries[key] = block
    output = "% Deterministically merged by materialize_unified_paper.py.\n\n"
    output += "\n\n".join(entries.values()) + "\n"
    (UNIFIED / "references.bib").write_text(output, encoding="utf-8")


def main() -> None:
    UNIFIED.mkdir(parents=True, exist_ok=True)
    for part, settings in PARTS.items():
        materialize_part(part, settings)
    merge_bibliography()
    print("UNIFIED_PAPER_SOURCES_MATERIALIZED")


if __name__ == "__main__":
    main()
