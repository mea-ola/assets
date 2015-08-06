# assets
Repo for assets

Should be run from the command line

`$<blender executable> -b creatureGenerator.blend -y -P creator.py -- --random <number of creatures>`


for example:
`$ blender -b creatureGenerator.blend -y -P creator.py -- --random 1`


params if you wanna do it manually (like a loser)

```

eyes<bool> True for normal eyes (black pupils), False for nocturnal eyes (white pupils on black),
eyesScale<float> 1 has big eyes (pupils), 0 has tiny ones,
hands<float> 0 for sphere hands, as you go up to 1 you get fingers,
feet<float> 0 for sphere feet, as you go up to 1 you get flat feet,
ears<float> 0 for round ears, as you go up to 1 you get pointed ears,

teeth1<bool> True for teeth (except for front teeth),
teeth2<bool> True for front teeth,
tongue<bool> True for a tongue,
mouth<float> how open the mouth is- 0 for zipped shut, 1 for wide open,
smile<float> 0 for frown, 1 for smile,

hair1<bool> adds mohawk hair (can stack with other hair),
hair2<bool> adds messy hair (can stack with other hair),
hair3<bool> adds normal hair (can stack with other hair),
hair4<bool> adds long hair (can stack with other hair),

bodyColorRed<float> component of body red (0-1),
bodyColorGreen<float> component of body green (0-1),
bodyColorBlue<float> component of body blue (0-1),

hairColorRed<float> component of hair red (0-1),
hairColorGreen<float> component of hair green (0-1),
hairColorBlue<float> component of hair blue (0-1),

name<string>
```

so for a completely blank one you do a little this:

`$ blender -b creatureGenerator.blend -y -P creator.py -- 0 0.5 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 'blank'`

and you get this guy :D

![blank slate](http://i.imgur.com/7JfLhcX.png "This guy")

along with 3 sprite sheets
`./images/blank/app.png`
`./images/blank/box.png`
`./images/blank/garden.png`
