"""
File: CollectNewspaperKarel.py
Name: Jennifer Li
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    Main function where Karel executes the task of picking up a beeper
    and placing it in a new location.
    """
    turn_right()  # Turn Karel to face east
    move()  # Move one step forward
    turn_left()  # Turn Karel to face north
    for i in range(3):
        move()  # Move three steps forward
    pick_beeper()  # Pick up the beeper
    turn_around()  # Turn Karel around to face south
    for i in range(3):
        move()  # Move three steps back to the original row
    turn_right()  # Turn Karel to face west
    move()  # Move one step forward
    turn_right()  # Turn Karel to face north
    put_beeper()  # Place the beeper


def turn_right():
    """
    Turn Karel to the right by turning left three times.
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    karel turn left two times
    """
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
