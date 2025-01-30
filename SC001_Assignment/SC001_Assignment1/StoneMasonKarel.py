"""
File: StoneMasonKarel.py
Name: Jennifer Li
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the lower left corner of the world, and there are
                   several broken pillars that are needed to be repaired.
    post-condition: Karel is at the lower right corner of world, facing east, and
                    the pillars have been repaired.
    This program makes Karel to repair all the broken pillars in the world, with three
    steps, which is represe
    """
    while front_is_clear():
        repair_colum()
        for i in range(4):
            move()
    # the last one Karel to build a column
    repair_colum()


def repair_colum():
    """
    pre-condition: Karel is at the bottom, facing east.
    post-condition: Karel is at the bottom, facing east.
    Karel climbs up the pillar, and repair with beepers.
    """
    turn_left()  # Turn Karel to face north (upwards)
    move_up_colum()
    put_top_beeper()
    move_back()
    turn_left()


def move_up_colum():
    """
    Move up the column, placing beepers where necessary
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()


def move_back():
    """
    Move Karel back to the base of the column by turning around
    and moving down until reaching the bottom.
    """
    turn_left()
    turn_left()  # Turn Karel to face south (downwards)
    while front_is_clear():  # Move down to the base of the column
        if on_beeper():
            if front_is_clear():
                move()


def put_top_beeper():
    """
    Ensure the topmost position has a beeper
    """
    if not front_is_clear():
        if not on_beeper():
            put_beeper()


def turn_right():
    """
    Turn Karel to the right by turning left three times.
    """
    for _ in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
