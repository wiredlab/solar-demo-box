SHELL=/bin/bash

# this is to make tex2svg from mathjax-node-cli show up in the PATH
# for the svgjax.py script
export PATH := $(HOME)/node_modules/.bin:$(PATH)

PYCKT=$(wildcard *.pyckt)
PYCKTSVG=$(addsuffix .svg,$(PYCKT))


# convention to identify which SVGs need rendering
SVGMATHSOURCE=$(wildcard *_math.svg)
SVGMATHRENDER=$(SVGMATHSOURCE:_math.svg=.svg)

# render all IPE files to svg
IPESOURCE=$(wildcard *.ipe)
IPERENDER=$(IPESOURCE:.ipe=.svg)

default: all

all: svgmath ipe pyckt


ipe: $(IPERENDER)

svgmath: $(SVGMATHRENDER)

pyckt: $(PYCKTSVG)

%.pyckt.svg: %.pyckt
	python3 $<

%.svg: %_math.svg
	./svgjax.py $< $@

%.svg: %.ipe
	iperender -svg $< $@.tmp.svg
	usvg --dpi 150 $@.tmp.svg $@ && rm $@.tmp.svg


# https://web.dev/replace-gifs-with-videos/
# https://www.smashingmagazine.com/2018/11/gif-to-video/
%.mp4: %.gif
	ffmpeg -i $< -b:v 0 -crf 25 $@

%.webm: %.gif
	ffmpeg -i $< -c vp9 -b:v 0 -crf 41 $@

