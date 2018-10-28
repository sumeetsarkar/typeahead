from .utils import checkifstring
from .trie import Trie


class Libta:
    def __init__(self):
        self.__trie = Trie()

    def populate_trie(self, filepath = None):
        if not checkifstring(filepath):
            raise ValueError('filepath can only be a string')
        words = []
        with open(filepath) as f:
            lines = f.read().splitlines()
            for l in lines:
                words.append(l.lower())
        return self.__trie.populate(words)


    def is_word_present(self, word = None):
        if not checkifstring(word):
            raise ValueError('word can only be a string')
        word = word.lower()
        return self.__trie.findword(word)
