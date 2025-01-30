"""
File: blur.py
Name: Jennifer Li
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    Applies a blur effect to the given image by averaging the RGB values of
    each pixel with its neighboring pixels.

    :param img: The original image to be blurred.
    :return: A new image with the blur effect applied.
    """
    # Create a blank image with the same dimensions as the original image
    new_img = SimpleImage.blank(img.width, img.height)

    # Iterate through each pixel in the image
    for x in range(img.width):
        for y in range(img.height):
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            count = 0

            # Iterate over the surrounding pixels within a 3x3 grid
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    # Ensure the pixel is within the image bounds
                    if 0 <= i < img.width and 0 <= j < img.height:
                        pixel = img.get_pixel(i, j)
                        sum_red += pixel.red
                        sum_green += pixel.green
                        sum_blue += pixel.blue
                        count += 1

            # Compute the average RGB values and assign them to the new pixel
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = sum_red // count
            new_pixel.green = sum_green // count
            new_pixel.blue = sum_blue // count

    return new_img


def main():
    """
    Loads an image, displays it, applies multiple iterations of the blur effect,
    and then displays the final blurred image.
    """
    # Load and display the original image
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    # Apply the blur effect multiple times for a stronger effect
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)

    # Display the final blurred image
    blurred_img.show()


if __name__ == '__main__':
    main()
