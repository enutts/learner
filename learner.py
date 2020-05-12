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
    def __init__(self):
        self.name = ""
        self.cards = []
        self.size = 0

    def from_file(self, filenames):
        decks = []
        for file in filenames:
            try:
                with open(file, 'r') as deckfile:
                    decks.append(deckfile.readlines())
            except IOError:
                print("{} does not appear to exist", file)
                break
        
        [ deck for deck in decks [ card for card in deck self.cards.append(card) ]]
        #for deck in decks:
        #    for card in deck:
        #        self.cards.append(card)

    def to_string(self):
        pass

    def to_json(self):
        """converts a String format deck to json"""
        print(json.dumps({"name": self.name, "qa": [self.cards]}, \
                          separators=(':', ','), \
                          sort_keys=True, \
                          indent=4))
    
    def study(self, shuffle=True):
        """ studies the deck """
        if shuffle == True:
            shuffle(self.cards)

        print('\n\t--hit enter to flip cards--\n')

        for card in self.cards:
            q, a = card.split('::')
            input(q)
            input(a)

class Notes:
    pass

def main():
    if len(sys.argv) == 0:
        print(helpstr)
    elif len(sys.argv) >= 1:
        sys.argv.pop(0)
        if '-h' in sys.argv or '--help' in sys.argv:
            print(helpstr)
            return
        if '-s' in sys.argv:
            shuffle = False
            sys.argv.pop(sys.argv.index('-s'))
        if '-j' in sys.argv:
            quiz = Quiz()
    else:
        print('something went wrong')
    
    sys.argv.pop(0)

    quiz = Quiz()

    try:
        quiz.from_file(sys.argv)
    except:
        print('{} don\'t seem to exist', sys.argv)

    if Shuffle == True:
        quiz.study()
    else:
        quiz.study(shuffle=False)

if __name__ == '__main__':
        main()