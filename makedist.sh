cd book-tex/
pdflatex -shell-escape vim-pour-les-humains.tex
pdflatex -shell-escape vim-pour-les-humains.tex
cd ../rst/fr
make clean
make epub
cd ../../dist

ts=`date +%s`
mkdir $ts
cd ..
cp book-tex/vim-pour-les-humains.pdf dist/$ts
cp rst/fr/_build/epub/Vimpourleshumains.epub dist/$ts/vim-pour-les-humains.epub
cd dist/$ts
kindlegen vim-pour-les-humains.epub
cd ..
rm -rf vimpourleshumains/
rm vimpourleshumains.zip
cp -rf $ts vimpourleshumains
zip -r vimpourleshumains.zip vimpourleshumains
