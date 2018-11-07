"""
LRU Cache Implementation with CacheEntry type nodes
"""


from .cache_entry import CacheEntry


class LRUCache:

    def __init__(self, size):
        if size < 1:
            raise ValueError('LRU size cannot be less than 1')
        self.__size = size
        self.__dict = {}
        self.__front = None
        self.__end = None

    def get(self, cacheKey):
        result = self.__dict.get(cacheKey, None)
        if result is not None:
            self.remove_item(result)
            self.__move_item_to_front(result)
            return result
        return None

    def __move_item_to_front(self, cacheEntry):
        if cacheEntry is None:
            raise ValueError('CacheEntry cannot be None')
        cacheEntry.prevnode = None
        cacheEntry.nextnode = self.__front
        if self.__front is not None:
            self.__front.prevnode = cacheEntry
        self.__front = cacheEntry
        if self.__end is None:
            self.__end = self.__front
    
    def remove_item(self, cacheEntry):
        if cacheEntry is None:
            raise ValueError('CacheEntry cannot be None')
        if cacheEntry.prevnode is not None:
            cacheEntry.prevnode.nextnode = cacheEntry.nextnode
        else:
            self.__start = cacheEntry.nextnode
        if cacheEntry.nextnode is not None:
            cacheEntry.nextnode.prevnode = cacheEntry.prevnode
        else:
            self.__end = cacheEntry.prevnode

    def add_item(self, key, data = None):
        if data is None:
            data = key
        itemfound = self.get(key)
        if itemfound:
            itemfound.data = data
            return itemfound
        cacheEntry = CacheEntry(key, data)
        if len(self.__dict) == self.__size:
            self.__dict.pop(self.__end.key, None)
            self.remove_item(self.__end)
        self.__move_item_to_front(cacheEntry)
        self.__dict[key] = cacheEntry

    def print_all_items(self):
        temp = self.__front
        while temp is not None:
            print(temp)
            temp = temp.nextnode
