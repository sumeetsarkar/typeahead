import os

from libta import Libta


DIR_NAME = os.path.dirname(__file__)
WORDS_1000 = os.path.join(DIR_NAME, 'words.1000.txt')
WORDS_10000 = os.path.join(DIR_NAME, 'words.10000.txt')
WORDS_100000 = os.path.join(DIR_NAME, 'words.100000.txt')


def test_trie(file, custom_queries):
    libta = Libta()
    # Populate the trie with 1000 words
    result = libta.populate_trie(file)

    print('Trie population result:', result)
    # Test words
    with open(file) as f:
        lines = f.read().splitlines()
        print('\n\n****** Testing for {} words ******'.format(len(lines)))
        for l in lines:
            if libta.is_word_present(l):
                continue
            print('Trie search test Failed')
            break
            
    for q in search_queries:
        print(q, libta.is_word_present(q))


listoffiles = [
    WORDS_1000,
    WORDS_10000,
    WORDS_100000
]

search_queries = [
    'Sumeet',
    'Sarkar',
    'loves',
    'coding',
    'documentcreatetextnode',
    'javaxservlethttphttpservletservice',
]

for file in listoffiles:
    test_trie(file, search_queries)


# Test LRU
from libta.lru import LRUCache

def test_lru(file):
    lrucache = LRUCache(10)
    with open(file) as f:
        lines = f.read().splitlines()
        for i in range(len(lines)):
            lrucache.add_item(i, lines[i])
        print('\n\nPrinting LRU state...\n')
        lrucache.print_all_items()


for f in listoffiles:
    test_lru(f)


# Simple Test
print('\n\nPrinting LRU state...\n')
lrucache = LRUCache(5)
lrucache.add_item(1, 1)
lrucache.add_item(10, 15)
lrucache.add_item(15, 10)
lrucache.add_item(10, 16)
lrucache.add_item(12, 15)
lrucache.add_item(18, 10)
lrucache.add_item(13, 16)
lrucache.add_item(20, 16)
lrucache.add_item(22, 16)
lrucache.add_item(23, 16)

lrucache.print_all_items()

print('get value for 15', lrucache.get(15))

print('get value for 18', lrucache.get(18))
lrucache.print_all_items()

print('get value for 20', lrucache.get(20))
lrucache.print_all_items()
