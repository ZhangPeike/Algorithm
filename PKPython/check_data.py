#!/usr/bin/python
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


def CheckImageTimestamp(image_dir):
    pic_files = os.listdir(image_dir)
    print(pic_files[0])
    # input("Debug")
    list_timestamp = [float(x[-13:-4]) * 1e-6 for x in pic_files]
    list_timestamp = sorted(list_timestamp)
    np_timestamp = np.array(list_timestamp)
    np_timestamp_diff = np.diff(np_timestamp)
    plt.plot(np_timestamp_diff)
    plt.grid(True)
    plt.show()


def main():
    CheckImageTimestamp(sys.argv[1])


if __name__ == "__main__":
    main()