from flask import Blueprint, current_app as app

bp = Blueprint("root", __name__)


@bp.route('/predict_icd/<word>')
def predict_icd(word):
    return app.config['db'].get_most_similar(app.config['vectorizer'].vectorize(word))
