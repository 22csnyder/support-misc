#Writes a QR Code. Savs it and reads it

'''Minimal version, example code
import qrcode
img=qrcode.make('https://xkcd.com/')
img.save('xkcd_url.png')
'''

'''more example:
/Users/christophersnyder/opt/anaconda3/lib/python3.9/site-packages/qrcode/__init__.py'''

#unexplored: there is also "from qrcode import image"
#part1: WRITING
#%%Method 1:
import qrcode
img1=qrcode.make('path-math.com')
img1.save('path-math_qr1.png')
#End Method 1

#%%Method 2
from qrcode.main import QRCode as QR #everywhere online says to do "from qrcode import QRCode" but it doesn't work.
qr=QR()
#qr.add_data('path-math.com')
qr.add_data('https://www.path-math.com/')
img2=qr.make_image();#img2.show()
img2.save('https-path-math_qr.png')
#End Method 2

#%%Method 3
'''
#Note "qr" is also a binary executable you can use in command line
#installing qrcode module was tricky. I'm not quire sure how I did i
qr "some ata" > "pmQR.png"'''
#End Method 3

#Part 2: READING
#%% Method 1
#zbarlight is a workaround for the more standard zbar (barcode reading lib)
# bc mac / windows (esp. conda) have trouble installing it
#"base" conda environment
from PIL import Image
import zbarlight

file_path = 'path-math_qr.png'
with open(file_path, 'rb') as image_file:
    image = Image.open(image_file)
    image.load()

# #wrote this part myself:
# if image.mode != 'RGB':
#     image_bw=image.copy()
#     image=image.convert('RGB')

#workaround if one of the known cause is that the image background color is the same as the foreground color 
#new_image = zbarlight.copy_image_on_background(image, color=zbarlight.WHITE)  # <<<<<<<<<<<<<<<< Add this line <<<<
#codes = zbarlight.scan_codes(['qrcode'], new_image)

codes=zbarlight.scan_codes(['qrcode'],image)
print('QR codes: %s' % codes)

# %%
