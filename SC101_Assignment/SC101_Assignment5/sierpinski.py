"""
File: sierpinski.py
Name: Jennifer Li
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = -6				# Controls the order of Sierpinski Triangle
LENGTH = 600			# The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		# The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100		# The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950		# The width of the GWindow
WINDOW_HEIGHT = 700		# The height of the GWindow
DELAY = 10				# The pause time

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: triangle layers.
	:param length: triangle length.
	:param upper_left_x: top left x-axis coordinate.
	:param upper_left_y: top left y-axis coordinate.
	:return: no return value.
	-----------------------------------------------------------------

	1. Drawing: draw triangle on the window.
	2. Judgment: set the conditions of the Base Case and Recursive Case.
		2-1. Base Case: when the order level is reduced to 0.
		2-2. Recursive Case: when the order level is greater than 0,
		2-3. Fool Proof design: this design simply prevents users from intentionally entering NEGATIVE order value.
	3. Recursion: tends the Recursive Case condition to the Base Case state.
	"""
	# 2. Judgment
	if order == 0:		# 2-1. Base Case
		return

	elif order < 0:		# 2-3 Fool Proof design
		order *= -1
		return sierpinski_triangle(order, length, upper_left_x, upper_left_y)

	elif order > 0:		# 2-2. Recursive Case
		# 1. Draw triangle on the window
		width = length * 0.5
		height = length * 0.866

		line_top = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		line_left = GLine(upper_left_x, upper_left_y, upper_left_x + width, upper_left_y + height)
		line_right = GLine(upper_left_x + length, upper_left_y, upper_left_x + length - width, upper_left_y + height)

		window.add(line_top)
		window.add(line_left)
		window.add(line_right)

		pause(DELAY)

		# 3. Recursion
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		sierpinski_triangle(order-1, length/2, upper_left_x+width, upper_left_y)
		sierpinski_triangle(order-1, length/2, upper_left_x+(width/2), upper_left_y + (height/2))


if __name__ == '__main__':
	main()
