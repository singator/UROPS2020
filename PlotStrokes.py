#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:17:11 2020

@author: wenhan
"""
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser(description='Visualize Pen Input')
parser.add_argument('scgfile')
args = parser.parse_args()

#file name should be ****.scgink
file = f'{args.scgfile}'   
newfname = '/home/wenhan/git/UROPS2020/Plots/' + str(file).strip('scgink') + 'png'

file = open('/home/wenhan/git/UROPS2020/SCG/'+file, 'r')
file.readline()
strokes = file.readline()
d={}
plt.figure(figsize=(16,6))
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
            xcoor.append(float(x))
            ycoor.append(-float(y))
    plt.plot(xcoor, ycoor, color='black')
plt.savefig(newfname)
plt.show()
file.close()
