#!/usr/bin/python3

import argparse
import configparser
# import sys
# import os

from quiz import Quiz
# import kim
# import notes

# main program to run app on command line
# this is still in very early development

__author__ = "Eric Nutter"
__license__ = "Apache 2.0"
__version__ = "0.0.1"
__email__ = "nuttereg@gmail.com"

def main():
    config = configparser.ConfigParser()
    config.read('test_config.ini')
    DECK_DIR = config['local_decks']['deck_dir']
    NOTES_DIR = config['local_notes']['notes_dir']
    SERV_PORT = config['local_server']['port']
    REMOTE_SERVS = config['remote_servers']['address'].split()

    parser = argparse.ArgumentParser(
                        description='Comprehensive Command Line cognitive growth software',
                        epilog='''Cards should be one line with questiong and answer separated 
                        with '::' and multi stage answers separated with ';;' ''')
    parser.add_argument('decks',
                        nargs='+',
                        default=[],
                        help='location of deck(s) you want to study')
    parser.add_argument('-s', '--shuffle',
                        action='store_true',
                        default=False,
                        help='whether or not to randomize order of cards')
    parser.add_argument('-q', '--quick',
                        action='store_true',
                        default=False, 
                        help='takes a random fifth of each deck to study')
    parser.add_argument('-g', '--web-gui',
                        action='store_true',
                        default=False,
                        help='Runs a local gui in web browser')
    args = vars(parser.parse_args())
    decks = args['decks']

    try:
        user_quiz = Quiz(decks)
        user_quiz.study(shuffle=args['shuffle'])
    except (OSError, IOError) as err:
        print(f'Trying to study {decks} failed \nerror: {err}')
        pass

    # print(DECK_DIR)
    # print(NOTES_DIR)
    # print(SERV_PORT)
    # print(REMOTE_SERVS)
  
if __name__ == '__main__':
    main()