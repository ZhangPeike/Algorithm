#!/usr/bin/env python3
import math
def my_quadratic(a, b, c):
  t = (b * b - 4 * a * c)
  if t < 0 :
    return 
  else :
    x1 = (-b-math.sqrt(t))/(2*a) 
    x2 = (-b+math.sqrt(t))/(2*a) 
    return x1, x2

print('quatratic(2,3,1)',my_quadratic(2,3,1))
