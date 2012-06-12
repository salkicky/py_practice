# coding: utf-8

import Image
import ImageDraw

try:
  img = Image.open("./sample.bmp")
  draw = ImageDraw.Draw( img )

  width, height = img.size
  draw.ellipse( (width/3, height/3, width*2/3, height*2/3), )

  del draw
  img.save("./result.bmp","BMP")
  del img

except IOError:
  print "Error"
