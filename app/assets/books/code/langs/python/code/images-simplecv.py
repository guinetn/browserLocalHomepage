"""
open-source package for building computer vision applications like face detection and recognition, object detection ...
"""

## source: http://simplecv.org/
from SimpleCV import Camera
# Initialize the camera
cam = Camera()
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
    # Make image black and white
    img = img.binarize()
    # Draw the text "Hello World" on image
    img.drawText("Hello World!")
    # Show the image
    img.show()