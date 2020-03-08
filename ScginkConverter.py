#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:21:36 2020

@author: wenhan
"""

from bs4 import BeautifulSoup
import argparse
import gzip
from lxml import etree as et

# function to unzip xopp to xml
def UnzipXopp(fname):
    with gzip.open('/home/wenhan/PycharmProjects/UROPS2020/Input/' + fname) as f:
        content = f.readlines()
        s = ''
        for line in content:
            newline = str(line)[2:-3]
            s += newline
    f.close()
    
    root = et.XML(s)
    with open('/home/wenhan/PycharmProjects/UROPS2020/Input/' + fname.strip('.xopp') + '.xml', 'w') as newfile:
        newfile.write(et.tostring(root, xml_declaration=True).decode('utf-8'))
    newfile.close()


parser = argparse.ArgumentParser(description='Convert xopp file to scgink file')
parser.add_argument('inputfile')
args = parser.parse_args()

#file name should be ****.xopp
file = f'{args.inputfile}'  
UnzipXopp(str(file))
 
filenameWOextension = str(file).strip('xopp')

#read strokes content
with open('/home/wenhan/PycharmProjects/UROPS2020/Input/'+filenameWOextension+'xml', "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    allstrokes = {}
    counter = 0
    for tag in soup.find_all("stroke"):
        text = str(tag.text).split(' ')
        x=[]
        y=[]
        for i in range(len(text)):
            if i%2==0:
                x.append(float(text[i]))
            else:
                y.append(float(text[i]))
        coordinates = {}
        coordinates['x'] = x
        coordinates['y'] = y
        allstrokes[counter] = coordinates
        counter+=1
f.close()

#write strokes content into scgink format
output = '/home/wenhan/PycharmProjects/UROPS2020/SCG/' + filenameWOextension + 'scgink'

newf= open(output,"w+")
newf.write('SCG_INK\n')
newf.write(str(len(allstrokes))+'\n')
for i in range(counter):
    stroke = allstrokes[i]
    pts = len(stroke['x'])
    newf.write(str(pts)+'\n')
    for j in range(pts):
        newf.write(str(stroke['x'][j])+' '+str(stroke['y'][j])+'\n')
newf.close()
