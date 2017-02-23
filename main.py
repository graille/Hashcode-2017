import sys

fileName = sys.argv[1]

with open(fileName, "r") as file:
    lines = file.readlines()
    nb = 0
    for line in lines:
        if nb == 0:
            elts = line.split(' ')

        if nb == 1:
            pass

        nb += 1


