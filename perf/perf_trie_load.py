# importing the required module 
import timeit

# code snippet to be executed only once 
mysetup = '''
from libta import Libta
'''

# code snippet whose execution time is to be measured 
code_load_trie = '''
libta = Libta()
libta.populate_trie('words.100000.txt')
'''
  
# timeit statement 
print(
    timeit.timeit(setup = mysetup, 
                    stmt = code_load_trie,
                    number = 1000)
)
