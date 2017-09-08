#!/usr/env/python
# Concatenates two labelling files (sloth or tensorbox)
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("file1")
ap.add_argument("file2")
args = vars(ap.parse_args())

imagelist = []
imagelist1 = []
imagelist2 = []
with open(args["file1"]) as json_data:
    imagelist1 = json.load(json_data)
with open(args["file2"]) as json_data:
    imagelist2 = json.load(json_data)
imagelist = imagelist1 + imagelist2

print(json.dumps(imagelist, indent=2, sort_keys=True))
