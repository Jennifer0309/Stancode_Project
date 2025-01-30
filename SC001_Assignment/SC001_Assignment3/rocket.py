"""
File: rocket.py
Name: Jennifer Li
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.
"""

SIZE = 2    # The rocket size


def main():
    """
    This rocket consist of 6 parts: 2 heads, 2 belts, 1 upper body and 1 lower body.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    To make a triangle part used at the ends of the rocket.
    """
    for i in range(SIZE):   # The variable "i" means which "row" to print

        # Print each row
        for j in range(SIZE - i):
            print(' ', end='')
        for j in range(i + 1):
            print('/', end='')
        for j in range(i + 1):
            print('\\', end='')

        print('')   # Move to next row


def belt():
    """
    To make a belt of the rocket.
    """
    print('+', end='')
    for i in range(2 * SIZE):
        print('=', end='')
    print('+')


def upper():
    """
    To make the upper part of the rocket.
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE - i - 1):
            print('.', end='')
        for j in range(i + 1):
            print('/', end='')
            print('\\', end='')
        for j in range(SIZE - i - 1):
            print('.', end='')
        print('|')


def lower():
    """
    To make the lower part of the rocket.
    """
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(SIZE - i):
            print('\\', end='')
            print('/', end='')
        for j in range(i):
            print('.', end='')
        print('|')


# --- DO NOT EDIT CODE BELOW THIS LINE --- #
if __name__ == '__main__':
    main()
