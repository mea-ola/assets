import bpy
import inspect
import json
import random
import os

def _to_bool(value):
    return float(value) > 0.5

def _json_to_hash(filepath):
    json_file = open(filepath, 'r')
    json_string = json_file.read()
    return json.loads(json_string)

def _write_json(data, filepath):
    with open(filepath, 'w') as outfile:
        json.dump(data, outfile)

def modify_creature(filepath):
    creature_hash = _json_to_hash(filepath)
    for func_name in creature_hash:
        globals()[func_name](creature_hash[func_name])

def modify_creature_rand(name):
    functions = filter(lambda f: 'mea_' in f, globals())
    functions = filter(lambda f: 'mea_' in f, globals())
    creature_hash = {}
    for func_name in functions:
        creature_hash[func_name] = random.random()
        globals()[func_name](creature_hash[func_name])
    if not os.path.exists('images/'):
        os.makedirs('images/')
    _write_json(creature_hash, 'images/' + name + '.json')

# eye colors
def mea_eyes_type(type=0):
    bpy.data.materials['eye_color'].diffuse_color = (0,0,0) if _to_bool(type) else (1,1,1)
    bpy.data.materials['eye_pupil'].diffuse_color = (1,1,1) if _to_bool(type) else (0,0,0)

def mea_eye_size(scale):
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[0] = float(scale)
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[1] = float(scale)

# change hands and feet
def mea_finger_hands(fingerRange):
    bpy.data.shape_keys["Key"].key_blocks["hand_transform"].value = float(fingerRange)

def mea_flat_feet(flatRange):
    bpy.data.shape_keys["Key.001"].key_blocks["feet_transform"].value = float(flatRange)

# ears
def mea_pointed_ears(pointRange):
    bpy.data.shape_keys["Key.002"].key_blocks["Key 1"].value = -0.2 + 1.2 * float(pointRange)

# mouth
# True all teeth (except front teeth) out
def mea_surround_teeth(teeth=0):
    bpy.data.shape_keys["Key.006"].key_blocks["surround-teeth"].value = -1 if _to_bool(teeth) else 1

# True two front teeth out
def mea_front_teeth(teeth=0):
    bpy.data.shape_keys["Key.006"].key_blocks["front-teeth"].value = -1 if _to_bool(teeth) else 1

# False no tongue, True tongue out
def mea_tongue(tongue_out=0):
    bpy.data.shape_keys["Key.006"].key_blocks["tongue"].value = -1 if _to_bool(tongue_out) else 0

# 0 closed, 1 open
def mea_mouth(openness=0):
    bpy.data.objects['body']["mouth_open"] = -1.2 + 2.2 * float(openness)

# 0 sad, 1 happy
def mea_smile(happyness=0):
    bpy.data.shape_keys["Key.006"].key_blocks["smile"].value = -1.5 + 2.5 * float(happyness)

# hair, takes an float, 0/5 - 1/5 is the first type, 1/5 - 2/5 is the second type
def mea_hair(hair_type):
    particle_systems = bpy.data.objects['body'].particle_systems
    hair = int(float(hair_type * (len(particle_systems) + 1)))
    for h in range(len(particle_systems)):
        bpy.data.objects['body'].modifiers[particle_systems[h].name].show_render = h == hair

# body color, takes a 4 tuple (rgba)
def mea_body_color(rgb):
    r,g,b = '0.'+str(rgb)[2:4], '0.'+str(rgb)[4:6], '0.'+str(rgb)[6:8]
    bpy.data.materials['body'].diffuse_ramp.elements[1].color = (float(r),float(g),float(b),1)

# hair color, takes a 4 tuple (rgba)
def mea_hair_color(rgb):
    r,g,b = '0.'+str(rgb)[2:4], '0.'+str(rgb)[4:6], '0.'+str(rgb)[6:8]
    bpy.data.materials['hair'].diffuse_ramp.elements[0].color = (float(r),float(g),float(b),1)
