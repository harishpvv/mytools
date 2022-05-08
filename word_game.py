from PyDictionary import PyDictionary
from english_words import english_words_set
import random
import numpy as np
from IPython.display import clear_output
import argparse

def argument(n, **kwargs):

    import argparse

    if 'argrrrrr' not in globals():
        globals()['argrrrrr'] = argparse.ArgumentParser()

    argrrrrr.add_argument(f"-{n}", f"--{n}", **kwargs)
    args, unknown = argrrrrr.parse_known_args()

    return vars(args)[n]

m = int(argument('m', default=10))

n = len(english_words_set)
d = PyDictionary()

def body():
    
    global score

    i = random.randint(0,n)
    word = list(english_words_set)[i]
    mean = d.meaning(word)

    hints = int(2*len(word)/3)
    places = np.random.choice(list(range(1,len(word))),hints,replace=False)
    
    dwd = ''
    for ii in range(len(word)):
        if ii in places:
            dwd+='_'
        else:
            dwd+=word[ii]

    df = mean[list(mean.keys())[0]][0]

    inp = input(f'{df} : \n\t{dwd}\n\n')

    got = False

    while got==False:

        if inp.lower()==word.lower(): 
            print('Correct!\n')
            got = True
            score += 1

        elif inp.lower()=='q':
            print(f'{word}\n')
            got = True

        else:
            print(f"{inp}: {d.meaning(inp)}\n")
            inp = input(f'Try again: ')

a = 0
score = 0
while a<m:
    try:
        body()
        clear_output(wait=True)
        a+=1
        print(f"Score {score}/{a}\n")
    except:
        pass
