# assets
Repo for assets


## Running it random
### _because I love rolling dice_

`$<blender executable> -b creatureGenerator.blend -y -P creator.py -- --random <number of creatures>`

for example:
`$ blender -b creatureGenerator.blend -y -P creator.py -- --random 1`

this will generate json files in the images folder with the same name as the creature generated

### What json!?
_YES JSON!_ And it'll look a little like this:

```

{
   "mea_eye_size":0.5000000,
   "mea_pointed_ears":0.000000,
   "mea_hair":0.000000,
   "mea_eyes_type":0.000000,
   "mea_finger_hands":0.000000,
   "mea_tongue":0.000000,
   "mea_flat_feet":0.000000,
   "mea_smile":0.000000,
   "mea_hair_color":0.000000,
   "mea_mouth":0.000000,
   "mea_body_color":0.000000,
   "mea_surround_teeth":0.000000,
   "mea_front_teeth":0.000000
}

```

All the values should be between 0 and 1.

### But I wanna load my own JSON files!
_YOU SUCK!_ But because I love you, you can just load a json file (like the one above) as a parameter

`$ blender -b creatureGenerator.blend -y -P creator.py -- <json file path> <creature name>`

`$ blender -b creatureGenerator.blend -y -P creator.py -- blank.json blank`

and you get this guy :D

![blank slate](http://i.imgur.com/7JfLhcX.png)

along with 3 sprite sheets

## `./images/blank/app.png`

![blank app sprite](http://i.imgur.com/Jo7r6LZ.png)

## `./images/blank/box.png`

![blank box sprite](http://i.imgur.com/Ech4VPT.png)

## `./images/blank/garden.png`

![blank garden sprite](http://i.imgur.com/B61Un1A.png)

# Docker usage
Theres a make file for convenience, this builds a base debian container with blender and nginx, run the blender script and hosts the images output with directory listing.
