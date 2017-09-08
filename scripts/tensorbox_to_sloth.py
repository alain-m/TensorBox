#!/usr/env/python
# Converts a tensorbox labelling file to a sloth labelling file
import json
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("input_file")
args = vars(ap.parse_args())

output = []
with open(args["input_file"]) as json_data:
    imagelist = json.load(json_data)
    for image in imagelist:
        output_image = {}
        output_image["filename"] = image["image_path"]
        output_image["class"] = "image"
        output_image["annotations"] = []
        for annotation in image["rects"]:
            output_rect = {}
            output_rect["class"] = "rect"
            output_rect["x"] = annotation["x1"]
            output_rect["y"] = annotation["y1"]
            output_rect["width"] = float(annotation["x2"]) - float(annotation["x1"])
            output_rect["height"] = float(annotation["y2"]) - float(annotation["y1"])
            output_image["annotations"].append(output_rect)
        output.append(output_image)

print(json.dumps(output, indent=2, sort_keys=True))
