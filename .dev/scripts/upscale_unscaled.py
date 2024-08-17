#!/usr/bin/env python3

from upscaler import upscale
from PIL import Image
import os
import json


files = []

# Find folders of images with a meta.json file
for root, _, filenames in os.walk("../../Media Unscaled"):
    for filename in filenames:
        if filename == "meta.json":
            with open(os.path.join(root, filename), "r") as f:
                meta = json.load(f)
                defaults = meta["defaults"]

                # Get images from meta.json
                for image in meta["images"]:
                    # Get image properties from meta.json or use defaults
                    upscale_factor = image.get("upscale_factor", defaults["upscale_factor"])
                    upscale_method = getattr(Image, image.get("upscale_method", defaults["upscale_method"]))

                    # Make path to new image if it doesn't exist
                    new_image_path = os.path.join(root.replace("Media Unscaled", "Media"), image["path"])
                    if not os.path.exists(new_image_path):
                        os.makedirs(os.path.dirname(new_image_path), exist_ok=True)

                    # Append to file info to list
                    #  (image path, upscale factor, upscale method, upscaled image path)
                    files.append((
                        os.path.join(root, image["path"]),
                        upscale_factor,
                        upscale_method,
                        new_image_path))

# Upscale images
for file in files:
    upscale(*file)
