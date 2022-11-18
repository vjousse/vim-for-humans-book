# Create dist/ if necessary
mkdir -p dist

# Create French Directory
cd rst/fr
make clean
make epub

# Create English Directory
cd ../en
make clean
make epub
make latexpdf
cd ../../dist

# Make Distribution
ts=`date +%s`
mkdir $ts
mkdir $ts/fr
mkdir $ts/en
cd ..
cp book-tex/vim-pour-les-humains.pdf dist/$ts/fr
cp rst/fr/_build/epub/Vimpourleshumains.epub dist/$ts/fr/vim-pour-les-humains.epub
cp rst/fr/_build/epub/Vimpourleshumains.pdf dist/$ts/fr/vim-pour-les-humains-rst.pdf
cp rst/en/_build/epub/Vimforhumans.epub dist/$ts/en/vim-for-humans.epub
cp rst/en/_build/latex/Vimforhumans.pdf dist/$ts/en/vim-for-humans.pdf
cd dist/$ts

# Create Kindle Versions
cd fr
kindlegen vim-pour-les-humains.epub
cd ../en
kindlegen vim-for-humans.epub
cd ..

# Zip
cd ..
rm -rf vimpourleshumains/
rm vimpourleshumains.zip
cp -rf $ts vimpourleshumains
zip -r vimpourleshumains.zip vimpourleshumains
