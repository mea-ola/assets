TAGNAME=mea-ola/blender

all: build

build:
	docker build -t $(TAGNAME) .

run:
	docker run -ti $(TAGNAME)
