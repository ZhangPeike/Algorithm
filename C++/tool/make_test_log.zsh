#!/bin/zsh
cd build
cmake ..
make
cd ..
./bin/test_log
