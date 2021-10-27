import fasttext

from model.vectorizer import Vectorizer


class FastTextVectorizer(Vectorizer):
    def __init__(self, model_path):
        self.model = fasttext.load_model(model_path)

    def vectorize(self, word):
        return self.model.get_sentence_vector(word)
