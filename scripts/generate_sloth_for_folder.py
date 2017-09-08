#!/usr/env/python
# Creates a new sloth labelling file by extracting from a master sloth labelling file
# only the data of the images contained in a given folder
import json
import argparse
import glob
import os

ap = argparse.ArgumentParser()
ap.add_argument("master_labelling_file")
ap.add_argument("image_folder")
ap.add_argument("filename_prefix")
args = vars(ap.parse_args())

images_in_folder = [os.path.basename(x) for x in glob.glob(args["image_folder"] + "/*")]
images_in_master_labelling_file = []
master_labelling_file_data = {}
with open(args["master_labelling_file"]) as json_data:
    master_labelling_file_data = json.load(json_data)
    images_in_master_labelling_file = [os.path.basename(x["filename"]) for x in master_labelling_file_data]

common_images = list(set(images_in_master_labelling_file).intersection(images_in_folder))

output = []
for image in master_labelling_file_data:
    if os.path.basename(image["filename"]) in common_images:
        newimage = image
        newimage["filename"] = args["filename_prefix"] + os.path.basename(image["filename"])
        output.append(newimage)

print(json.dumps(output, indent=2, sort_keys=True))

