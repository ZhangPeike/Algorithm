#!/bin/bash
cwd=$(pwd)
cd ~/A-Projects
git clone https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
mkdir build
cd build
cmake ..
cmake --build .
cd $cwd
