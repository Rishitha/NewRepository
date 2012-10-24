#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()
import sys
sys.path.append('\Python27\Scripts')

from images2gif import writeGif
from PIL import Image

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

numFile = open('numberUploads.txt', 'r')
number = numFile.read()
number = int(number) + 1
numFile.close()
numFile = open('numberUploads.txt', 'w')
numFile.write(str(number))
numFile.close()

directoryName = "user" + str(number)

if not os.path.exists(directoryName):
    os.makedirs(directoryName)

form = cgi.FieldStorage()

# Test if the file was uploaded
count = 1

while(count <= 5):
   fileitem = form['file' + str(count)]
   if fileitem.filename:
   
      # strip leading path from file name to avoid directory traversal attacks
      #fn = os.path.basename(fileitem.filename)
      fn = str(count) + '.png'
      uploadedFile = open(directoryName + '/' + fn, 'wb')
      uploadedFile.write(fileitem.file.read())
      uploadedFile.close()
      #message = 'The file "' + fn + '" was uploaded successfully'

   count += 1

file_names = sorted((fn for fn in os.listdir(directoryName) if fn.endswith('.png')))
#['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "

images = [Image.open(directoryName + '/' + fn) for fn in file_names]

#print writeGif.__doc__
# writeGif(filename, images, duration=0.1, loops=0, dither=1)
#    Write an animated gif from the specified images.
#    images should be a list of numpy arrays of PIL images.
#    Numpy images of type float should have pixels between 0 and 1.
#    Numpy images of other types are expected to have values between 0 and 255.

filename = str(number) + "my_gif.GIF"
writeGif(filename, images, duration=0.2)

print 'Content-type: text/html'
print

print '<HTML><HEAD><TITLE>Snap My Life</TITLE></HEAD>'
print '<BODY><CENTER>'
print '<H1>Your Animated Gif!</H1>'
print '<img src="' + str(number) + 'my_gif.GIF" />'
#print directoryName + '/' + fn

print '</BODY></CENTER></html>'
