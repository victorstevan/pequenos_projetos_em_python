#!/usr/bin/env python
"""
Author : Anonymous <Anonymous@DESKTOP-UECKJHR>
Date   : 2021-01-02
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- Choose the correct article!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Action"""

    args = get_args()
    word = args.word

    article = ''

    if word[0] in 'aeiou':
        article = 'an'
    elif word[0] in 'AEIOU':
        article = 'An'
    elif word[0] not in 'aeiou':
        if word[0].isupper():
            article = 'A'
        else:
            article = 'a'
   

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


"""    if word[0].lower() in 'aeiou':
        print(f"Ahoy, Captain, an {word} off the larboard bow!")
    else:
        print(f"Ahoy, Captain, a {word} off the larboard bow!")"""


"""    if word[0] == 'a':
        print(f'Ahoy, Captain, an {word} off the larboard bow!')
    elif word[0] == 'b':
        print(f'Ahoy, Captain, a {word} off the larboard bow!')
    else:
        print("Ahoy")"""


# --------------------------------------------------
if __name__ == '__main__':
    main()
