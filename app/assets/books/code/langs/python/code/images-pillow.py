from PIL import Image  #pip install pillow
me = Image.open('images-pillow-me.png')   # use inpixio or remove.bg
bg = Image.open('images-pillow-bg.jpg')
me.show()
bg.paste(me, (0,0), me)
bg.save('images-pillow_bg_added.jpg')


# make a dark image a little beautiful by increasing its contrast
from PIL import Image,ImageEnhance
img_original = Image.open("dark.jpg")
img_original.show("Original Image")
img = ImageEnhance.Contrast(img_original)
img.enhance(3.8).show("Image With More Contrast")

# https://www.youtube.com/c/ProgrammingHero/videos

"""
image processing library 
 manipulate images like resizing, adding filters...
 https://pillow.readthedocs.io/en/3.1.x/index.html
"""