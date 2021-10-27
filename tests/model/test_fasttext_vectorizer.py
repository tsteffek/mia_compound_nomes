from unittest import TestCase
from unittest.mock import patch, Mock

import fasttext

from model.fasttext_vectorizer import FastTextVectorizer


class TestFasttextVectorizer(TestCase):
    @patch('fasttext.load_model')
    def test_init(self, fasttext_mock):
        mock_path = 'mock_path'
        under_test = FastTextVectorizer(mock_path)
        fasttext_mock.assert_called_with(mock_path)

    @patch('fasttext.load_model')
    def test_vectorize(self, fasttext_mock):
        under_test = FastTextVectorizer('mock_path')
        mock_word = 'test_word'
        under_test.model = Mock()
        under_test.model.get_sentence_vector = Mock(return_value=mock_word)
        under_test.vectorize(mock_word)
        under_test.model.get_sentence_vector.assert_called_with(mock_word)
