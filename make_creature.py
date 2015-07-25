import bpy
import sys
import random

# time<float>, eyes<bool>, hands<float>, feet<float>, ears<float>,
# teeth1<bool>, teeth2<bool>, tongue<bool>, mouth<float>, smile<float>,
# hair1<bool>, hair2<bool>, hair3<bool>, hair4<bool>,
# bodyColor<color>, hairColor<color>
def creatureCreator(args):
    day_time(args[0])
    light_eyes() if args[1] else nocturnal_eyes()
    finger_hands(args[2])
    flat_feet(args[3])
    pointed_ears(args[4])
    surround_teeth(args[5])
    front_teeth(args[6])
    tongue(args[7])
    mouth(args[8])
    smile(args[9])
    hair([args[10],args[11],args[12],args[13]])
    body_color(args[14],args[15],args[16])
    hair_color(args[17],args[18],args[19])
    render_scene(args[20])

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
    bpy.data.shape_keys["Key.006"].key_blocks["open"].value = -1.2 + 2.2 * openness

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

def render_scene(filepath):
    bpy.context.scene.render.filepath = "//images/" + str(filepath)
    bpy.ops.render.render(write_still=True)

def main():
    argv = sys.argv
    if "--random" in argv:
        # if given random, just come up with random stuff
        config = [
            0,
            random.random() > 0.5,
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
            "rando" + str(random.random())
        ]
        print(config)
        creatureCreator(config)
    else:
        # else go through the params and put them in the right type
        config = argv[argv.index("--")+1:]
        for i in range(len(config)):
            if config[i] == "True":
                config[i] = True
            elif config[i] == "False":
                config[i] = False
            else:
                try:
                    config[i] = float(config[i])
                except ValueError:
                    pass
        print(config)
        creatureCreator(config)

if __name__ == "__main__":
    main()
else:
    print(__name__)
