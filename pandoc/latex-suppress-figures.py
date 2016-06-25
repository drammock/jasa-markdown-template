#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
This script excises figures from a LaTeX source document.
'''

import sys
infile = sys.argv[-2]
outfile = sys.argv[-1]
fig = False
fignum = 1

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        if '\\begin{figure}' in line:
            fig = True
            g.write(' '.join(['\\begin{{center}}\\bfseries',
                              '[Insert Figure {} about here]\\end{{center}}\n']
                             ).format(fignum))
            fignum += 1
        if not fig:
            g.write(line)
        if '\\end{figure}' in line:
            fig = False
