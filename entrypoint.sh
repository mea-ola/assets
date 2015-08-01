#!/bin/bash

nginx

blender -b creatureGenerator.blend -y -P make_creature.py -- --random 10 1
ls ./images

tail -f /var/log/nginx/*
