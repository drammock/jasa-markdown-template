submission: link_subm_template _subm cleantex

el_prepress: link_el_template _el_pre cleantex

manuscript.tex: manuscript.md
	pandoc --natbib --number-sections --no-tex-ligatures \
	--template=template.tex --output=manuscript.tex manuscript.md

_el_pre: manuscript.tex figures/fig-placeholder.eps link_bib_figs
	python pandoc/latex-postprocessor.py manuscript.tex \
	manuscript-prepress.tex
	pdflatex manuscript-prepress.tex
	bibtex manuscript-prepress.aux
	pdflatex manuscript-prepress.tex
	pdflatex manuscript-prepress.tex
	pdflatex manuscript-prepress.tex

_subm: manuscript.tex figures/fig-placeholder.eps link_bib_figs
	python pandoc/latex-postprocessor.py manuscript.tex cleanms.tex
	pdflatex cleanms.tex
	bibtex cleanms.aux
	python pandoc/latex-make-standalone.py cleanms.tex submission.tex
	python pandoc/latex-suppress-figures.py submission.tex \
	submission-no-figs.tex
	pdflatex submission.tex
	pdflatex submission.tex
	pdflatex submission.tex

figures/fig-%.eps: figures/fig-%.py
	cd $(<D); python $(<F)

response:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=pandoc/template-plain.tex \
	--output=review/response-to-reviewers.pdf \
	review/response-to-reviewers.md

coverletter:
	pandoc --no-tex-ligatures --latex-engine=xelatex \
	--template=pandoc/template-letterhead.tex \
	--output=cover-letter/cover-letter.pdf cover-letter/cover-letter.md

link_el_template:
	ln -sf pandoc/template-JASA-EL-prepress.tex template.tex

link_subm_template:
	ln -sf pandoc/template-JASA-submission.tex template.tex

link_bib_figs:
	ln -sf bib/jasa-submission.bst bibstyle.bst
	for fig in figures/*.eps; do ln -sf "$$fig"; done

cleantex:
	rm -f *.eps *-eps-converted-to.pdf 
	rm -f bibstyle.bst template.tex manuscript.tex
	bn="cleanms"; for ext in tex pdf $(EXTS); do rm -f "$$bn.$$ext"; done
	bn="submission"; for ext in $(EXTS); do rm -f "$$bn.$$ext"; done
	bn="manuscript-prepress"; for ext in tex $(EXTS); do rm -f "$$bn.$$ext"; done

clean: cleantex
	rm -f manuscript.pdf manuscript.tex submission.pdf submission.tex \
	submission-no-figs.tex manuscript-prepress.pdf

EXTS = bbl aux ent fff log lof lol lot toc blg out pyg ttt

.PHONY: link_bib_figs link_el_template link_subm_template cleantex clean
