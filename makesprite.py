import shutil
import glob
from PIL import Image

def tile_app(name):
    # image size for app is 192 x 192
    tile_set(name,"app",192,192)

def tile_garden(name):
    # image size for app is 96 x 96
    tile_set(name,"garden",96,96)

def tile_box(name):
    # image size for app is 64 x 64
    tile_set(name,"box",64,64)

def tile_set(name,folder,img_width,img_height):
    images = [Image.open(img_path,'r') for img_path in sorted(glob.glob("./images/"+name+"/"+folder+"/*.png"))]
    width = len(images) * img_width
    final_image = Image.new('RGBA', (width, img_height), (0,0,0,0))
    offset = (0,0)
    for img in images:
        final_image.paste(img,offset)
        offset = (offset[0]+img_width, 0)
    final_image.save("images/"+name+"/"+folder+".png")
    shutil.rmtree("images/"+name+"/"+folder)
