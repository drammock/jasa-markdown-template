---
title: Insert title here (but don't use title case)
runningtitle: This is the running title (6 words or fewer)
author:
- name: Jane Q. Author
  email: jane_q@soundu.edu
  affiliation:
  - Department of Acoustics
  - Rayleigh School of Acoustical Engineering, Sound University, Sometown, NR 54321, USA
- name: John P. Coauthor
  affiliation:
  - Institute for Acoustics, Acoustics State University, Otherburg, RS, 98765-4321, USA
documentclass: article
classoption: oneside
fontsize: 12pt
geometry:
- letterpaper
- margin=1in
biblio-style: bibstyle
bibliography: bib/bibfile
pacs:
- 99.99.Aa <!-- Fake PACS title -->
- 88.88.Bb <!-- Fake PACS title -->
- 77.77.Cc <!-- Fake PACS title -->
keywords:
- acoustics
- sound
- hearing
copyrightyear: 2016
abstract: Curabitur et finibus tellus. Mauris vel tortor non erat feugiat gravida a ut urna. Fusce sodales odio vitae tellus luctus, a porta lectus tempus. Nunc lacinia suscipit consectetur. Curabitur et finibus tellus. Nunc lacinia suscipit consectetur.
acknowledgments: TODO acknowledge some folks
possible-reviewers: TODO this is just a reminder to suggest some reviewers, not incorporated in the finished documents.
---
# Introduction
Phasellus nec ante eu ex vulputate mattis. Fusce varius maximus justo vitae bibendum. Proin pellentesque ultrices dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce ullamcorper lectus ac ipsum euismod vehicula.

Mauris vel tortor non erat feugiat gravida a ut urna. Fusce sodales odio vitae tellus luctus, a porta lectus tempus. Nunc lacinia suscipit consectetur. Curabitur et finibus tellus.

# Background
Suspendisse vitae feugiat augue.[@riesz1928] Ut sodales lobortis sem vitae sodales.[@sandel1955] Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam ultricies, elit eget venenatis aliquam, ex ligula ultrices risus, ut varius odio purus eget ante. Curabitur hendrerit lectus malesuada velit congue dictum.

Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor.[@mills1958]

# Methods
Aenean efficitur consectetur arcu nec volutpat. Maecenas nec mattis nunc. Phasellus sit amet elit ac dolor fermentum tempor. Aliquam ac metus placerat, gravida tortor eget, sollicitudin ex. Nulla facilisi.

## General methods
Curabitur hendrerit lectus malesuada velit congue dictum. Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor. Suspendisse vitae feugiat augue.

### Stimuli
Here is a cross-reference to Table \ref{tab-simple}. In the row of dashes in between the header row and content rows in the markdown source, the ratio of dashes in each column determines the relative column widths.  More complicated tables (e.g., using LaTeX `multicolumn`, or the `siunitx` package for number formatting and alignment) can be incorporated as LaTeX tables in the markdown source, or as separate `my-table.tex` files using `\include{my-table}` in the markdown source.

Table: The simplest type of markdown table. There is a LaTeX `\label{}` tag in this caption for cross-referencing, and a couple of `$`-bracketed math expressions, but otherwise the table is pure markdown. \label{tab-simple}

**Left aligned**             **Centered**                    **Right aligned**
-------------------------- ---------------- ----------------------------------
$\beta_i \times d^\prime$    `foo`                   some _nearly_ normal text
$\alpha_j$                   bar^2^                       some other text

Ut sodales lobortis sem vitae sodales. Interdum et malesuada fames ac ante ipsum primis in faucibus. Etiam ultricies, elit eget venenatis aliquam, ex ligula ultrices risus, ut varius odio purus eget ante. Curabitur hendrerit lectus malesuada velit congue dictum. Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor. Suspendisse vitae feugiat augue.

### Participants
Phasellus sodales, massa ac vestibulum scelerisque, mauris urna aliquet ante, id lacinia odio enim nec sem. Nulla sit amet consequat erat. Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere. Proin sed tincidunt turpis.

### Procedure
Phasellus sodales, massa ac vestibulum scelerisque, mauris urna aliquet ante, id lacinia odio enim nec sem. Nulla sit amet consequat erat. Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere. Proin sed tincidunt turpis.

## Experiment 1
Proin sed tincidunt turpis. Phasellus sodales, massa ac vestibulum scelerisque, mauris urna aliquet ante, id lacinia odio enim nec sem. Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor.Nulla sit amet consequat erat. Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere.

## Experiment 2
Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere. Phasellus sodales, massa ac vestibulum scelerisque, mauris urna aliquet ante, id lacinia odio enim nec sem. Nulla sit amet consequat erat. Proin sed tincidunt turpis.

# Results
Nulla sit amet consequat erat. Phasellus sodales, massa ac vestibulum scelerisque, mauris urna aliquet ante, id lacinia odio enim nec sem. Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere. Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Proin sed tincidunt turpis.

![caption goes here. Mathmode test in caption: $t_\mathrm{max}$ works.](fig-placeholder.eps)

Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor.

Nam tincidunt eros eu risus elementum ultrices sit amet quis orci. Suspendisse mattis, ante sed efficitur convallis, velit ligula lobortis erat, quis aliquam nulla lorem sed dolor.Nulla sit amet consequat erat. Suspendisse ut finibus leo, ac ultricies sem. Maecenas dapibus gravida posuere.

# Discussion
Phasellus nec ante eu ex vulputate mattis. Fusce varius maximus justo vitae bibendum. Proin pellentesque ultrices dignissim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce ullamcorper lectus ac ipsum euismod vehicula.

Mauris vel tortor non erat feugiat gravida a ut urna. Fusce sodales odio vitae tellus luctus, a porta lectus tempus. Nunc lacinia suscipit consectetur. Curabitur et finibus tellus.
