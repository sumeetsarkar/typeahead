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
