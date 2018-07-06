#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 13:39:37 2018

@author: nilay
"""

from PIL import Image
im = Image.new("RGB", (800,800))
data = [(0, 255, 0) for y in range(im.size[1]) for x in range(im.size[0])]
im.putdata(data)
im.save("pix.jpg") 
