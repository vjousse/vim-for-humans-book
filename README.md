# Vim for humans

## Installation

Be sure to create a symlink named 'vim-for-humans' in the project directory. This symlink should point to a directory where you've cloned [code examples](https://github.com/vjousse/vim-for-humans).

You will need some prerequisites to be able to compile the LaTeX source code:

- A Tex distribution, [TexLive](https://www.tug.org/texlive/) for example.
- [Pygments](http://pygments.org/), it's used for syntax highlighting using the mint LaTeX package.
- [Sphinx](http://sphinx-doc.org/) to generate the epub file.
- [kindlegen](http://www.amazon.com/gp/feature.html?docId=1000765211) to generate the .mobi file.

## Compiling

If you've installed everything, running the `makedist.sh` script should do the trick. If not, be sure to check the content of the script and to run each command one after another.
