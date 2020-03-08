#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:26:24 2020

@author: wenhan
"""

from DocumentClass import Document

doc = Document('example.xopp')
for i in range(doc.numPages()):
    print('Page {}:\n'.format(i))
    doc.getPage(i).printLines()
doc.toLatex()