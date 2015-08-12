#cd book-tex/
#pdflatex -shell-escape vim-pour-les-humains.tex
#pdflatex -shell-escape vim-pour-les-humains.tex
cd rst/fr
make clean
make epub
cd ../en
make clean
make epub
make latexpdf
cd ../../dist

ts=`date +%s`
mkdir $ts
cd ..
cp book-tex/vim-pour-les-humains.pdf dist/$ts
cp rst/fr/_build/epub/Vimpourleshumains.epub dist/$ts/vim-pour-les-humains.epub
cp rst/en/_build/epub/Vimforhumans.epub dist/$ts/vim-for-humans.epub
cp rst/en/_build/latex/Vimforhumans.pdf dist/$ts/vim-for-humans.pdf
cd dist/$ts
kindlegen vim-pour-les-humains.epub
kindlegen vim-for-humans.epub
cd ..
rm -rf vimpourleshumains/
rm vimpourleshumains.zip
cp -rf $ts vimpourleshumains
zip -r vimpourleshumains.zip vimpourleshumains
