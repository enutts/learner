import sys
import json
from collections import namedtuple
from random import shuffle

"""
this is a small library containing all the logic
"""
__author__ = "Eric Nutter"
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__email__ = "nuttereg@gmail.com"

helpstr = """ lol """

class Quiz:
    def __init__(self, name='', cards = []):
        self.name = name
        self.cards = cards
        self.size = 0

    def from_file(self, filenames):
        decks = []
        for file in filenames:
            try:
                with open(file, 'r') as deckfile:
                    decks.append(deckfile.readlines())
            except IOError:
                print(file, "does not appear to exist")
                break

        [[ self.cards.append(card) for card in deck ]  for deck in decks ]

    def to_string(self):
        pass

    def to_json(self):
        """converts a String format deck to json"""
        print(json.dumps({"name": self.name, "qa": [self.cards]}, \
                          separators=(':', ','), \
                          sort_keys=True, \
                          indent=4))
    
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
    Shuffle = True
    if len(sys.argv) == 1:
        print(helpstr)
    elif len(sys.argv) >= 2:
        sys.argv.pop(0)
        if '-h' in sys.argv or '--help' in sys.argv:
            print(helpstr)
            return
        if '-s' in sys.argv:
            Shuffle = False
            sys.argv.pop(sys.argv.index('-s'))
        if '-j' in sys.argv:
            sys.argv.pop(sys.argv.index('-j'))
            quiz = Quiz(name="test_json")
            quiz.from_file(sys.argv)
            quiz.to_json()

    else:
        print('something went wrong')
    
    quiz = Quiz()

    try: # needs to be a try, except else... for now
        quiz.from_file(sys.argv)
    except:
        print(sys.argv, 'don\'t seem to exist')

    if Shuffle == True:
        quiz.study()
    else:
        quiz.study(Shuffle=False)

if __name__ == '__main__':
        main()