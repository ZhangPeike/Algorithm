#!/usr/bin/python
import os
import sys
import math
import shutil


# copy an image directory, ignoring its first 3 iamges
def BatchCopy(original_dir, dest_dir, n):
    list_images = os.listdir(original_dir)
    list_images = sorted(list_images)
    for i in range(min(len(list_images), n)):
        shutil.copy(os.path.join(original_dir, list_images[i]), dest_dir)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "usage: %s <original_dir> <dest_dir> <num_file>" % sys.argv[0]
        sys.exit(1)
    BatchCopy(sys.argv[1], sys.argv[2], int(sys.argv[3]))