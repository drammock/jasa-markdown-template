# -*- coding: utf-8 -*-
"""
===============================================================================
Script 'placeholder figure'
===============================================================================

This script makes a gray square to use as a placeholder figure.
"""
# @author: drmccloy
# Created on Tue Sep  8 13:57:47 2015
# License: BSD (3-clause)

import sys
from matplotlib import pyplot as plt

if len(sys.argv) > 2:
    figsize = (sys.argv[1], sys.argv[2])
elif len(sys.argv) > 1:
    figsize = (sys.argv[1], sys.argv[1])
else:
    figsize = (3.5, 3.5)

fig = plt.figure(figsize=figsize, frameon=False)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')
_ = ax.plot(-1, -1)
_ = plt.fill_between((0, 1), 1, color='gray')
_ = plt.xlim(0, 1)
_ = plt.ylim(0, 1)

plt.savefig('fig-placeholder.eps')
