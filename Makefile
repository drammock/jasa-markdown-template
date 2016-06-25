submission: linkbst makesub cleantex

makesub: manuscript.tex figures/fig-placeholder.eps linkeps
	python pandoc/latex-postprocessor.py manuscript.tex cleanms.tex
	pdflatex cleanms.tex
	bibtex cleanms.aux
	python pandoc/latex-make-standalone.py cleanms.tex submission.tex
	python pandoc/latex-suppress-figures.py submission.tex \
	submission-no-figs.tex
	pdflatex submission.tex
	pdflatex submission.tex
	pdflatex submission.tex

manuscript.tex: manuscript.md pandoc/template-JASA-submission.tex
	pandoc --natbib --number-sections --no-tex-ligatures \
	--template=pandoc/template-JASA-submission.tex \
	--output=manuscript.tex manuscript.md

figures/fig-%.eps: figures/fig-%.py
	cd $(<D); python $(<F)

prepress:
	pandoc --filter pandoc-eqnos --natbib \
	--template=pandoc/template-JASA-prepress.tex \
	--output=manuscript-prepress.pdf manuscript.md

response:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=pandoc/template-plain.tex \
	--output=review/response-to-reviewers.pdf \
	review/response-to-reviewers.md

coverletter:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=pandoc/template-letterhead.tex \
	--output=cover-letter/cover-letter.pdf cover-letter/cover-letter.md

cleantex:
	rm -f *.eps *-eps-converted-to.pdf bibstyle.bst manuscript.tex
	bn="cleanms"; for ext in tex pdf $(EXTS); do rm -f "$$bn.$$ext"; done
	bn="submission"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done

clean: cleantex
	rm -f manuscript.pdf manuscript.tex submission.pdf submission.tex \
	submission-no-figs.tex manuscript-prepress.pdf

linkbst:
	ln -sf bib/jasa-submission.bst bibstyle.bst

linkeps:
	for fig in figures/*.eps; do ln -sf "$$fig"; done

EXTS = bbl aux ent fff log lof lol lot toc blg out pyg ttt

.PHONY: linkbst linkeps cleantex clean
