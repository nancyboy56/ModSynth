import bpy
import random
import numpy as np

wall_collection = "Wall Mods"
mods_collection ="Modules"
rows = 8
column_space = 0.1
row_space =0.01;

wall = bpy.data.objects.get("Wall Python")
if wall:
    
    start = wall.matrix_world @ wall.data.vertices[0].co
    end = wall.matrix_world @ wall.data.vertices[1].co

mods = bpy.data.collections.get(mods_collection).objects[:]
print("test")

# delete objects in wall collection
collection = bpy.data.collections.get(wall_collection)

for o in collection.objects[:]:
    bpy.data.objects.remove(o, do_unlink=True)
    

x = start.x
y = start.y -1
#z = start.z
# y is actually z lol
z_distance = mods[0].dimensions.y+row_space;
z = start.z
row_height = mods[0]
for i in range(8):
    z += z_distance;
    x= start.x
    while x < end.x:
        
        mod_type = random.randint(0, len(mods)-1)
        new_mod = mods[mod_type].copy()
        bpy.data.collections["Wall Mods"].objects.link(new_mod)
        x = x + new_mod.dimensions.x/2;
        new_mod.location = (x, y ,z)
        x = x + new_mod.dimensions.x/2 +column_space
        #new_mod.name = "wowow"

def test_dup():
    
    if mods:
        duplicate_test = mods[1].copy()
        bpy.data.collections["Wall Mods"].objects.link(duplicate_test)
        # bpy.context.collection.objects.link(duplicate_test)
     #start = end
        if start:
    
            duplicate_test.location = (start.x, start.y -1, start.z)
        else:
            duplicate_test.location =(random.randint(0, 10),3,3)
    
        duplicate_test.name ="test1"
    
    else:
        print("doesn't work")    

