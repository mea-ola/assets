import bpy
from mathutils import Euler
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) ))
from modifiers import *
from makesprite import *

from flask import Flask, send_file, request
app = Flask(__name__, static_url_path='')

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
def creature_creator(name):

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
    time_frame(30,76)
    render_scene(filepath, [14,10], 1, NORMAL_ANGLE)

def render_creature_app(filepath, angle=NORMAL_ANGLE):
    time_frame(0,46)
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
## makes a random creature. returns name ##
def make_random():
    name = "rando" + str(time.time())
    modify_creature_rand(name)
    creature_creator(name)
    return name

####################### APP #########################

## make a new random creature through flask ##
@app.route("/new")
def send_random_creature():
    name = make_random()
    return send_creature(name)

## retrieve a creature through flask ##
@app.route("/app/<creature>")
def send_creature_app(creature):
    return send_file('images/'+creature+'/app.png', mimetype="image/png")

## retrieve a creature through flask ##
@app.route("/garden/<creature>")
def send_creature_garden(creature):
    return send_file('images/'+creature+'/garden.png', mimetype="image/png")

## retrieve a creature through flask ##
@app.route("/box/<creature>")
def send_creature_box(creature):
    return send_file('images/'+creature+'/box.png', mimetype="image/png")

## retrieve a creature through flask ##
@app.route("/creature/<creature>")
def send_creature(creature):
    return '''
        <img src="{0}app/{1}" /> <br/>
        <img src="{0}garden/{1}" /> <br/>
        <img src="{0}box/{1}" />
    '''.format(request.url_root, creature)

## if main, run the flask app ##
if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0") # use host param for external visiblity
