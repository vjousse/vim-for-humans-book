pdflatex -shell-escape vim-pour-les-humains.tex
#pdftk vim-pour-les-humains.pdf cat 9-11 output vim-pour-les-humains-extrait.pdf
evince vim-pour-les-humains.pdf
