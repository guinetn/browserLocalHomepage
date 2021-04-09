'''
pillow
https://pypi.org/project/Pillow/
https://pillow.readthedocs.io/en/stable/
https://github.com/python-pillow/Pillow

Fork of the Python Image Library
To manipulate digital images
To create thumbnails, convert between file formats, rotate, apply filters, display images...
For automated image editing tasks

to write a resizing script that takes all images and creates various sizes of thumbnails, featured images, optimizes the file size. This saves literally gigabytes of data and bandwidth when used on websites.
You can turn vertical images horizontal, you can put a text or watermark on them, you could easily write a meme generator that takes custom text and prints it on pictures.
'''

from PIL import Image

im = Image.open("kittens.jpg")
im.show()
print(im.format, im.size, im.mode)
# JPEG (1920, 1357) RGB
