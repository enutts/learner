import sys
import json
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
        self.size = 0
        self.json = {}

        if filelist != []:
            
            # simple for now
            self.name = filelist[1]

            decks = []
            for file in filelist:
                names = filelist
                names = [ names.pop(names.index(filename)) for filename in names ]
                #print('names = ', names)
                try:
                    with open(file, 'r') as deckfile:
                        decks.append(deckfile.readlines())
                except IOError:
                    print(file, "does not appear to exist")
                    break

            [[ self.cards.append(card) for card in deck ]  for deck in decks ]

            self.size = len(self.cards)



    def to_string(self):
        """converts a json Quiz to the "legacy" format"""
        pass

    def to_json(self):
        """converts a String format deck to json"""
        self.json = json.dumps({"name": self.name, "qa": [self.cards]}, \
                                separators=(':', ','), \
                                sort_keys=True, \
                                indent=4)
    
    def study(self, Shuffle=True):
        """ studies the deck """
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
        if '-S' in sys.argv:
            quiz = Quiz(sys.argv)
            quiz.study(Shuffle=False)
        if '-j' in sys.argv:
            sys.argv.pop(sys.argv.index('-j'))
            quiz = Quiz(sys.argv)
            quiz.to_json()
    else:
        print('something went wrong')
    
    quiz = Quiz(sys.argv)

if __name__ == '__main__':
        main()