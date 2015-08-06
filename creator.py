import bpy
from mathutils import Euler
import random
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) ))
from modifiers import *
from makesprite import *

NORMAL_ANGLE = (-0.40227848291397095, 0.16484859585762024, 6.682433605194092)
DEG_0_ANGLE = (-0.7853982448577881, -0.0, 0.0)
DEG_90_ANGLE = (-0.7853982448577881, -0.0, 1.570796251296997)
DEG_180_ANGLE = (-0.7853982448577881, -0.0, 3.141592502593994)
DEG_270_ANGLE = (-0.7853982448577881, -0.0, 4.71238899230957)
angles = [DEG_0_ANGLE,DEG_90_ANGLE,DEG_180_ANGLE,DEG_270_ANGLE]

# eyes<bool>, eyesScale<float>, hands<float>, feet<float>,
# ears<float>, teeth1<bool>, teeth2<bool>, tongue<bool>, mouth<float>,
# smile<float>, hair1<bool>, hair2<bool>, hair3<bool>, hair4<bool>,
# bodyColorR,G,B<float>, hairColorR,G,B<float>, name<string>
def creature_creator(args, name):
    print(args)
    eyes_type(args.pop(0))
    eye_size(args.pop(0))
    finger_hands(args.pop(0))
    flat_feet(args.pop(0))
    pointed_ears(args.pop(0))
    surround_teeth(args.pop(0))
    front_teeth(args.pop(0))
    tongue(args.pop(0))
    mouth(args.pop(0))
    smile(args.pop(0))
    hair([args.pop(0),args.pop(0),args.pop(0),args.pop(0)])
    body_color(args.pop(0),args.pop(0),args.pop(0))
    hair_color(args.pop(0),args.pop(0),args.pop(0))

    render_egg_box(name + "/box/egg")
    render_egg_garden(name + "/garden/egg")
    render_egg_app(name + "/app/egg")

    render_creature_box(name + "/box/creature") # normal angle
    for i in range(len(angles)):
        render_creature_garden(name + "/garden/c" + str(i) +"", angles[i])
    render_creature_app(name + "/app/creature")

    tile_app(name)
    tile_garden(name)
    tile_box(name)

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
    #two renders for each rotation
    render_scene(filepath, [0,10], 1, NORMAL_ANGLE, 1, -8)
    render_scene(filepath, [0,10], 1, NORMAL_ANGLE, 1, 8)

################# RENDERING SETTINGS ################
# set the time start, end, and current
def time_frame(start=0, end=None, current=None):
    bpy.context.scene.frame_start = start
    bpy.context.scene.frame_current = current or start
    bpy.context.scene.frame_end = end or start + 1

# generic use of rendering the scene
def render_scene(filepath, layers, image_size, angle, rotation=0, offset=0):
    # factor and offset: ONLY USE FOR ANIMATING A CAMERA SPIN,
    # OTHERWISE USE THE ANGLES ABOVE
    bpy.data.objects['camera-rotation-control']['factor'] = rotation
    bpy.data.objects['camera-rotation-control']['offset'] = offset

    bpy.data.cameras["Camera"]["scale"] = 3
    bpy.context.scene.render.resolution_percentage = (100 * 3) / image_size
    change_angle(angle)
    visible_layers(layers) # layers for creature
    bpy.context.scene.render.filepath = "//images/" + str(filepath) + ("b" if offset > 0 else "")
    bpy.ops.render.render(animation=True)

def visible_layers(vis):
    bpy.context.scene.layers = [i in vis for i in range(20)]

def change_angle(angle):
    bpy.data.objects['camera-control'].rotation_euler = Euler(angle,'XYZ')

######################## MAIN #######################
def main():
    argv = sys.argv
    if "--random" in argv:
        # if given random, just come up with random stuff
        args = argv[argv.index("--random")+1:]
        repeat = args[0]
        for creature in range(int(repeat)):
            config = [random.random() for i in range(20)]
            print(config)
            creature_creator(config,"rando" + str(time.time()))
    else:
        # last param is name, others get thrown in config
        creature_creator( argv[argv.index("--")+1:-1] , argv[-1] )

if __name__ == "__main__":
    main()
else:
    print(__name__)