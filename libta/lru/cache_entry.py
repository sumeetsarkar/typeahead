"""
LRU Cache Entry class
"""


class CacheEntry:

    def __init__(self, key, data, prevnode = None, nextnode = None):
        self.__key, self.__data = key, data
        self.prevnode, self.nextnode = prevnode, nextnode
    
    @property
    def key(self):
        return self.__key

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def __str__(self):
        return '[{}, {}]'.format(self.key, self.data)
