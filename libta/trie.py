from .node import Node


class Trie:
    def __init__(self):
        self.__root = Node()

    def __addword(self, node, word=None):
        if word is None:
            raise ValueError('NoneType cannot be entered in dictionary')
        elif word != '':
            firstchar, remaining = word[0:1], word[1:len(word)]
            if node.dictionary.get(firstchar, None) is None:
                node.dictionary[firstchar] = Node()
            node = node.dictionary[firstchar]
            self.__addword(node, remaining)
        else:
            node.is_end = True

    def populate(self, array):
        for word in array:
            self.__addword(self.__root, word)
        return self.__root

    def __findword_helper(self, node, word):
        if word != '':
            firstchar, remaining = word[0:1], word[1:len(word)]
            if node.dictionary.get(firstchar, None) is None:
                return False
            node = node.dictionary[firstchar]
            return self.__findword_helper(node, remaining)
        else:
            return node.is_end

    def findword(self, word):
        return self.__findword_helper(self.__root, word)
