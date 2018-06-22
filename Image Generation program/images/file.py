# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:02:02 2018

@author: kansa
"""

import os,sys
import csv
import PIL
s=input("Enter the colour").lower()
with open("RGB.csv","r") as csvfile:
    pairs=dict(csv.reader(csvfile))
if(not s in  pairs): 
   sys.exit(0)
R,G,B=pairs[s].split(";")
R,G,B=int(R),int(G),int(B)
finalcolor=PIL.Image.new("RGB",(1024,1024),(R,G,B))
finalcolor.save("texture1.png")
check=1
os.system(r'cd C:\Users\kansa\Documents\GitHub\Text-To-Image\Image Generation program && model.obj')
