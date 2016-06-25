#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
This script assembles a standalone LaTeX file with bibliography and list of
figures incorporated into the main document (JASA requires single standalone
documents for article submission). It also replaces proper unicode en-dashes
(–) with LaTeX-style double-hyphens (--) and smart double quotes with LaTeX-
style `` and ''. Pandoc has already done this in the main document (which
propogates to the list of figures), so we only modify the bibliography here.
'''

import sys
import os.path as op
infile = sys.argv[-2]
outfile = sys.argv[-1]
bibliography = op.splitext(infile)[0] + '.bbl'
listoffigs = op.splitext(infile)[0] + '.lof'

figs = ''.join(open(listoffigs).readlines())
bib = ''.join(open(bibliography).readlines())
bib = bib.replace('–', '--')
bib = bib.replace('“', '``')
bib = bib.replace('”', '\'\'')

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        if '\\bibliography{' in line:
            line = bib
        if '\\listoffigures' in line:
            g.write('\\section*{List of figures}\n')
            line = figs
        g.write(line)
