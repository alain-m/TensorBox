#!/usr/env/python
# Simply check that all bounding box coordinates in the specified tensorbox labelling file are valid
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("filename")
args = vars(ap.parse_args())

with open(args.filename) as json_data:
    d = json.load(json_data)
    for rect in d["rects"]:
        if rect["x1"] > rect["x2"] or rect["y1"] > rect["y2"]:
            print "File " + str(args.filename) + " problem: {}".format(d)
