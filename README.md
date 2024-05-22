# Vim for humans

Website code available here: https://github.com/vjousse/vim-for-humans-website
`vimrc` config examples available here: https://github.com/vjousse/vim-for-humans

## Install

Be sure to create a symlink named 'vim-for-humans' in the project directory. This symlink should point to a directory where you've cloned [code examples](https://github.com/vjousse/vim-for-humans).

You will need some prerequisites to be able to compile the LaTeX source code:

- A Tex distribution, [TexLive](https://www.tug.org/texlive/) for example.
- [Pygments](http://pygments.org/), it's used for syntax highlighting using the mint LaTeX package.
- [Sphinx](http://sphinx-doc.org/) to generate the epub file.
- [kindlegen](http://www.amazon.com/gp/feature.html?docId=1000765211) to generate the .mobi file.
- [sphinx-autobuild](https://github.com/sphinx-doc/sphinx-autobuild) if you want to start a webserver with hot reload in `rst/fr` with `make livehtml`

### Archlinux

    yay -S python-sphinx python-pygments kindlegen

Use [instructions from the official website for TeX Live](https://tug.org/texlive/quickinstall.html)

## Compile

After the dependencies have been installed, run `makedist.sh` script to start compiling. If the compilation fails, be sure to check the content of the script and try running each command one after another.

## Enjoy

Upon success outputs can be found in the `dist/vimpourleshumains/` directory. Enjoy!

## Tips & tricks

### Generate rounded/shadowed image

Be sur to have [ImageMagick](https://imagemagick.org/index.php) installed and use the `add-borders.sh` script like these:

    ./add-borders.sh book-tex/graphics/vim-catpuccin-mocha.png

It will replace your `book-tex/graphics/vim-catpuccin-mocha.png` image with a rounded/shadowed one and save the original image to `book-tex/graphics/vim-catpuccin-mocha-original.png`.

### Get kitty terminal window for screenshots with sway

With sway, be sure that your [kitty](https://sw.kovidgoyal.net/kitty/) window is floating. Then resize it and change kitty font size.

    swaymsg -r resize set width 1200 px; swaymsg -r resize set height 1000 px; kitty @ set-font-size 14

Font used: FiraCode Nerd Font from [Nerd Fonts](https://www.nerdfonts.com/font-downloads).
