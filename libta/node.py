class Node:
    def __init__(self):
        self.__dictionary = {}
        self.__is_end = False
    
    @property
    def dictionary(self):
        return self.__dictionary
    
    @dictionary.setter
    def dictionary(self, value):
        self.__dictionary = value

    @property
    def is_end(self):
        return self.__is_end
    
    @is_end.setter
    def is_end(self, value):
        self.__is_end = value

    def __str__(self):
        return 'Dictionary count: {}, End: :{}'.format(len(self.dictionary.keys()), self.is_end)
