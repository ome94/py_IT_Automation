#!/usr/bin/env python3

import sys

def add(*args):
    """
    returns the sum  of values of a list of any length
    or lists.
    """
    
    return sum(args)

def format_input():
    # Iterate over the args list and convert every element
    #  EXCEPT the first into integers
    sys.argv = sys.argv[1:]
    for arg in sys.argv:
        if type(arg) == int:
            continue

        sys.argv[sys.argv.index(arg)] = int(arg)

def main():
    print(add(sys.argv[1], sys.argv[2]))

if __name__ == "__main__":
    main()

  