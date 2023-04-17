import bpy
import bpy_extras
import mathutils
import numpy as np
import os
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector
import random

bpy.data.objects['Cube'].select_set(True)
bpy.ops.object.delete()
bpy.ops.wm.collada_import(filepath = 'C:/Users/Oliver/Documents/LEGO Creations/MODELS/legomix4.dae', auto_connect = True, find_chains = True, fix_orientation = True)
for obj in bpy.context.selected_objects:
  obj.name = "brick"

ob = bpy.context.active_object
ob.scale = (0.01, 0.01, 0.01)
bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
for obj in  C.selected_objects:
  obj.location[0] = 0 # x
  obj.location[1] = 0 # y
  obj.location[2] = 0 # z


for i in range(0, 1236):
  original_rotation = bpy.context.object.rotation_euler
  for scene in bpy.data.scenes:
    scene.render.resolution_x = 640
    scene.render.resolution_y = 480
  #SPEICHERT_DIE_2D_KOORDINATEN_UND_SPEICHERT_DIESE_AB
  scene = bpy.context.scene
  brick = bpy.data.objects['brick']
  bb_vertices = [Vector(v) for v in brick.bound_box]
  temp = bb_vertices[2]
  bb_vertices[2] = bb_vertices[3]
  bb_vertices[3] = temp
  temp2 = bb_vertices[6]
  bb_vertices[6] = bb_vertices[7]
  bb_vertices[7] = temp2
  mat = brick.matrix_world
  world_bb_vertices = [mat @ v for v in bb_vertices]
  co_2d = [world_to_camera_view(scene, scene.camera, v) for v in world_bb_vertices]  # from 0 to 1
  co_2d_new = np.delete(co_2d, 2, 1)
  co_2d_final = np.reshape(co_2d_new, -1)
  #KOORDINATEN_DES_CENTROID
  bpy.context.scene.camera
  #scene = bpy.context.scene
  obj = bpy.context.scene.camera
  centroid = mathutils.Vector((0.0, 0.0, 0.0))
  centr_2d = bpy_extras.object_utils.world_to_camera_view(scene, obj, centroid)
  #Centroid in die richtige form bringen
  centr_2d_temp = np.array(centr_2d)
  centr_2d_new = np.delete(centr_2d_temp, 2)
  centroid_2d_final = np.reshape(centr_2d_new, -1)
  for y_cord in range (0, 16):
    if (y_cord % 2 == 1):
      co_2d_final[y_cord] = 1 - co_2d_final[y_cord]
  #print(co_2d_final)
  max_h = []
  for j in co_2d_new:
    max_h.append(j[0])
  max_height = max(max_h)
  min_h = []
  for j in co_2d_new:
    min_h.append(j[0])
  min_height = min(min_h)
  max_w = []
  for j in co_2d_new:
    max_w.append(j[1])
  max_widht = max(max_w)
  min_w = []
  for j in co_2d_new:
    min_w.append(j[1])
  min_widht = min(min_w)
  height = max_height - min_height
  width = max_widht - min_widht
  #Generiert die labels, benötigt aber unbedingt vorher die koordinaten
  final = centroid_2d_final
  final = np.append(final, co_2d_final)
  final = np.append(final, height)
  final = np.append(final, width)
  np.savetxt(f'C:/python_work/test/temp{i}.txt', final, newline=" ", fmt='%f')
  file = open(f'C:/python_work/test/temp{i}.txt', 'r+')
  buffer = ""
  buffer += file.read()
  labels = "0 " + buffer
  file.truncate(0)
  file.close()
  with open(f'C:/python_work/singleshotpose/LINEMOD/legomix4_2/labels/{i:06d}.txt', 'w') as f:
    f.write(labels)
  brick.rotation_euler[1] = radians(i * 0.1 * (360.0 / 1236))
  #print(radians(i * 1.5 * (360.0 / 1000)))
  #print(radians(i * 1.5 * (360.0 / 1000)))
  brick.rotation_euler[2] = radians(i * 0.1 * (360.0 / 1236))
  bpy.context.scene.render.filepath = os.path.join('C:/python_work/singleshotpose/LINEMOD/legomix4_2/JPEGImages', ('%04d.jpg' % i))
  bpy.ops.render.render(write_still = True)



 

               
# def rotate_and_render(output_dir, output_file_pattern_string = '%d.jpg', rotation_steps = 1000, rotation_angle = 360.0, subject = bpy.context.object):

#     #Rotation, 0 = x, 1 = y, 2 = z (z most important, x 2nd most (1/4))
#     #subject.rotation_euler[0] = radians(step * (rotation_angle / rotation_steps))
#     subject.rotation_euler[1] = radians(step * 1.5 * (rotation_angle / rotation_steps))
#     print(radians(step * 1.5 * (rotation_angle / rotation_steps)))
#     subject.rotation_euler[2] = radians(step * 1.5 *(rotation_angle / rotation_steps))
#     print(radians(step * 1.5 *(rotation_angle / rotation_steps)))
#     bpy.context.scene.render.filepath = os.path.join(output_dir, (output_file_pattern_string % step))
#     bpy.ops.render.render(write_still = True)
#   subject.rotation_euler = original_rotation

# rotate_and_render('C:/Users/Oliver/Pictures/VR/test1', '%d.jpg', subject = bpy.data.objects["brick"])
