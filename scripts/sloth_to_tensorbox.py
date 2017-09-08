#!/usr/env/python
# Convert a sloth labelling file to a tensorbox labelling file
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
        output_image["image_path"] = image["filename"]
        output_image["rects"] = []
        for annotation in image["annotations"]:
            output_rect = {}
            output_rect["x1"] = annotation["x"]
            output_rect["y1"] = annotation["y"]
            output_rect["x2"] = float(annotation["x"]) + float(annotation["width"])
            output_rect["y2"] = float(annotation["y"]) + float(annotation["height"])
            output_image["rects"].append(output_rect)
        output.append(output_image)

print(json.dumps(output, indent=2, sort_keys=True))
