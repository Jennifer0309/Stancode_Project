"""
File: my_drawing.py
Name:Jennifer Li
----------------------
I wrote a piece of code to draw my favorite cartoon picture,
combining various GObjects (including GOval, GRect, GLine, GLabel, etc.) to create my own artwork!
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Bringing Luck Ryan
    Ryan is my favorite cartoon character.
    The more I watch it, the cuter it becomes,
    and my mood gets better and better.
    I wish you all write about coding and the more you write,
    the better your mood will be.
    """
    window = GWindow(width=800, height=700)
    l_ear = GOval(80, 80, x=230, y=200)
    window.add(l_ear)
    l_ear.filled = True
    l_ear.fill_color = 'orange'
    l_ear.color = 'orange'
    R_ear = GOval(80, 80, x=430, y=200)
    window.add(R_ear)
    R_ear.filled = True
    R_ear.fill_color = 'orange'
    R_ear.color = 'orange'

    face = GOval(320, 310, x=210, y=200)
    window.add(face)
    face.filled = True
    face.fill_color = 'orange'
    face.color = 'orange'

    l_eye = GOval(20, 20, x=290, y=335)
    window.add(l_eye)
    l_eye.filled = True
    l_eye.fill_color = 'black'
    R_eye = GOval(20, 20, x=430, y=335)
    window.add(R_eye)
    R_eye.filled = True
    R_eye.fill_color = 'black'

    l_eyebrow = GRect(55, 10, x=265, y=305)
    window.add(l_eyebrow)
    l_eyebrow.filled = True
    l_eyebrow.fill_color = 'black'
    R_eyebrow = GRect(55, 10, x=420, y=305)
    window.add(R_eyebrow)
    R_eyebrow.filled = True
    R_eyebrow.fill_color = 'black'

    l_mouth = GOval(40, 35, x=335, y=375)
    window.add(l_mouth)
    l_mouth.filled = True
    l_mouth.fill_color = 'white'
    l_mouth.color = 'white'
    R_mouth = GOval(40, 35, x=370, y=375)
    window.add(R_mouth)
    R_mouth.filled = True
    R_mouth.fill_color = 'white'
    R_mouth.color = 'white'

    nose = GOval(25, 20, x=360, y=365)
    window.add(nose)
    nose.filled = True
    nose.fill_color = 'black'

    l_cheek = GOval(45, 25, x=250, y=365)
    window.add(l_cheek)
    l_cheek.filled = True
    l_cheek.fill_color = 'pink'
    l_cheek.color = 'pink'
    R_cheek = GOval(45, 25, x=450, y=365)
    window.add(R_cheek)
    R_cheek.filled = True
    R_cheek.fill_color = 'pink'
    R_cheek.color = 'pink'

    l_heart = GOval(65, 65, x=310, y=520)
    window.add(l_heart)
    l_heart.filled = True
    l_heart.fill_color = 'red'
    l_heart.color = 'red'
    R_heart = GOval(65, 65, x=360, y=520)
    window.add(R_heart)
    R_heart.filled = True
    R_heart.fill_color = 'red'
    R_heart.color = 'red'

    triangle = GPolygon()
    triangle.add_vertex((312, 565))
    triangle.add_vertex((423, 565))
    triangle.add_vertex((368, 625))
    window.add(triangle)
    triangle.filled = True
    triangle.fill_color = 'red'
    triangle.color = 'red'

    label = GLabel('Have a good day', x=160, y=600)
    label.font = '-60'
    window.add(label)


if __name__ == '__main__':
    main()
