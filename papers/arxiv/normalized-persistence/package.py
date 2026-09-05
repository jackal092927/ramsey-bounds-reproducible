from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess

root = Path(__file__).resolve().parent
subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=root, check=True)
with ZipFile(root / "arxiv-source.zip", "w", ZIP_DEFLATED) as archive:
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if path.is_file() and (path.suffix in {".tex", ".sty", ".bib", ".bst", ".bbl"} or (relative.parts[0] == "anc" and not any(part.startswith(".") or part == "__pycache__" for part in relative.parts))):
            archive.write(path, relative)
print("Prepared arxiv-source.zip; inspect the rebuilt PDF before upload.")
