SHELL := /bin/bash

prepare:
	mkdir -p _build

hello: prepare
	gcc -o _build/hello src/hello.c
