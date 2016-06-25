# JASA submission template
This is a template for writing an article for *The Journal of the Acoustical Society of America* in [Markdown][md].  The `Makefile` uses [pandoc][pd] to convert the markdown source to both a PDF with inline figures (for reviewer use) and a standalone LaTeX source file with integrated bibliography and *without* figures (*JASA* requires that figures be submitted separately and replaced by “[INSERT FIGURE XX ABOUT HERE]” in the text).  The submittable LaTeX output also pushes all tables to the end of the document, and appends a list of figure captions.

I offer no guarantees of compliance, because *JASA*’s style and formatting requirements are a moving target; however, if you want to write in markdown and submit to *JASA*, this may save you some time.

I offer no guarantees of this working on your computer either; for the record it works for me with this setup:

- OS: Linux (Xubuntu 14.04)
- pandoc 1.17.1
- pdfTeX 3.1415926-2.5-1.40.14 (TeX Live 2013/Debian)
- XeTeX 3.1415926-2.5-0.9999.3-2014012222 (TeX Live 2013/Debian)
- GNU Make 3.81

# Makefile directives you should use
- `make submission` (the default) builds both a submittable standalone LaTeX source file (`submission-no-figs.tex`) and a compiled PDF (`submission.pdf`), as described above. Also generates `submission.tex`, the file from which the PDF was created.
- `make coverletter` (replace files `pandoc/author-signature.pdf` and `pandoc/letterhead-banner.pdf` before using)
- `make response` (response to reviewers; not strictly neccessary)
- `make clean` (delete all generated files except figures)

Note that the makefile directive `makesub` is where you should add additional dependencies (e.g., for figures) if you want `make` to monitor the figure-generating scripts. If your figure-generating scripts are not python scripts (or are not named `fig-*.py`) then you will need to add a new directive or modify the directive for `figures/fig-%.eps`.

[md]: https://daringfireball.net/projects/markdown/
[pd]: http://pandoc.org/
