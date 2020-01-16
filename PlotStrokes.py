#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:17:11 2020

@author: wenhan
"""
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Visualize Pen Input')
parser.add_argument('fname')
args = parser.parse_args()

# change source directory for own use
path = '/home/wenhan/git/UROPS2020/Seshat-master/SampleMathExps'

#file name should be ****.scgink
file = f'{args.fname}'   

fullpath = path+'/'+file
   
file = open(fullpath, 'r')
file.readline()
strokes = file.readline()
d={}
plt.figure(figsize=(9,6))
plt.axis('off')
for i in range(int(strokes)):
    npts = file.readline()
    d[i] = []
    xcoor = []
    ycoor = []
    for j in range(int(npts)):
        line = file.readline().split(' ')
        if line not in d[i]:
            d[i].append(line)
            x = line[0]
            y = line[1]
            xcoor.append(int(x))
            ycoor.append(-int(y))
    plt.plot(xcoor, ycoor, color='black')
    
newfname = 'Output.png'
plt.savefig(newfname)
plt.show()
file.close()
