#!/usr/bin/env python
"""
Author : Victor Ribeiro <victor.stevan1>
Date   : 2021-01-02
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='A picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items and exit',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    isSorted = args.sorted

    if(isSorted):
        items.sort()

    if len(items) == 1:
        print(f"You are bringing {items[0]}.")
    elif len(items) == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    else:
        bringing = ""
        for item in items:
            if(item != items[-1]):
                bringing += f" {item},"

        print(f"You are bringing{bringing} and {items[-1]}.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
