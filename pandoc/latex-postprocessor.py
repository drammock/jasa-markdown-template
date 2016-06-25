# -*- coding: utf-8 -*-
import sys

infile = sys.argv[-2]
outfile = sys.argv[-1]

with open(infile, 'r') as f, open(outfile, 'w') as g:
    for line in f:
        # spacing hacks
        line = line.replace(' vs. ', ' vs.\ ')
        line = line.replace(' Hz', '~Hz')
        line = line.replace(' kHz', '~kHz')
        line = line.replace(' ms ', '~ms ')
        line = line.replace(' s ', '~s ')
        line = line.replace(' s,', '~s,')
        line = line.replace(' s.', '~s.')
        line = line.replace('cf. ', 'cf.\ ')
        line = line.replace('St. ', 'St.\ ')
        line = line.replace('Table ', 'Table~')
        line = line.replace('Figure ', 'Figure~')
        line = line.replace('Figures ', 'Figures~')
        line = line.replace('Equation ', 'Equation~')
        line = line.replace('Experiment ', 'Experiment~')
        line = line.replace('Experiments ', 'Experiments~')
        # prevent prime collisions
        line = line.replace('d^\\prime', 'd\\thinspace^\\prime')
        # push acknowledgments to separate page
        if 'section{Acknowledgments' in line:
            g.write('\\cleardoublepage\n')
            line = line.replace('section{Acknowledgments',
                                'section*{Acknowledgments')
        # push appendices to separate page
        if 'section{Appendix' in line:
            g.write('\\cleardoublepage\n')
            line = line.replace('section{Appendix', 'section*{Appendix')
        # convert to ASCII to be plain LaTeX friendly (not XeLaTeX)
        line = line.replace('−', '\\textminus{}')
        line = line.replace('°', '\\textdegree{}')
        line = line.replace('±', '\\textpm{}')
        line = line.replace('™', '\\texttrademark{}')
        line = line.replace('†', '\\ensuremath{\\dagger}')
        line = line.replace('×', '\\texttimes{}')
        line = line.replace('⅔', '$\\sfrac{2}{3}$')
        line = line.replace('⁻⅓', '$\sfrac{-1}{3}$')
        line = line.replace('ƒ₀', '\\ensuremath{\\mathit{f}_0}')
        line = line.replace('π', '\\ensuremath{\\pi}')
        line = line.replace('“', '``')  # double quote left
        line = line.replace('”', '\'\'')  # double quote right
        line = line.replace('’', '\'')  # single quote right / apostrophe
        line = line.replace('–', '\\textendash{}')
        # write line
        g.write(line)
