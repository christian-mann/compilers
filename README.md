Compilers Project 2-4
====


Prerequisites
---
    python2.6+
    rstr (for src/fuzz.py)
    pdflatex


Building
---
Run `make`

To build the documentation, run `make doc`.

To run tests, run `make tests`.

Modifying the grammar
---

Modify the grammar contained in `src/rules.py` -- there ought to be enough examples to get a feeling of the structure. `[""]` is epsilon.

If you add any new terminals or nonterminals, make sure to update the `V` and `T` sets.

Modify the reverse translator contained in `src/grammarToLatex.py#printTerm(t)` to reflect any new terminals.
