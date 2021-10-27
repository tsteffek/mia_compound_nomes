import numpy as np
import pandas

from sklearn.metrics.pairwise import cosine_similarity

from model.vectorizer import Vectorizer


class FakeDB:
    """
    A simple class that holds our vectorized database in memory.
    Obviously we'd need something like FAISS for production,
    but setting that up is probably too much for this challenge.
    """

    def __init__(self, data_path, vectorizer: Vectorizer):
        db = pandas.read_csv(data_path, sep=';')
        db['vector'] = db['name'].apply(vectorizer.vectorize)

        self.db = db

    def get_most_similar(self, embedding: np.array):
        """
        Gets most similar id from our db based on cosine similarity.
        """
        # this part is a little ugly, but then again, we wouldn't have all of this in FAISS
        matrix = np.stack(self.db['vector'].to_numpy())
        similarities = cosine_similarity(embedding[np.newaxis, :], matrix)
        return self.db.loc[np.argmax(similarities), 'id']
