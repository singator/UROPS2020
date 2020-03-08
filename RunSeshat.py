#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:46:50 2020

@author: wenhan
"""

import argparse
import os

parser = argparse.ArgumentParser(description='Seshat pipeline: From xopp/scgink file to latex')
parser.add_argument('inputfile')
parser.add_argument('type')

args = parser.parse_args()

file = f'{args.inputfile}'   
ftype = f'{args.type}'
if str(ftype) == 'xopp':
    cmd = 'python3 ScginkConverter.py ' + file
    os.system(cmd)
    fname = str(file).split('.')[0] + '.scgink'
else:
    fname = str(file)

#plotting
cmd = 'python3 PlotStrokes.py ' + fname 
os.system(cmd)

os.chdir('/home/wenhan/PycharmProjects/UROPS2020/Seshat-master')
cmd = 'python3 GetLatex.py ' + fname 
os.system(cmd)
os.chdir('/home/wenhan/PycharmProjects/UROPS2020')
