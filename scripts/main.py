import bpy
import sys
import os

basedir = os.path.dirname(bpy.data.filepath) + "\scripts" # get scripts directory 

if basedir not in sys.path:
    sys.path.append(basedir) # add files to interpretate with python

import blender as bd
import imager as imgr

blender = bd.Blender()
imager = imgr.Imager()

number_of_generates = int(input("Enter number of generates: "))
number_of_pictures = int(input("Enter number of pictures: "))
number_of_feathers = int(input("Enter number of feathers: "))

cutter_angle = float(input("Enter cutter angle: "))

x = 0

for x in range(number_of_generates):
    px = blender.generate(number_of_feathers, number_of_pictures, cutter_angle)
    imager.create(number_of_pictures, px, cutter_angle)

print('Process finished! ')
