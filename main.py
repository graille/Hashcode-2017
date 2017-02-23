#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import numpy as np

# Set the syspath
f_name = "main.py"
a_path = str(os.path.abspath(__file__))
new_sys_entry = a_path[0:len(a_path) - len(f_name)]

print("Add " + new_sys_entry + "to sys path")
sys.path.insert(0, new_sys_entry)

from model.Program import *

fileName = sys.argv[1]

_program = Program()

with open(fileName, "r") as file:
    lines = file.readlines()
    nb = 0
    nbRequest = -1
    for line in lines:
        line = line.rstrip('\n')
        elts = line.split(' ')
        if nb == 0:
            _program.nbVideos = int(elts[0])
            _program.nbEndpoints = int(elts[1])
            _program.nbCaches = int(elts[3])
            _program.cacheCapacity = int(elts[4])

            nbRequest = int(elts[2])
        if nb == 1:
            for elt in elts:

            pass

        nb += 1
