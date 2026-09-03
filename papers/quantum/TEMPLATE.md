# LIPIcs anonymous ITCS submission layout

The standalone quantum paper uses the official **LIPIcs v2021.1.3** class,
downloaded on 2026-09-01 from Dagstuhl Publishing:

- Template page: <https://www.dagstuhl.de/en/publishing/series/details/lipics>
- Pinned archive: <https://submission.dagstuhl.de/styles/download-tag/lipics/v2021.1.3/authors/zip>
- Author instructions: <https://submission.dagstuhl.de/styles/instructions/lipics>
- ITCS 2027 call: <https://itcs-conf.org/>
- Downloaded ZIP SHA-256: `b9a4a6d6b44444cc4b9463c8d402e8f41b87e411a344b4af2508cd5bed6c19ef`

`lipics-v2021.cls`, `cc-by.pdf`, `lipics-logo-bw.pdf`, and `orcid.pdf`
are unmodified copies from that archive. The accompanying license is
preserved verbatim in `LIPICS-LICENSE.md`. The BibTeX style `plainurl`
is supplied by TeX Live's `urlbst` package.

## Review mode

`main.tex` explicitly selects `anonymous`, retains the template's line
numbers, and calls `\hideLIPIcs` to omit the publication footer and unassigned
DOI/article-number fields. Only anonymous placeholders appear in the author,
affiliation, running-author, and copyright source fields; no real author
details are hidden in the review source. PDF metadata is set to
`Anonymous Authors`. The class option `draft` is deliberately not used:
it is a layout-debugging switch, not an anonymous-submission switch.

The official class fixes body text at 10pt, abstract and references at 9pt,
and rejects an `11pt` option. Because ITCS explicitly requires at least
11pt, `itcs-submission.sty` raises prose sizes to 11pt with 14.3pt leading,
including the abstract, keywords, references, and any small/footnote text.
Mathematical scripts and marginal line numbers retain their normal sizes.
This local review-copy adapter does not change the original class, its
page dimensions, margins, font family, or theorem/list designs. No content
is cut to obtain a particular page count.

## Build

From the repository root, `make paper` builds the standalone PDF and the
separate unified manuscript using the existing pinned metadata epoch.
For the standalone paper only:

```sh
SOURCE_DATE_EPOCH=1788073200 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -cd papers/quantum/main.tex
```

The input sections and appendices remain canonical and reusable by the
unified manuscript. The LIPIcs class and adapter apply only to the standalone
submission. For a future accepted camera-ready version, remove the review
adapter, restore author metadata, and follow the editors' then-current
production instructions; this copy is not a camera-ready publication.
