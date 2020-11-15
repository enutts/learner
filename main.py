import argparse
import sys
import os

import kim
import notes
import quiz

# main program to run app on command line

def main():
    parser = argparse.ArgumentParser(description='Comprehensive Command Line cognitive growth software')
    parser.add_argument('-d', '--deck',
                        nargs='*',
                        default=argparse.SUPPRESS,
                        help='location of deck(s) you want to study')
    parser.add_argument('-s', '--shuffle',
                        action='store_true',
                        default=argparse.SUPPRESS,
                        help='whether or not to randomize order of cards')
    parser.add_argument('-i', '--interleave',
                        action='store_true',
                        default=argparse.SUPPRESS,
                        help='shuffles decks together instead of running in sequence')
    parser.add_argument('-q', '--quick',
                        action='store_true',
                        default=argparse.SUPPRESS, 
                        help='takes a random fifth of each deck to study')

    args = parser.parse_args()
    print(args)
    

if __name__ == '__main__':
    main()