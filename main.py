#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:26:24 2020

@author: wenhan
"""

from DocumentClass import Document

doc = Document('example1.xopp')
doc.prettyPrint()
doc.evaluatePage(0, 'Solve')
doc.evaluatePage(1, 'Reduce')
doc.evaluatePage(2, 'Solve')

doc.toLatex()
