#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os

# Set the syspath
f_name = "main.py"
a_path = str(os.path.abspath(__file__))
new_sys_entry = a_path[0:len(a_path) - len(f_name)]

print("Add " + new_sys_entry + "to sys path")
sys.path.insert(0, new_sys_entry)

from model.Program import *

fileName = sys.argv[1]

with open(fileName, "r") as file:
    lines = file.readlines()
    nb = 0
    for line in lines:
        print(line)
        if nb == 0:
            elts = line.split(' ')

        if nb == 1:
            pass

        nb += 1


