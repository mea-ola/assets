import bpy
from mathutils import Euler
import sys
import random
import time

NORMAL_ANGLE = (0.26240038871765137, 0.09180232882499695, 4.485085964202881)
DEG_0_ANGLE = (0.5142398476600647, 0.013469358906149864, -2.178062915802002)
DEG_45_ANGLE = (0.5142397880554199, 0.013469358906149864, -2.9634644985198975)
DEG_90_ANGLE = (0.5142398476600647, 0.013469359837472439, -3.7488629817962646)
DEG_135_ANGLE = (0.5142397880554199, 0.013469361700117588, -4.534261226654053)
DEG_180_ANGLE = (0.5142398476600647, 0.013469361700117588, -5.31965970993042)
angles = [DEG_0_ANGLE,DEG_45_ANGLE,DEG_90_ANGLE,DEG_135_ANGLE,DEG_180_ANGLE]

# time<float>, eyes<bool>, eyesScale<float>, hands<float>, feet<float>,
# ears<float>, teeth1<bool>, teeth2<bool>, tongue<bool>, mouth<float>,
# smile<float>, hair1<bool>, hair2<bool>, hair3<bool>, hair4<bool>,
# bodyColorR,G,B<float>, hairColorR,G,B<float>, name<string>, scale<int>
def creatureCreator(args):
    day_time(args[0])
    light_eyes() if args[1] else nocturnal_eyes()
    eye_size(args[2])
    finger_hands(args[3])
    flat_feet(args[4])
    pointed_ears(args[5])
    surround_teeth(args[6])
    front_teeth(args[7])
    tongue(args[8])
    mouth(args[9])
    smile(args[10])
    hair([args[11],args[12],args[13],args[14]])
    body_color(args[15],args[16],args[17])
    hair_color(args[18],args[19],args[20])

    render_creature(args[21], args[22]) # normal angle
    render_egg(args[21] +"__egg",args[22])
    for i in range(len(angles)):
        render_creature(args[21] +"__"+ str(i), args[22], angles[i])
        render_walk_cycle(args[21] +"__"+ str(i), args[22], angles[i])
    render_creature_idle(args[21], args[22])
    render_egg_hatching(args[21], args[22])

# day sequence
# night = 1, day = 0
def day_time(night=0):
    bpy.data.materials['body'].diffuse_ramp.elements[1].position = 0.5 + night * 0.3
    bpy.data.materials['hair'].diffuse_ramp.elements[1].position = 0.5 + night * 0.2

# eye colors
def nocturnal_eyes():
    bpy.data.materials['eye_color'].diffuse_color = (0,0,0)
    bpy.data.materials['eye_pupil'].diffuse_color = (1,1,1)

def light_eyes():
    bpy.data.materials['eye_color'].diffuse_color = (1,1,1)
    bpy.data.materials['eye_pupil'].diffuse_color = (0,0,0)

def eye_size(scale):
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[0] = scale
    bpy.data.objects['Armature'].pose.bones["pupil-control"].scale[1] = scale

# change hands and feet
def finger_hands(fingerRange):
    bpy.data.shape_keys["Key"].key_blocks["hand_transform"].value = fingerRange

def flat_feet(flatRange):
    bpy.data.shape_keys["Key.001"].key_blocks["feet_transform"].value = flatRange

# ears
def pointed_ears(pointRange):
    bpy.data.shape_keys["Key.002"].key_blocks["Key 1"].value = -0.2 + 1.2 * pointRange

# mouth
# True all teeth (except front teeth) out
def surround_teeth(teeth=False):
    bpy.data.shape_keys["Key.006"].key_blocks["surround-teeth"].value = -1 if teeth else 1

# True two front teeth out
def front_teeth(teeth=False):
    bpy.data.shape_keys["Key.006"].key_blocks["front-teeth"].value = -1 if teeth else 1

# False no tongue, True tongue out
def tongue(tongueOut=False):
    bpy.data.shape_keys["Key.006"].key_blocks["tongue"].value = -1 if tongueOut else 0

# 0 closed, 1 open
def mouth(openness=0):
    bpy.data.objects['body']["mouth_open"] = -1.2 + 2.2 * openness

# 0 sad, 1 happy
def smile(happyness=0):
    bpy.data.shape_keys["Key.006"].key_blocks["smile"].value = -1.5 + 2.5 * happyness

# hair, takes an array [mohawk, mess, normal, long] to combine them
def hair(hairArray):
    bpy.data.objects['body'].modifiers["mohawk"].show_render = hairArray[0]
    bpy.data.objects['body'].modifiers["mess"].show_render = hairArray[1]
    bpy.data.objects['body'].modifiers["normal"].show_render = hairArray[2]
    bpy.data.objects['body'].modifiers["long"].show_render = hairArray[3]

# body color, takes a 4 tuple (rgba)
def body_color(r,g,b):
    bpy.data.materials['body'].diffuse_ramp.elements[1].color = (r,g,b,1)

# hair color, takes a 4 tuple (rgba)
def hair_color(r,g,b):
    bpy.data.materials['hair'].diffuse_ramp.elements[1].color = (r,g,b,1)

def render_creature(filepath,scale=3,angle=NORMAL_ANGLE):
    change_angle(angle)
    bpy.context.scene.frame_current = 0

    visible_layers([0,10]) # layers for creature
    bpy.data.scenes['creature'].render.image_settings.file_format = 'PNG' # one image
    bpy.data.scenes['creature'].render.image_settings.color_mode = 'RGBA' # use alpha layer
    bpy.data.cameras["Camera"]["scale"] = int(scale)
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(write_still=True)

def render_egg(filepath,scale=3,angle=NORMAL_ANGLE):
    change_angle(angle)
    bpy.context.scene.frame_current = 0

    visible_layers([14,10]) # layers for creature
    bpy.data.scenes['creature'].render.image_settings.file_format = 'PNG' # one image
    bpy.data.scenes['creature'].render.image_settings.color_mode = 'RGBA' # use alpha layer
    bpy.data.cameras["Camera"]["scale"] = int(scale)
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(write_still=True)

def render_creature_idle(filepath,scale=3,angle=NORMAL_ANGLE):
    change_angle(angle)
    bpy.context.scene.frame_current = 0
    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_end = 48

    visible_layers([0,10]) # layers for creature
    bpy.data.scenes['creature'].render.image_settings.file_format = 'H264'
    bpy.data.cameras["Camera"]["scale"] = int(scale)
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(animation=True)

def render_walk_cycle(filepath,scale=3,angle=NORMAL_ANGLE):
    change_angle(angle)
    bpy.context.scene.frame_current = 50
    bpy.context.scene.frame_start = 50
    bpy.context.scene.frame_end = 95

    visible_layers([0,10]) # layers for creature
    bpy.data.scenes['creature'].render.image_settings.file_format = 'H264'
    bpy.data.cameras["Camera"]["scale"] = int(scale)
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(animation=True)

def render_egg_hatching(filepath,scale=3):
    change_angle(NORMAL_ANGLE)
    bpy.context.scene.frame_start = 0
    bpy.context.scene.frame_current = 0
    bpy.context.scene.frame_end = 500

    visible_layers([14,10]) # layers for creature
    bpy.data.scenes['creature'].render.image_settings.file_format = 'H264'
    bpy.data.cameras["Camera"]["scale"] = int(scale)
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(animation=True)

def visible_layers(vis):
    layers = []
    for i in range(len(bpy.context.scene.layers)):
        layers.append(True if i in vis else False)
    bpy.context.scene.layers = layers

def change_angle(angle):
    bpy.data.objects['camera-control'].rotation_euler = Euler(angle,'XYZ')

def main():
    argv = sys.argv
    if "--random" in argv:
        # if given random, just come up with random stuff
        args = argv[argv.index("--random")+1:]
        scale = args[0]
        repeat = args[1]
        for creature in range(int(repeat)):
            config = [
                0,
                random.random() > 0.5,
                random.random(),
                random.random(),
                random.random(),
                random.random(),

                random.random() > 0.5,
                random.random() > 0.5,
                random.random() > 0.5,
                random.random(),
                random.random(),

                random.random() > 0.5,
                random.random() > 0.5,
                random.random() > 0.5,
                random.random() > 0.5,

                random.random(),random.random(),random.random(),
                random.random(),random.random(),random.random(),
                "rando" + str(time.time()), scale
            ]
            print(config)
            creatureCreator(config)
    else:
        # else go through the params and put them in the right type
        config = argv[argv.index("--")+1:]
        for i in range(len(config)):
            print(str(i) + " : " + str(config[i]))
            if config[i] == "True":
                config[i] = True
            elif config[i] == "False":
                config[i] = False
            else:
                try:
                    config[i] = float(config[i])
                except ValueError:
                    pass
            print(str(config[i]))
        print(config)
        creatureCreator(config)

if __name__ == "__main__":
    main()
else:
    print(__name__)
