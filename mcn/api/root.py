from flask import Flask, Blueprint

bp = Blueprint("default", __name__)


@bp.route('/predict_icd')
def predict_icd():  # put application's code here
    return 'Hello World!'
