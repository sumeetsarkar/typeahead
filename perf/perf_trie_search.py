
# importing the required module 
import timeit

# code snippet to be executed only once 
mysetup = '''
from libta import Libta
libta = Libta()
libta.populate_trie('words.100000.txt')
'''

code_search_word = '''
libta.is_word_present('javaxservlethttphttpservletservice')
'''
  
# timeit statement 
print(
    timeit.timeit(setup = mysetup, 
                    stmt = code_search_word,
                    number = 1000000)
)
