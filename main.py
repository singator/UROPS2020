#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:26:24 2020

@author: wenhan
"""

from DocumentClass import Document

doc = Document('example10.xopp')
doc.prettyPrint()
#doc.evaluatePage(0, 'Solve')
#doc.evaluatePage(0, 'Reduce')

doc.toLatex()
