#!/bin/bash

nginx

blender -b creatureGenerator.blend -y -P creator.py -- --random 1
ls ./images

tail -f /var/log/nginx/*
