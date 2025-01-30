"""
File: draw_line.py
Name:Jennifer Li
-------------------------
TODO:
Keep drawing "two dots and one line" on the window
The detailed process is as follows:
The position of the odd number of clicks is the line's starting point.
At this time, a hollow circle with a radius of constant SIZE will be drawn with the mouse click position as the center of the circle;
the even number of click positions is the end point of this line.
The hollow circle will disappear, and a straight line will be drawn at this point.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Global Variable
window = GWindow()
SIZE = 5
hole = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global hole, count
    if count % 2 == 0:
        # draw an empty circle
        window.add(hole, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
    else:
        line = GLine(hole.x + SIZE / 2, hole.y + SIZE / 2, mouse.x, mouse.y)
        # line = GLine( starting point x, starting point y, end point x, end point y)
        window.add(line)
        window.remove(hole)
    count += 1


if __name__ == "__main__":
    main()
