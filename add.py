#!/usr/bin/env python3

import sys

def add(a, b):
    # How can I define a function to take as many arguments 
    # as required when called,
    # i.e a function without a fixed number of parameters.
    # This way add() can be defined to take as many parameters
    # or little parameterswhen it is called.
    """
    returns the sum  of values of a list of any length
    or lists.
    """
    if type(a) != int or type(b) != int:
        raise ValueError("Only Numbers Please")
    return a + b

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

  