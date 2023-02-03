#!/bin/python

import math
import os
import random
import re
import sys
import numpy as np

pattern ='[A-Za-z0-9_]'

def raw_input():
    f = open("test.txt", "r")
    data  = f.read()
    return data

'''
first_multiple_input = raw_input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
'''

raw_input2 = re.findall(r'[A-Za-z0-9_\s\#\%\!\$]', raw_input() )

print(raw_input2)

multirow=[]
i = 0
width = raw_input2.index('\n')
while '\n' in raw_input2: raw_input2.remove('\n')

print(raw_input2)

arr = np.asarray(raw_input2)
newarr = arr.reshape(-1, width)

print(newarr)

print('---iterate ---')

arr = newarr.tolist()
print(len(arr[0]))

result = []
for i in range(0, len(arr[0]) ):
  for row in arr:
    res = re.findall(r'[A-Za-z_\s\#\%\!\$]', row[i])
    if res:
        result+= res 
    else:
        result += ''
print(result)
result2 = ''.join(result)

result2 = result2.replace('#',' ',1)
result2 = result2.replace('$','',1)
result2 = result2.replace('%',' ',1)

#result2 = result2.replace(' ','',1)

print(re.sub(r'a-z\sa-z', "", result2))

print(result2)

#result2 = re.sub(r'[\#\$\%)]', '', result2)
#result2 = re.sub(r'[^#|%|%]', '', result2)
#result2 = result2.replace('#%',' ',1)


#result2 = re.sub(r'[(A-Za-z)\s(A-Za-z)]', '', result2)
#print(result2)


#print(re.sub("/[(A-Za-z)\s(A-Za-z)]/g", '', result2 ))

#print(re.sub("(\#) | (\$) | (\%)", " ", result2))


#  This is Matrix#  %!

exit()

matrix = []

for _ in xrange(n):
    matrix_item = raw_input()
    matrix.append(matrix_item)







    