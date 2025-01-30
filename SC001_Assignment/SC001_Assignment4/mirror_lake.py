"""
File: mirror_lake.py
Name: Jennifer Li
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    Creates a vertically reflected image by mirroring the original image
    onto a blank canvas that is twice its height.

    :param filename: The file path of the original image.
    :return: A new image with the original and its reflection combined.
    """
    img = SimpleImage(filename)

    # Create a blank image with the same width but double the height
    mirror_lake_img = SimpleImage.blank(img.width, img.height * 2)

    # Iterate through each pixel in the original image
    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)

            # Copy original pixel to the top half of the new image
            mirror_lake_img_pixel1 = mirror_lake_img.get_pixel(x, y)
            mirror_lake_img_pixel1.red = img_pixel.red
            mirror_lake_img_pixel1.green = img_pixel.green
            mirror_lake_img_pixel1.blue = img_pixel.blue

            # Copy original pixel to the mirrored position in the bottom half
            mirror_lake_img_pixel2 = mirror_lake_img.get_pixel(x, img.height * 2 - y - 1)
            mirror_lake_img_pixel2.red = img_pixel.red
            mirror_lake_img_pixel2.green = img_pixel.green
            mirror_lake_img_pixel2.blue = img_pixel.blue

    return mirror_lake_img


def main():
    """
    Loads an image, displays the original version, applies the reflection effect,
    and then displays the final mirrored image.
    """
    # Load and display the original image
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()

    # Generate the reflected image
    reflected = reflect('images/mt-rainier.jpg')

    # Display the final mirrored image
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
