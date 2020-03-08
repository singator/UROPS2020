#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:39:47 2020

@author: wenhan
"""
import os
import pandas as pd


# class page to take in a scgink file
class NewPage:
    def __init__(self, scgfile):
        self.templines = pd.read_pickle('/home/wenhan/git/UROPS2020/line_coordinates')
        self.numlines = 0
        self.lines = {}
        fname = scgfile.strip('.scgink')

        # step 1: create a folder in Output using the filename (Eg. test)
        newpath = '/home/wenhan/git/UROPS2020/Output/' + fname
        try:
            os.mkdir(newpath)
        except OSError:
            print("Creation of the directory %s failed" % newpath)
            print('Directory may already exist')
        else:
            print("Successfully created the directory %s " % newpath)

        # step 2: for each line, create a new scgink file using the filename + line num (Eg. test_line1.scgink),
        #         run seshat to get latex string,
        #           create lines attribute (dictionary)
        # a) store coordinates to self.lines
        with open('/home/wenhan/git/UROPS2020/SCG/{}.scgink'.format(fname), 'r') as f:
            f.readline()
            totalstrokes = f.readline()

            for strokeindex in range(int(totalstrokes)):

                # 30 lines per page
                if strokeindex < 30:
                    f.readline()
                    f.readline()
                    f.readline()
                else:
                    npts = f.readline()
                    xcoor = []
                    ycoor = []
                    for j in range(int(npts)):
                        pt = f.readline().split(' ')
                        xcoor.append(float(pt[0]))
                        ycoor.append(float(pt[1]))

                    midpt = (max(ycoor) + min(ycoor)) / 2
                    for index, row in self.templines.iterrows():
                        if midpt > row['start'] and midpt < row['end']:
                            linenum = index
                            break

                    if linenum not in self.lines:
                        self.lines[linenum] = {}
                    self.lines[linenum][strokeindex] = [xcoor, ycoor]
        f.close()

        # b) for each line, create a new scginkfile in Output/fname directory and run seshat for each line
        index = 1
        for line in self.lines.values():
            output = '{}/{}_line_{}.scgink'.format(newpath, fname, index)
            with open(output, 'w') as linefile:
                linefile.write('SCG_INK\n')
                linefile.write(str(len(line)) + '\n')
                for strokes in line.values():
                    linefile.write(str(len(strokes[0])) + '\n')
                    for i in range(len(strokes[0])):
                        linefile.write(str(strokes[0][i]) + ' ' + str(strokes[1][i]) + '\n')
            linefile.close()
            os.chdir('/home/wenhan/git/UROPS2020/Seshat-master')
            tempfile = newpath + '/' + 'temp.txt'
            cmd = './seshat -c Config/CONFIG -i ' + output + ' -o out.inkml -r render.pgm -d out.dot > ' + tempfile
            os.system(cmd)
            with open(tempfile, "r") as f:
                latex = f.readlines()[-1]
            f.close()
            self.lines[index - 1] = latex
            index += 1
        self.numlines = len(self.lines)

    def getNumLines(self):
        return self.numlines

    def printLines(self):
        for line in self.lines.values():
            print(line)

    def getLines(self, n):
        if type(n) == int and n >= 0 and n < len(self.lines):
            return self.lines[n]
        else:
            return 'Line does not exist'





