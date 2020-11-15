import json
from os import path
from random import shuffle as rshuf

__author__ = "Eric Nutter"
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__email__ = "nuttereg@gmail.com"

class Quiz:
    def __init__(self, filelist = []):
        self.cards = []

        if filelist != []:
            self.name = filelist[0].split('.')[0]

            for file in filelist:
                try:
                    with open(file, 'r') as deckfile:
                        for card in deckfile.readlines():
                            self.cards.append(card)
                except OSError:
                    raise OSError
                except IOError:
                    raise IOError

    def __len__(self):
        l = len(self.cards)
        return l
    
    def study(self, shuffle=False, interleave=False):
        """ study the deck """
        if shuffle == True:
            rshuf(self.cards)

        print('\n\t--hit enter to flip cards--\n')

        for card in self.cards:
            q, a = card.split('::')
            al = a.split(';;')
            input(q)
            for sa in al:
                input(sa)