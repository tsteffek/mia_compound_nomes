import abc


class Vectorizer(abc.ABC):
    @abc.abstractmethod
    def vectorize(self, word):
        raise NotImplementedError('Call to abstract method.')
