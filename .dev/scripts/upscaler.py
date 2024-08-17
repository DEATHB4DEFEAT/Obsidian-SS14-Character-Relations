#!/usr/bin/env python3

from PIL import Image


def upscale(image_path='test.png', upscale_factor=2, upscale_method=Image.BOX, save_path=None):

    image = Image.open(image_path)
    width, height = image.size
    new_size = (width * upscale_factor, height * upscale_factor)
    new_image = image.resize(new_size, upscale_method)
    new_image.save(save_path or image_path + f'_{upscale_factor}x.png')


if __name__ == '__main__':
    import sys

    upscale(sys.argv[1], int(sys.argv[2]))
