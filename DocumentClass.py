#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:40:12 2020

@author: wenhan
"""

from NewPageClass import NewPage
import gzip
from lxml import etree as et
from bs4 import BeautifulSoup 

# function to unzip xopp to xml 
def UnzipXopp(fname):
    with gzip.open('/home/wenhan/git/UROPS2020/Input/' + fname) as f:
        content = f.readlines()
        s = ''
        for line in content:
            newline = str(line)[2:-3]
            s += newline
    f.close()
    
    root = et.XML(s)
    with open('/home/wenhan/git/UROPS2020/Input/' + fname.strip('.xopp') + '.xml', 'w') as newfile:
        newfile.write(et.tostring(root, xml_declaration=True).decode('utf-8'))
    newfile.close()
    
#function to convert xml to scgink
def Convert(fname):
    name = fname.strip('.xml')
    with open('/home/wenhan/git/UROPS2020/Input/{}'.format(fname), "r") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, 'lxml')
            pages = {}
            pagenum = 0
            for tag in soup.find_all('page'):
                pages[pagenum] = {}
                stroke_counter = 0
                for stroke in tag.find_all('stroke'):
                    text = str(stroke.text).split(' ')
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
                    pages[pagenum][stroke_counter] = coordinates
                    stroke_counter+=1
                pagenum += 1
    f.close()
           
    #write strokes content into scgink format
    for num in pages.keys():
        output = '/home/wenhan/git/UROPS2020/SCG/{}_{}.scgink'.format(name, num)
        newf= open(output,"w+")
        newf.write('SCG_INK\n')
        allstrokes = pages[num]
        newf.write(str(len(allstrokes))+'\n')
        for i in range(len(allstrokes)):
            stroke = allstrokes[i]
            pts = len(stroke['x'])
            newf.write(str(pts)+'\n')
            for j in range(pts):
                newf.write(str(stroke['x'][j])+' '+str(stroke['y'][j])+'\n')
        newf.close()
    return len(pages)

class Document:
    def __init__(self, xoppfile):
        UnzipXopp(xoppfile)
        fname = xoppfile.strip('.xopp')
        self.npages = Convert('{}.xml'.format(fname))
        self.pages = {}
        for i in range(self.npages):
            scg = '{}_{}.scgink'.format(fname, i)
            self.pages[i] = NewPage(scg)

    def getPage(self, pagenum):
        return self.pages[pagenum]
    
    def numPages(self):
        return self.npages


        
        
    
