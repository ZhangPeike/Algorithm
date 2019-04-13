#!/bin/zsh
cd build
cmake ..
make
cd ..
./bin/linked_list_stack
