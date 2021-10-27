from flask import Blueprint, current_app as app, make_response

bp = Blueprint("root", __name__)


@bp.route('/predict_icd/<word>')
def predict_icd(word):
    vector = app.config['vectorizer'].vectorize(word)
    prediction = app.config['db'].get_most_similar(vector)
    response = make_response(prediction)
    response.mimetype = 'text/plain'
    return response
