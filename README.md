# assets
Repo for assets

Make sure you have the following things installed: blender (v2.77), PIL/ Pillow (python image library fork), and Flask (python web microframework). If running off of Windows, remove the python install that comes with blender or allow libraries to be pulled from the system python.

## Running it random
### _because I love rolling dice_

`$ blender -b creatureGenerator.blend -y -P creator.py`

This will generate json files in the images folder with the same name as the creature generated

### What json!?
_YES JSON!_ And it'll look a little like this:

```
{
  "mea_body_color": 0.41241191188122994,
  "mea_hair": 0.48623670688775433,
  "mea_horns": 0.9299540399668266,
  "mea_finger_hands": 0.3932549268029555,
  "mea_surround_teeth": 0.880970702699059,
  "mea_eyes_type": 0.44525076924934903,
  "mea_eye_size": 0.011294256212641018,
  "mea_mouth": 0.33324649593153244,
  "mea_pointed_ears": 0.27936197073302405,
  "mea_hair_color": 0.4219901386486845,
  "mea_front_teeth": 0.5944592910566778,
  "mea_flat_feet": 0.8381430323175804,
  "mea_smile": 0.3595084753226234,
  "mea_tongue": 0.3105734338297026
}

```

All the values should be between 0 and 1.

### _TODO, load json to re-render creatures_

# Docker usage
Theres a make file for convenience, this builds a base debian container with blender and nginx, run the blender script and hosts the images output with directory listing.
