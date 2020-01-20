#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 11:46:50 2020

@author: wenhan
"""

import argparse
import os

parser = argparse.ArgumentParser(description='Seshat pipeline: From .xml file to latex')
parser.add_argument('inputfile')
args = parser.parse_args()

file = f'{args.inputfile}'   
cmd = 'python3 ScginkConverter.py ' + file
os.system(cmd)
fname = str(file)

cmd = 'python3 PlotStrokes.py ' + fname + 'scgink'
os.system(cmd)

os.chdir('/home/wenhan/git/UROPS2020/Seshat-master')
cmd = 'python3 GetLatex.py ' + fname + 'scgink'
os.system(cmd)
os.chdir('/home/wenhan/git/UROPS2020')
