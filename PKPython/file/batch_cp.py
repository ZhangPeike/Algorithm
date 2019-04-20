#!/usr/bin/python
import os
import sys
import shutil


# copy an image directory, ignoring its first 3 iamges
def BatchCopy(original_dir, dest_dir):
    list_images = os.listdir(original_dir)
    list_images = sorted(list_images)
    for i in range(3, len(list_images)):
        shutil.copy(os.path.join(original_dir, list_images[i]), dest_dir)


if __name__ == "__main__":
    BatchCopy(sys.argv[1], sys.argv[2])