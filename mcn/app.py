import os

import pandas
from flask import Flask

from api.root import bp as default_bp
from db.fake_db import FakeDB
from model.fasttext_vectorizer import FastTextVectorizer

app = Flask(__name__)

if bool(os.environ.get('WERKZEUG_RUN_MAIN')):
    app.config['vectorizer'] = FastTextVectorizer(os.getenv('model'))
    app.config['db'] = FakeDB(os.getenv('data'), app.config['vectorizer'])

app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run()

# Let's run our examples here to test our approach; only if it's in debug mode and the flask reloader has run
if app.debug and bool(os.environ.get('WERKZEUG_RUN_MAIN')):
    log = app.logger.debug  # shortcut
    df = pandas.read_csv('../tests/examples.csv', sep=';')
    log(f'Run Examples\n{df.head()}')
    predictions = [
        app.config['db'].get_most_similar(
            app.config['vectorizer'].vectorize(alternative)
        ) for alternative in df['alternative']
    ]
    results = df['id'] == predictions
    log(f'Predictions\n{predictions}')
    log(f'Predicted {results.sum()} / {len(results)} correctly.')
