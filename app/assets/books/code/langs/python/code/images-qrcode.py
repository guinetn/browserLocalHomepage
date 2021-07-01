# QRCode
"""
https://betterprogramming.pub/how-to-modernize-your-kitchen-with-qr-codes-in-python-995aae0c4ccd

see also C:\tools\opencv-4.5.2\samples\python\qrcode.py

"""

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
data = 'Peppermint. Uses: indigestion, nausea. Steep time: 5-10 mins.'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('images-qrcode-peppermint.png')