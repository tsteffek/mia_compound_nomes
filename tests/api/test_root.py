from unittest import TestCase
from unittest.mock import Mock

from flask import Flask

from api.root import bp as root_bp
from db.fake_db import FakeDB
from model.vectorizer import Vectorizer


class TestRootAPI(TestCase):
    def setUp(self) -> None:
        app = Flask(__name__)
        app.config['TESTING'] = True

        self.mock_db = Mock(FakeDB)
        app.config['db'] = self.mock_db
        self.mock_vectorizer = Mock(Vectorizer)
        app.config['vectorizer'] = self.mock_vectorizer

        app.register_blueprint(root_bp)
        self.app = app.test_client()

    def test_predict_icd(self):
        input_value = 'value'
        returned_id = 'return_value'
        returned_vec = 'vec_return'
        self.mock_vectorizer.vectorize.return_value = returned_vec
        self.mock_db.get_most_similar.return_value = returned_id

        response = self.app.get(f'/predict_icd/{input_value}')

        self.mock_vectorizer.vectorize.assert_called_with(input_value)
        self.mock_db.get_most_similar.assert_called_with(returned_vec)
        self.assertEquals(response.data, returned_id.encode('utf-8'))
        self.assertEquals(response.status_code, 200)
