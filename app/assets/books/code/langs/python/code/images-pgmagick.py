"""
pgmagick
http://www.graphicsmagick.org/
facilities such as resizing, rotation, sharpening, gradient images, drawing...

pip install pgmagick


"""

from pgmagick.api import Image 
  
img = Image('fox.png') 
  
# scaling image up to 1.5x 
img.scale((150, 100), 'fox_scaled')