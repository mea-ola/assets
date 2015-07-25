# assets
Repo for assets

Should be run from the command line

`<blender executable>  -b creatureGenerator.blend -P make_creature.py -- --random`

params if you wanna do it manually (like a loser)

`time<float>, eyes<bool>, hands<float>, feet<float>, ears<float>, teeth1<bool>, teeth2<bool>, tongue<bool>, mouth<float>, smile<float>, hair1<bool>, hair2<bool>, hair3<bool>, hair4<bool>, bodyColorRed<float>, bodyColorGreen<float>, bodyColorBlue<float>, hairColorRed<float>, hairColorGreen<float>, hairColorBlue<float>, name<string>`

so for a completely blank one you do a little this:

`blender -b creatureGenerator.blend -P make_creature.py -- 0 True 0 0 0 False False False 0 0 False False False False 0 0 0 1 0 0 0 1 'blank'`

and you get this guy :D

![blank slate](http://i.imgur.com/7JfLhcX.png "This guy")
