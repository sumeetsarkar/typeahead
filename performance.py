
# importing the required module 
import timeit

# code snippet to be executed only once 
mysetup = '''
from libta import Libta
'''

# code snippet whose execution time is to be measured 
mycode = '''
libta = Libta()
libta.populate_trie('words.100000.txt')
libta.is_word_present('javaxservlethttphttpservletservice')
'''
  
# timeit statement 
print(
    timeit.timeit(setup = mysetup, 
                    stmt = mycode,
                    number = 1)
)
