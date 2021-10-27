# MIA NLP Challenge - Compound Nouns

The task consists of setting up a small NLP NEL application.
The app is supposed to link compound words and their alternate writing to the same ICD code.

## Setup

Install the project using your favorite python environment manager via the requirements.txt, e.g.
```bash
virtualenv venv
python3 -m pip install -r requirements.txt
```

Download the fastText model of your choice, or just pick the official Facebook one (4.6gb, trained on Wikipedia and Common Crawl):
```bash
wget https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.de.300.bin.gz
gunzip cc.de.300.bin.gz
# for work out of the box magic:
mkdir models
mv cc.de.300.bin models/
# else adjust the model path in .flaskenv
```

Now everything should be setup, so run the application using
```bash
flask run
```

... or just do it all with `sh setup.sh`.

## Testing

To run the tests, run the usual python unittest command:
```bash
python -m unittest discover
```

## Examples

For automatic testing of the 7 given examples start the server in debug/development mode, but beware - this will have the model read twice and therefore take considerably longer. 

## A few words

### FastText?

...is a very low spec model, able to be run on even most laptops, as long as you have ~6gb free RAM. Obviously a modern model like BERT will perform better.

Nevertheless, even being that lightweight, fastText has some interesting properties for this kind of task, like that it's typo-resistant and can work with unseen words. Also, it's proven to be good enough for the given examples.

### FakeDB?

Setting up a "real" database like FAISS or elastic that's able to store and compare vectors more efficiently will be necessary for scaling this, but that's out of the 3-6 hours scope given for this task.

### The example GET /predict_icd “Zungengrundkarzinom” doesn't work!

Yes, because I don't exactly know what that's supposed to mean. I'm unfamiliar with the syntax and couldn't find anything like it online. I only know 2 ways of sending data with a GET request: Either using a get parameter or by making it part of the URL.
Since a GET parameter needs a name (e.g. `GET /predict_icd?word=Zungengrundkarzinom`) and I would have to guess or define that name, I went with the more modern approach of parsing the URL.

There's also the possibility of sending a request body with the GET request, but that's undefined in the http specification, so I'm assuming this option is out. 

Therefore, the correct way to interact with my app is:
```http request
GET /predict_icd/Zungengrundkarzinom
```