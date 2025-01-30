"""
File: best_photoshop_award.py
Name: Jennifer Li
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    Creative Concept: A Bright and Shining Future**
    """
    fig = SimpleImage('image_contest/Jennifer.JPG')  # 2048 x 2047
    bg = SimpleImage('image_contest/flower.jpg')  # 1170 x 1545
    bg.make_as_big_as(fig)  # 2048 x 2047
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            # avg = (fig_pixel.red+fig_pixel.green+fig_pixel.blue) // 3
            if fig_pixel.red == 255 and fig_pixel.green == 255 and fig_pixel.blue == 255:
                # White Screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
