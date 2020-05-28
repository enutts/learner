import sys
import json
from os import path
from random import shuffle

"""
this is a small library containing all the logic
"""
__author__ = "Eric Nutter"
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__email__ = "nuttereg@gmail.com"

helpstr = """ 
Manages flashcards and notes. 

Flags: 
    -h -> Displays this help string
    Flashcards: 
        -s {DECKS...} -> Study deck, or if more than one are supplied, it will interlieve them all, then shuffle
        -S {DECKS...} -> same as -s, but doesn't shuffle
"""

class Quiz:

    def __init__(self, filelist = []):
        self.name = ''
        self.cards = []
        self.json = {}

        if filelist != []:
            self.name = filelist[0].split('.')[0]

            for file in filelist:
                try:
                    with open(file, 'r') as deckfile:
                        [ self.cards.append(card) for card in deckfile.readlines() ]
                except OSError:
                    raise OSError
                except IOError:
                    raise IOError

    def __len__(self):
        l = len(self.cards)
        l += len(self.json)
        return l

    def to_legacy(self):
        #pass
        if len(self) == 0:
            print("need to figure out what kind of error this is")
        else:
            self.cards = self.json['cards']
            
    def to_json(self):
        if len(self.json) == 0:
            self.json = json.dumps({"name": self.name, "qa": [self.cards]}, \
                                    separators=(':', ','), \
                                    sort_keys=True, \
                                    indent=4)
    
    def save(self):
        """ saves the deck in both classical or json formats """
        legacy_name = self.name + '.txt'
        json_name = self.name + '.json'
        if not path.isfile(legacy_name):
            if self.cards == []:
                self.to_legacy()
            with open(legacy_name, 'w') as f:
                for c in self.cards:
                    f.write(c)
        
        if not path.isfile(json_name):
            if self.json == {}:
                self.to_json()
            with open(json_name, 'w') as f:
                f.write(self.json)
    
    def study(self, Shuffle=True):
        """ study the deck at the command line """
        if Shuffle == True:
            shuffle(self.cards)

        print('\n\t--hit enter to flip cards--\n')

        for card in self.cards:
            q, a = card.split('::')
            input(q)
            input(a)

class Notes:
    """This may never get implemented"""
    pass
    #__init__(self, notes_dir):
    #    self.dir = notes_dir

class Tasks:
    """This may also never get implemented""" 
    pass

# this is included in the library to keep the complete functionality of the program contained
# to one file. 
def main():
    if len(sys.argv) == 1:
        print(helpstr)
    elif len(sys.argv) >= 2:
        sys.argv.pop(0)
        if '-h' in sys.argv or '--help' in sys.argv:
            print(helpstr)
            return
        if '-s' in sys.argv:
            sys.argv.pop(sys.argv.index('-s'))
            quiz = Quiz(sys.argv)
            quiz.study()
            quiz.save()
        if '-S' in sys.argv:
            quiz = Quiz(sys.argv)
            quiz.study(Shuffle=False)
        if '-j' in sys.argv:
            sys.argv.pop(sys.argv.index('-j'))
            quiz = Quiz(sys.argv)
            quiz.to_json()
    else:
        print('something went wrong')

if __name__ == '__main__':
        main()