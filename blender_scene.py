import bpy
import pickle

print("File blender_scene.py called")

fp_data = open("gem_data.dat", 'rb')
fin = open("extracted_models.txt", 'r')

data = pickle.load(fp_data)

models = fin.read()
models = models.split(' ')
print(models)

path = "/Volumes/My Passport/SHAPE/models-OBJ/models/"
x_dims_count = 0
y_dims_count = 0
z_dims_count = 0
for i in range(len(models)-1):
	# fdims = open("aligned_dims1.txt", 'r')
	# line = fdims.readline().split()
	# while line[0][4:] != models[i]:
	# 	line = fdims.readline().split()
	# print(line[1])
	# dims = line[1].split('\\,')
	full_id = 'wss.' + models[i]
	dims = data[full_id]['dims']
	rotation_info = data[full_id]['up']
	unit = float(data[full_id]['unit'][0])
	print(dims)
	print(rotation_info)
	print(unit)
	x_dims = float(dims[0])*unit
	y_dims = float(dims[1])*unit
	z_dims = float(dims[2])*unit
	if '*' in rotation_info:
		x_rot = 0
		y_rot = 0
		z_rot = 0
	# Change the following to account for rotation
	else:
		x_rot = 0
		y_rot = 0
		z_rot = 0
	print(x_dims, y_dims, z_dims)
	print(x_rot, y_rot, z_rot)
	# print("Command went into for loop")
	model_id = models[i] + '.obj'
	model_path = path + model_id
	imported_object = bpy.ops.import_scene.obj(filepath=model_path)
	print("Object", model_id, "imported")
	obj_object = bpy.context.selected_objects[0]
	# obj_object.location = (x_scale/1000,y_scale/1000,0) 
	obj_object.delta_scale = (unit, unit, unit)
	obj_object.rotation_euler = (x_rot, y_rot, z_rot)
	bpy.ops.object.origin_set(type = 'GEOMETRY_ORIGIN')
	if i>0:
		# if i==1:
		# y = y_dims_count + y_dims/2
		# obj_object.location = (0, y, 0)
		# y_dims_count += y_dims + 0.3
		# print("Object", i, "location = 0", y, "0\n\n")
		x = x_dims_count + (float(dims[0]))/200
		obj_object.location = (0, x, 0)
		x_dims_count += (float(dims[0]))/100


	# else:
	# 	x_dims_count += (x_dims/2) + 0.3
	# 	y_dims_count += (y_dims) + 0.3
	# 	z_dims_count += (z_dims/2) + 0.3

	else:
		x_dims_count += (float(dims[0]))/100 + 0.3
		y_dims_count += (float(dims[1]))/100 + 0.3
		z_dims_count += (float(dims[2]))/100 + 0.3


fin.close()
fp_data.close()