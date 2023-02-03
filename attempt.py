#!/bin/python

import math
import os
import random
import re
import sys
import numpy as np

pattern =r'[A-Za-z0-9_\s\#\%\!\$]'
pattern2 = r'[A-Za-z_\#\%\!\$]'

def raw_input():
    f = open("test.txt", "r")
    data  = f.read()
    return data

raw_input2 = re.findall(pattern, raw_input() )

width = raw_input2.index('\n')
while '\n' in raw_input2: raw_input2.remove('\n')

print('----input-----')
print(raw_input2)
#-------------obtain  array with shape (8,3)---------
arr = np.asarray(raw_input2)
newarr = arr.reshape(-1, width)
#-------------vertical traversal---------
arr = newarr.tolist()

result = []
for i in range(0, len(arr[0]) ):
  for row in arr:
    res = re.findall(pattern2, row[i])
    if res:
        result+= res 
    else:
        result += ''

print('----vertical traversal-----')
print(result)
result2 = ''.join(result)

#---------- remove initial occurance of #,$,% symbols -------
result2 = re.sub("#", " ", result2, 1)
result2 = re.sub("\$", "", result2, 1)
result2 = re.sub("%", " ", result2, 1)
result2 = re.sub("%", " %", result2, 1)
#print(re.sub(r'a-z\sa-z', "", result2))

print('----output-----')
print(result2)









    