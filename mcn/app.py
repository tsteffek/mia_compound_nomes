import os

import pandas
from flask import Flask

from api.root import bp as default_bp, predict_icd

app = Flask(__name__)

app.config['data'] = os.getenv('data')

app.register_blueprint(default_bp)

if __name__ == '__main__':
    app.run()

# Let's run our examples here to test our approach; only if it's in debug mode and the flask reloader has run
if app.debug and os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    log = app.logger.debug  # shortcut
    df = pandas.read_csv('./tests/examples.csv', sep=';')
    log(f'Run Examples\n{df.head()}')
    log(predict_icd())
    predictions = [alternative for alternative in df['alternative']]
    results = df['original'] == predictions
    log(f'Results\n{results}')
    log(f'Predicted {results.sum()} / {len(results)} correctly.')
