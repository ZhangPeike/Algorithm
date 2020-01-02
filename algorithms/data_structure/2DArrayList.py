#!/usr/bin/python2
import os
import numpy as ny

list_a = [x * x for x in range(1, 11)]
print list_a

list_b = [x * x for x in range(1, 11) if x * x % 3 == 0]
print list_b

list_dir = [x for x in os.listdir('./')]
print list_dir

dict_a = {'x': 'A', 'y': 'B', 'z': 'C'}
print dict_a
list_key_value = [k + ' = ' + v for k, v in dict_a.items()]
print list_key_value

list_words = ['Hello', "World"]
list_words_new = [s.lower() for s in list_words]
print list_words_new

list_words_num = ['Hello', 2019, "world"]
list_words_filtered = [s.lower() for s in list_words_num if isinstance(s, str)]
print list_words_filtered

# m = input("Input rows: ")
# n = input("Input columns: ")
array = [[-1 for x in range(0, 8)] for i in range(3)]
# TODO: make a double linked list
# header
L = 0
array[2][L] = 0
array[1][L] = 13
print array