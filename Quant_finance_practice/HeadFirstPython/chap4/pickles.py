import pickle
from nester import print_lol

try:
    with open('test1.txt','wb') as file, with open ('test2.txt','wb') as file2:
        pickle.dum


new_man = []

try:
    with open('test1.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)

except IOError as err:
    print('No such file'+str(err))
except pickle.PicklingError as error:
    print('Pickling Error'+str(error))