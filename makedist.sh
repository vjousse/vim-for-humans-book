# Create dist/ if necessary
mkdir -p dist

# Generate french epub from rst content
cd rst/fr
make clean
make epub
make latexpdf

# Generate english epub and pdf from rst content
cd ../en
make clean
make epub
make latexpdf

cd ../../book-tex

# We need to run it twice for the images to appear
# Don't ask me why 🤓
pdflatex -shell-escape vim-pour-les-humains.tex
pdflatex -shell-escape vim-pour-les-humains.tex


cd ../dist

# Make Distribution
ts=`date +%s`
mkdir $ts
mkdir $ts/fr
mkdir $ts/en
cd ..
cp book-tex/vim-pour-les-humains.pdf dist/$ts/fr
cp rst/fr/_build/epub/Vimpourleshumains.epub dist/$ts/fr/vim-pour-les-humains.epub
cp rst/fr/_build/latex/vimpourleshumains.pdf dist/$ts/fr/vim-pour-les-humains-rst.pdf
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
rm -f vimpourleshumains.zip
cp -rf $ts vimpourleshumains
zip -r vimpourleshumains.zip vimpourleshumains
