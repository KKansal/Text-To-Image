# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:47:22 2018

@author: kansa
"""

import bpy
fp=open('selected.txt','r')
ids=fp.readlines()
for i in ids:
    i=i.rstrip('\n') 
    file_loc="C:\\Users\\kansa\\Desktop\\SHAPE\\Extracted\\models-OBJ\\models\\"+ i + '.obj'
    imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
#    bpy.data.scenes["Scene"].render.engine()
    print('done')
    obj_object = bpy.context.selected_objects[0]
    print('Imported name: ', obj_object.name)
