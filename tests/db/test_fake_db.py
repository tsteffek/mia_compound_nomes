from unittest import TestCase

import numpy as np
import pandas
from flask import Flask

from db.fake_db import FakeDB
from model.vectorizer import Vectorizer


class RandomVectorizer(Vectorizer):
    def __init__(self, length):
        self.length = length

    def vectorize(self, word):
        return np.random.rand(self.length)


class TestFakeDB(TestCase):
    def setUp(self) -> None:
        app = Flask(__name__)
        app.config['TESTING'] = True
        self.app = app.test_client()
        self.data_path = 'examples.csv'
        self.pd = pandas.read_csv(self.data_path, sep=';')
        self.vectorizer = RandomVectorizer(5)

    def test_init(self):
        under_test = FakeDB(self.data_path, self.vectorizer)
        pandas.testing.assert_frame_equal(self.pd, under_test.db.drop('vector', axis=1))
        self.assertIn('vector', under_test.db.columns)

    def test_get_most_similar(self):
        under_test = FakeDB(self.data_path, self.vectorizer)
        real_first_row = under_test.db.loc[0]
        expected_first_row = self.pd.loc[0]
        real_id = under_test.get_most_similar(real_first_row['vector'])
        self.assertEquals(real_first_row['name'], expected_first_row['name'])
        self.assertEquals(real_id, expected_first_row['id'])
