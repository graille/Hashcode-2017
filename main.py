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
from entity.Video import *
from entity.Cache import *
from entity.Endpoint import *

fileName = sys.argv[1]

_program = Program()

with open(fileName, "r") as file:
    # LINE 0
    line = file.readline()

    line = line.rstrip('\n')
    elts = line.split(' ')

    # informations
    _program.nbVideos = int(elts[0])
    _program.nbEndpoints = int(elts[1])
    _program.nbCaches = int(elts[3])
    _program.cacheCapacity = int(elts[4])

    for k in range(_program.nbVideos):
        v = Video(k)
        _program.addVideos(v)

    for k in range(_program.nbCaches):
        e = Endpoint(k)
        _program.addEndpoint(e)

    for k in range(_program.nbEndpoints):
        c = Cache(k, {}, {})
        _program.addCache(c)

    nbRequest = int(elts[2])

    # LINE 1
    line = file.readline()

    line = line.rstrip('\n')
    elts = line.split(' ')

    k = 0
    for elt in elts:
        _program.videos[k].size = int(elt)
        k += 1

    # LINES > 1
    numeroEndpoint = 0
    for k in []:
        line = file.readline()

        line = line.rstrip('\n')
        elts = line.split(' ')

        _program.endpoints[numeroEndpoint].dataCenterLatency = int(elts[0])

        for j in range(int(elts[1])):
            line = file.readline()

            line = line.rstrip('\n')
            elts = line.split(' ')

            # Update latency
            _program.endpoints[numeroEndpoint].latency[int(elts[0])] = int(elts[1])
            _program.caches[int(elts[0])].latency[numeroEndpoint] = int(elts[1])








    nb += 1
