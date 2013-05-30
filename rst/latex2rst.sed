s/\\ldots/…/g
s/\\vimcmd{\([^}]*\)}/:vimcmd:`\1`/g
s/\\vimrc/|vimrc|/g
s/\\vim/|vim|/g
s/\\url{\([^}]*\)}/\1/g
s/\\textbf{\([^}]*\)}/**\1**/g
s/\\emph{\([^}]*\)}/*\1*/g
s/\\Verb|\([^|]*\)|/``\1``/g
s/ \\fg{}/ »/g
s/ \\fg/ »/g
s/\\og /« /g
s/\\xspace//g
s/\\ttesc/|ttesc|/g
s/\\tti/|tti|/g
s/\\tty/|tty|/g
s/\\hlred{\([^}]*\)}/\1/g
