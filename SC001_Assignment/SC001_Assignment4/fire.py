"""
File: fire.py
Name: Jennifer Li
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage

# Threshold factor to determine if a pixel is part of a fire
HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    Processes an image to highlight areas of fire by enhancing red pixels.
    Any pixel where the red component is significantly higher than the average
    RGB value is turned bright red (255, 0, 0). All other pixels are converted to grayscale.

    :param filename: The file path of the image to be processed.
    :return: A new image with fire areas highlighted in red.
    """
    img = SimpleImage(filename)

    # Iterate through each pixel in the image
    for pixel in img:
        # Compute the average RGB intensity
        average = (pixel.red + pixel.green + pixel.blue) // 3

        if pixel.red > average * HURDLE_FACTOR:
            pixel.red = 255  # Max red intensity
            pixel.green = 0  # Remove green component
            pixel.blue = 0  # Remove blue component
        else:
            pixel.red = average
            pixel.green = average
            pixel.blue = average

    return img


def main():
    """
    Loads an image, displays the original version, processes it to highlight
    fire areas, and then displays the modified version.
    """
    # Load and display the original fire image
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()

    # Apply the fire detection and highlighting function
    highlighted_fire = highlight_fires('images/greenland-fire.png')

    # Display the processed image with fires highlighted
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
