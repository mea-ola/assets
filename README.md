# assets
Repo for assets

Should be run from the command line

`<blender executable>  -b creatureGenerator.blend -P make_creature.py -- --random <scale> <number of creatures>`

params if you wanna do it manually (like a loser)

```
time<float> (used only if you want the lighting to match a darker setting, keep at zero otherwise,

eyes<bool> True for normal eyes (black pupils), False for nocturnal eyes (white pupils on black),
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
scale<int> you can scale in integer increments
```

so for a completely blank one you do a little this:

`blender -b creatureGenerator.blend -P make_creature.py -- 0 True 0 0 0 False False False 0 0 False False False False 0 0 0 1 0 0 0 1 'blank' 1`

and you get this guy :D

![blank slate](http://i.imgur.com/7JfLhcX.png "This guy")
