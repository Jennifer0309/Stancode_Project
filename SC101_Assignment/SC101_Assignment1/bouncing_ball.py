"""
File: bouncing_ball.py
Name:Jennifer Li
-------------------------
TODO:Create a program where a ball initially floats at the start.
It begins falling when the user clicks the window.
Its horizontal speed remains constant at VX, but its vertical speed increases with each frame due to gravity
(add GRAVITY to vertical speed).
Upon hitting the ground, the ball bounces back with its vertical speed becoming 90% of its previous value
(due to energy loss with each bounce, defined as REDUCE).
If the ball exits the window on the right, it resets to the start and stays put until the next click, resuming the fall.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# constant
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
X_START = 30
Y_START = 40

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE, x=X_START, y=Y_START)
ball.filled = True
ball.color = "black"
window.add(ball)

falling = False
bounce_count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start_falling)
    global falling, bounce_count
    vy = 0
    vx = VX

    while True:
        if bounce_count >= 3:
            break

        if falling:
            while True:
                pause(DELAY)
                ball.move(vx, vy)
                vy += GRAVITY
                if ball.y + SIZE > window.height:  # Checks if the ball has hit the ground
                    ball.y = window.height - SIZE  # Reset the ball's position to just above the ground
                    vy *= -REDUCE  # rebound speed reduction
                if ball.x > window.width:  # Checks if the ball has exited the window on the right side
                    ball.x = X_START
                    ball.y = Y_START
                    vy = 0
                    falling = False
                    bounce_count += 1
                    break

        pause(DELAY)


def start_falling(event):
    global falling
    falling = True


if __name__ == "__main__":
    main()
