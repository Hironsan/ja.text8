# installation
virtualenv venv --python=python3
source venv/bin/activate
pip install mecab-python3
git clone https://github.com/attardi/wikiextractor.git
cd wikiextractor
mkdir extracted

# download, preprocess and make data
wget https://dumps.wikimedia.org/jawiki/20171001/jawiki-20171001-pages-articles.xml.bz2
python WikiExtractor.py -o extracted jawiki-20171001-pages-articles.xml.bz2
cd ..
mv wikiextractor/extracted .
python process.py
python tokenize.py

# post process
rm wikiextractor/jawiki-20171001-pages-articles.xml.bz2
rm tmp.txt
rm -rf extracted
rm -rf venv