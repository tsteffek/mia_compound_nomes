virtualenv venv
python3 -m pip install -r requirements.txt

if ! test -f "models/cc.de.300.bin"; then
  wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.de.300.bin.gz
  gunzip cc.de.300.bin.gz
  mkdir models
  mv cc.de.300.bin models/
fi

python3 -m unittest discover

flask run