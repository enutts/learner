import argparse 

# main program to run app on command line

def main():
    parser = argparse.argumentParser(description='Comprehensive Command Line cognitive growth software')
    parser.add_argument('-d', '--deck', 
                        help='location of deck you want to study')
    parser.add_argument('-s', '--shuffle',
                        type=bool, 
                        help='whether or not to randomize order of cards')
    parser.add_argument('-i', '--interlieve',
                        nargs='*',
                        help='shuffles multiple complete decks together to study at once')
    parser.add_argument('-q', '--quick',
                        type=bool, 
                        help='takes a random fifth of each deck to study')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


if __name__ == '__main__':
    main()