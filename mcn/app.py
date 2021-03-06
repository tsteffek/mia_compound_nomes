import os

import pandas
from flask import Flask

from mcn.api.root import bp as default_bp
from mcn.db.fake_db import FakeDB
from mcn.model.fasttext_vectorizer import FastTextVectorizer

app = Flask(__name__)

# TODO: find a better place for this, so that it doesn't get run twice.
#  But that's apparently pretty hard to find in dev mode
app.config['vectorizer'] = FastTextVectorizer(os.getenv('model'))
app.config['db'] = FakeDB(os.getenv('data'), app.config['vectorizer'])
app.logger.debug('Loaded FastTest model and FakeDB.')

app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run()

# Let's run our examples here to test our approach; only if it's in debug mode and the flask reloader has run
if app.debug and bool(os.environ.get('WERKZEUG_RUN_MAIN')):
    log = app.logger.debug  # shortcut
    df = pandas.read_csv('test/examples.csv', sep=';')
    log(f'Run Examples\n{df.head()}')
    predictions = [
        app.config['db'].get_most_similar(
            app.config['vectorizer'].vectorize(alternative)
        ) for alternative in df['alternative']
    ]
    results = df['id'] == predictions
    log(f'Predictions\n{predictions}')
    log(f'Predicted {results.sum()} / {len(results)} correctly.')
