import argparse
import configparser
# import sys
# import os

# import kim
# import notes
from quiz import Quiz

# main program to run app on command line

__author__ = "Eric Nutter"
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__email__ = "nuttereg@gmail.com"

def main():
    configs = configparser.ConfigParser()


    parser = argparse.ArgumentParser(
                        description='Comprehensive Command Line cognitive growth software')
    parser.add_argument('decks',
                        nargs='*',
                        default=argparse.SUPPRESS,
                        help='location of deck(s) you want to study')
    parser.add_argument('-s', '--shuffle',
                        action='store_true',
                        default=False,
                        help='whether or not to randomize order of cards')
    parser.add_argument('-i', '--interleave',
                        action='store_true',
                        default=False,
                        help='shuffles decks together instead of running in sequence')
    parser.add_argument('-q', '--quick',
                        action='store_true',
                        default=False, 
                        help='takes a random fifth of each deck to study')
    args = vars(parser.parse_args())
    decks = args['decks']

    try:
        user_quiz = Quiz(decks)
        user_quiz.study(shuffle=args['shuffle'])
    except (OSError, IOError) as err:
        print(f'Trying to study {decks} failed \nerror: {err}')
        pass
  
if __name__ == '__main__':
    main()