"""
File: CheckerboardKarel.py
Name: Jennifer Li
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the lower left corner of the world, facing east.
    post-condition: Karel draws a checkerboard in the world with beepers.

    Karel finished drawing the checkerboard by putting beepers, and three functions
    are used to achieve the goal. Everytime Karel finishes a line, it will return
    to the left end of the line, and prepare to move to another line if the line
    it stands on is not the last one. Notice the program should satisfy any rectangle
    or square worlds.
    """
    if front_is_clear():
        while front_is_clear():
            fill_odd_line()
            go_back()
            if front_is_clear():  # check the last line
                move()
                turn_right()
                fill_even_line()
                go_back()
            if front_is_clear():  # check the last line
                move()
                turn_right()
    else:  # for the 1x1 and 8x1 world
        turn_left()
        fill_odd_line()


def fill_odd_line():
    """
    pre-condition: Karel is at the left end of a line.
    post-condition: Karel is at the right end of a line with the line is finished.

    Karel moves from left to right of a street to finish a line in checkerboard.
    The principle of putting beepers is put a beeper at the left end, then moves
    two steps and put another beeper repeatedly, until Karel reaches the right
    end of the line. Notice that there is a blank position between two adjacent beepers.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():  # check if Karel encounters a wall
            move()
            put_beeper()


def fill_even_line():
    """
    pre-condition: Karel is at the left end of a line.
    post-condition: Karel is at the right end of a line with the line is finished.

    Karel moves from left ot right of a line to finish a line in checkerboard.
    Compared to fill_odd_line(), the first beeper of this function will be put on
    second left position of a line. After that, Karel moves two steps and put another
    beeper repeatedly, until Karel reaches the right end of the line. Notice that
    there is also a blank position between two adjacent beepers.
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():  # check if Karel encounters a wall
            move()


def go_back():
    """
    pre-condition: Karel is at the right end of a line, facing east.
    post-condition: Karel is at the left end of a line, facing north.

    When Karel finished a line, it will return to the left end of the
    same line, facing north.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()  # facing north


def turn_around():
    """
    karel turn left two times
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Turn Karel to the right by turning left three times.
    """
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
