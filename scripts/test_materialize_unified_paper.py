#!/usr/bin/env python3
"""Regression tests for semantic equation-reference materialization."""

from __future__ import annotations

import unittest

from materialize_unified_paper import equation_replacements, qualify_equation_tags


class EquationReferenceMaterializationTests(unittest.TestCase):
    def test_prose_reference_changes_but_function_value_does_not(self) -> None:
        source = {
            "sample.tex": (
                "\\[x=1.\\tag{2.9}\\]\n"
                "By (2.9), D(2.9)>0 and D'(2.9)>0.\n"
            )
        }
        rendered = qualify_equation_tags(
            source, prefix="up", visible_prefix="U", scope="main"
        )["sample.tex"]

        self.assertIn(r"\tag{U2.9}\label{up:main:eq:2-9}", rendered)
        self.assertIn(r"By \eqref{up:main:eq:2-9}", rendered)
        self.assertIn("D(2.9)>0", rendered)
        self.assertIn("D'(2.9)>0", rendered)

    def test_cross_scope_reference_uses_supplied_mapping(self) -> None:
        main = {"main.tex": r"\[x=1.\tag{2.9}\]"}
        appendix = {
            "appendix.tex": (
                r"\[y=1.\tag{A.1}\]" "\n" r"Use (2.9) and (A.1)."
            )
        }
        references = equation_replacements(
            main, prefix="low", visible_prefix="L", scope="main"
        )
        references.update(
            equation_replacements(
                appendix,
                prefix="low",
                visible_prefix="L-A.",
                scope="app-A",
            )
        )

        rendered = qualify_equation_tags(
            appendix,
            prefix="low",
            visible_prefix="L-A.",
            scope="app-A",
            reference_replacements=references,
        )["appendix.tex"]

        self.assertIn(r"Use \eqref{low:main:eq:2-9}", rendered)
        self.assertIn(r"and \eqref{low:app-A:eq:a-1}", rendered)


if __name__ == "__main__":
    unittest.main(verbosity=2)
