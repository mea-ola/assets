import bpy

def to_bool(value):
    return float(value) > 0.5

# eye colors
def eyes_type(type=0):
    bpy.data.materials['eye_color'].diffuse_color = (0,0,0) if to_bool(type) else (1,1,1)
    bpy.data.materials['eye_pupil'].diffuse_color = (1,1,1) if to_bool(type) else (0,0,0)

def eye_size(scale):
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[0] = float(scale)
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[1] = float(scale)

# change hands and feet
def finger_hands(fingerRange):
    bpy.data.shape_keys["Key"].key_blocks["hand_transform"].value = float(fingerRange)

def flat_feet(flatRange):
    bpy.data.shape_keys["Key.001"].key_blocks["feet_transform"].value = float(flatRange)

# ears
def pointed_ears(pointRange):
    bpy.data.shape_keys["Key.002"].key_blocks["Key 1"].value = -0.2 + 1.2 * float(pointRange)

# mouth
# True all teeth (except front teeth) out
def surround_teeth(teeth=False):
    bpy.data.shape_keys["Key.006"].key_blocks["surround-teeth"].value = -1 if to_bool(teeth) else 1

# True two front teeth out
def front_teeth(teeth=False):
    bpy.data.shape_keys["Key.006"].key_blocks["front-teeth"].value = -1 if to_bool(teeth) else 1

# False no tongue, True tongue out
def tongue(tongueOut=False):
    bpy.data.shape_keys["Key.006"].key_blocks["tongue"].value = -1 if to_bool(tongueOut) else 0

# 0 closed, 1 open
def mouth(openness=0):
    bpy.data.objects['body']["mouth_open"] = -1.2 + 2.2 * float(openness)

# 0 sad, 1 happy
def smile(happyness=0):
    bpy.data.shape_keys["Key.006"].key_blocks["smile"].value = -1.5 + 2.5 * float(happyness)

# hair, takes an array [mohawk, mess, normal, long] to combine them
def hair(hairArray):
    bpy.data.objects['body'].modifiers["mohawk"].show_render = to_bool(hairArray[0])
    bpy.data.objects['body'].modifiers["mess"].show_render = to_bool(hairArray[1])
    bpy.data.objects['body'].modifiers["normal"].show_render = to_bool(hairArray[2])
    bpy.data.objects['body'].modifiers["long"].show_render = to_bool(hairArray[3])

# body color, takes a 4 tuple (rgba)
def body_color(r,g,b):
    bpy.data.materials['body'].diffuse_ramp.elements[1].color = (float(r),float(g),float(b),1)

# hair color, takes a 4 tuple (rgba)
def hair_color(r,g,b):
    bpy.data.materials['hair'].diffuse_ramp.elements[1].color = (float(r),float(g),float(b),1)
