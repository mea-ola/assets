TAGNAME=mea-ola/blender

all: build

build:
	docker build -t $(TAGNAME) .

run: build
	docker run -it -p 8080:80 $(TAGNAME)

run-dev: build
	docker run -ti -v `pwd`:/assets $(TAGNAME)
