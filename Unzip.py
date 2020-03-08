#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 08:55:05 2020

@author: wenhan
"""

import gzip
from lxml import etree as et

def UnzipXopp(fname, output):
    with gzip.open('/home/wenhan/git/UROPS2020/Input/' + fname) as f:
        content = f.readlines()
        s = ''
        for line in content:
            newline = str(line)[2:-3]
            s += newline
    f.close()
    
    root = et.XML(s)
    with open('test.xml', 'w') as newfile:
        newfile.write(et.tostring(root, xml_declaration=True).decode('utf-8'))
    newfile.close()