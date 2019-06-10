#!/usr/bin/zsh
cd build
rm -rf *
cmake ..
make -j9
cd ..
./build/test_bspline