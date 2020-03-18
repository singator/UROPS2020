#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 11:40:12 2020

@author: wenhan
"""

from NewPageClass import NewPage
from UnzipXopp import UnzipXopp
from Convert import Convert
import os


# xopp file has to start writing from the 1st line. If not error will occur. Need to fix
class Document:
    def __init__(self, xoppfile):
        UnzipXopp(xoppfile)
        fname = xoppfile.strip('.xopp')
        self.fname = fname
        self.npages = Convert('{}.xml'.format(fname))
        self.pages = {}
        for i in range(self.npages):
            scg = '{}_{}.scgink'.format(fname, i)
            self.pages[i] = NewPage(scg)

    def getPage(self, pagenum):
        return self.pages[pagenum]

    def numPages(self):
        return self.npages

    def toLatex(self):
        rootpt = os.getcwd()+'/'
        outputfile = '{}Latex/{}.tex'.format(rootpt, self.fname)
        with open(outputfile, "w") as f:
            f.write('\\documentclass{article}\n')
            f.write('\\usepackage[utf8]{inputenc}\n')
            f.write('\\begin{document}\n')
            for pageindex in self.pages.keys():
                f.write('\\section{}\n')
                page = self.pages[pageindex]
                for index in range(page.getNumLines()):
                    line = page.getLines(index)
                    f.write('$${}$$'.format(line))
            f.write('\\end{document}\n')
        f.close()

    def evaluatePage(self, n, type):
        self.getPage(n).evaluate(type)

    def prettyPrint(self):
        for i in range(self.numPages()):
            print('--------------------------------------------------------------------\n')
            print('Page {}:\n'.format(i))
            self.getPage(i).printLines()
            print('--------------------------------------------------------------------\n')




