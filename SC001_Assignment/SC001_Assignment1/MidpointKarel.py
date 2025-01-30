"""
File: MidpointKarel.py
Name: Jennifer Li
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at the lower left corner of a square world.
    post-condition: Karel stands at the midpoint of street 1 with a beeper.

    The purpose of this program is finding the midpoint of street 1 in any
    square world. In order to reach the goal, there are two procedures.
    First, put two beepers on the two ends of street respectively as two
    boundaries that remind Karel that it should turn around. Later, everytime
    Karel encounters a beeper, then it will turn around, pick it up, move a
    step toward to the midpoint, put it down, and move until it arrives the
    other beeper. By doing the procedures mentioned above repeatedly, Karel
    will find the midpoint when the two beepers meet each other.
    """
    put_on_head_and_tail()
    find_midpoint()


def put_on_head_and_tail():
    """
    pre-condition: Karel is at the lower left corner of a world.
    post-condition: There are two beepers on the two ends of street 1 respectively,
                     and Karel stands on the right beeper.

    In order to approach the midpoint, we should set two boundaries in advance, which
    reminds Karel that it should turn around. The two boundaries are represented by
    two beepers.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper_safely()  # for 1x1 world
    turn_around()


def find_midpoint():
    """
    pre-condition: Karel stands on the right beeper.
    post-condition: Karel stands on the midpoint of street 1 with a beeper.

    Everytime Karel encounters a beeper, it will turn around, pick it up,
    move a step forward, put it down, and move to the other beeper. By
    repeating the procedures above, the two beeper will meet each other
    eventually, and the position at that time is the midpoint that we are
    looking for.
    """
    if front_is_clear():  # for 1x1 world
        pick_beeper()
        move()
        put_beeper_safely()  # for 2x2 world
        if front_is_clear():
            move()
        while not on_beeper():  # move to the other beeper
            move()
            if on_beeper():
                turn_around()
                pick_beeper()
                move()
                put_beeper_safely()
                move()
        pick_beeper()  # remove the redundant beeper
        turn_around()
        move()
        put_beeper_safely()  # stand on the midpoint with a beeper


def turn_around():
    """
    Turns Karel around by 180 degrees.
    """
    turn_left()
    turn_left()


def put_beeper_safely():
    """
    Check if there has been a beeper before putting one.
    """
    if not on_beeper():
        put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
