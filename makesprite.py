from subprocess import call

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
