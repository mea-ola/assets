import bpy
from mathutils import Euler
import sys
import random
import time
from subprocess import call

NORMAL_ANGLE = (-0.40227848291397095, 0.16484859585762024, 6.682433605194092)
DEG_0_ANGLE = (-0.7853982448577881, -0.0, 0.0)
DEG_90_ANGLE = (-0.7853982448577881, -0.0, 1.570796251296997)
DEG_180_ANGLE = (-0.7853982448577881, -0.0, 3.141592502593994)
DEG_270_ANGLE = (-0.7853982448577881, -0.0, 4.71238899230957)
angles = [DEG_0_ANGLE,DEG_90_ANGLE,DEG_180_ANGLE,DEG_270_ANGLE]

# time<float>, eyes<bool>, eyesScale<float>, hands<float>, feet<float>,
# ears<float>, teeth1<bool>, teeth2<bool>, tongue<bool>, mouth<float>,
# smile<float>, hair1<bool>, hair2<bool>, hair3<bool>, hair4<bool>,
# bodyColorR,G,B<float>, hairColorR,G,B<float>, name<string>
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

    render_egg_box(args[21] + "/box/egg")
    render_egg_garden(args[21] + "/garden/egg")
    render_egg_app(args[21] + "/app/egg")

    render_creature_box(args[21] + "/box/creature") # normal angle
    for i in range(len(angles)):
        render_creature_garden(args[21] + "/garden/c" + str(i) +"", angles[i])
    render_creature_app(args[21] + "/app/creature")

    tile_app(args[21])
    tile_garden(args[21])
    tile_box(args[21])

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


##################### RENDERING #####################
def render_creature_box(filepath):
    time_frame(0)
    render_scene(filepath, [0,10], 3, NORMAL_ANGLE)

def render_egg_box(filepath):
    time_frame(0)
    render_scene(filepath, [14,10], 3, NORMAL_ANGLE)

def render_creature_garden(filepath, angle):
    time_frame(50,97)
    render_scene(filepath, [0,10], 2, angle)

def render_egg_garden(filepath):
    time_frame(0,42)
    render_scene(filepath, [14,10], 2, NORMAL_ANGLE)

def render_egg_app(filepath):
    time_frame(0,500)
    render_scene(filepath, [14,10], 1, NORMAL_ANGLE)

def render_creature_app(filepath, angle=NORMAL_ANGLE):
    time_frame(0,48)
    render_scene(filepath, [0,10], 1, NORMAL_ANGLE)

################# RENDERING SETTINGS ################
# set the time start, end, and current
def time_frame(start=0, end=None, current=None):
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_current = current or start
    bpy.context.scene.frame_end = end or start + 1

# generic use of rendering the scene
def render_scene(filepath, layers, image_size, angle):
    bpy.data.cameras["Camera"]["scale"] = 3
    bpy.context.scene.render.resolution_percentage = (100 * 3) / image_size
    change_angle(angle)
    visible_layers(layers) # layers for creature
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(animation=True)

def visible_layers(vis):
    bpy.context.scene.layers = [i in vis for i in range(20)]

def change_angle(angle):
    bpy.data.objects['camera-control'].rotation_euler = Euler(angle,'XYZ')

################# TILE MAKING ################
# requires imagemagick installed
def tile_app(name):
    call(["montage", "./images/"+name+"/app/*.png", "-tile", "8x",
    "-geometry", "192x192", "-background", "none", "images/"+name+"/app.png"])

def tile_garden(name):
    call(["montage", "./images/"+name+"/garden/*.png", "-tile", "8x",
    "-geometry", "96x96", "-background", "none", "images/"+name+"/garden.png"])

def tile_box(name):
    call(["montage", "./images/"+name+"/box/*.png", "-tile", "2x",
    "-geometry", "64x64", "-background", "none", "images/"+name+"/box.png"])

######################## MAIN #######################
def main():
    argv = sys.argv
    if "--random" in argv:
        # if given random, just come up with random stuff
        args = argv[argv.index("--random")+1:]
        repeat = args[0]
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
                "rando" + str(time.time())
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
