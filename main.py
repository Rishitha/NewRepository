import sys
sys.path.append('\Python27\Scripts')

from images2gif import writeGif
from PIL import Image
import os

file_names = sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
#['animationframa.png', 'animationframb.png', 'animationframc.png', ...] "

images = [Image.open(fn) for fn in file_names]

#print writeGif.__doc__
# writeGif(filename, images, duration=0.1, loops=0, dither=1)
#    Write an animated gif from the specified images.
#    images should be a list of numpy arrays of PIL images.
#    Numpy images of type float should have pixels between 0 and 1.
#    Numpy images of other types are expected to have values between 0 and 255.

filename = "my_gif.GIF"
writeGif(filename, images, duration=0.2)

print 'Content-type: text/html'
print

print '<HTML><HEAD><TITLE>Snap My Life</TITLE></HEAD>'
print '<BODY>'
print "<H1>Hello World!</H1>"
print '<img src="my_gif.GIF" />'

print '</BODY></html>'
