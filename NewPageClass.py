#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:39:47 2020

@author: wenhan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:26:15 2020

@author: wenhan
"""
import os
import pandas as pd

from bs4 import BeautifulSoup
import gzip
from lxml import etree as et

# functions to unzip xopp to xml then to scgink
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
    
def Convert(file):
    UnzipXopp(str(file))
    filenameWOextension = str(file).strip('xopp')
    
    #read strokes content
    with open('/home/wenhan/git/UROPS2020/Input/'+filenameWOextension+'xml', "r") as f:
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
    output = '/home/wenhan/git/UROPS2020/SCG/' + filenameWOextension + 'scgink'
    
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

class NewPage:
    def __init__(self):
        self.templines = pd.read_pickle('/home/wenhan/git/UROPS2020/line_coordinates')
        self.lines = {}
        self.numlines = 0
        
        
    def loadLines(self, xoppfile):
        #This function loads the xopp file into an empty Page with each value of the self.lines being the latex format
        
        # step 1: convert xopp to scgink
        fname = xoppfile.strip('.xopp')
        Convert(xoppfile)
        
        # step 2: create a folder in Output using the filename (Eg. test)
        newpath = '/home/wenhan/git/UROPS2020/Output/'+fname
        try:
            os.mkdir(newpath)
        except OSError:
            print ("Creation of the directory %s failed" % newpath)
            print ('Directory may already exist')
        else:
            print ("Successfully created the directory %s " % newpath)
            
        # step 3: for each line, create a new scgink file using the filename + line num (Eg. test_line1.scgink), 
        #         run seshat to get latex string,
        #           create lines attribute (dictionary)   
        # a) store coordinates to self.lines
        with open('/home/wenhan/git/UROPS2020/SCG/'+fname+'.scgink', 'r') as f:
            f.readline()
            totalstrokes = f.readline()
            
            for strokeindex in range(int(totalstrokes)):
                
                #30 lines per page
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
                    
                    midpt = (max(ycoor)+min(ycoor))/2
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
            output = newpath + '/' + fname + '_line' + str(index) + '.scgink'
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
            self.lines[index-1] = latex
            index += 1
        self.numlines = len(self.lines)

    
    def getNumLines(self):
        return self.numlines
    
    def printLines(self):
        for line in self.lines.values():
            print(line+'\n')
    
    def getLines(self, n):
        if type(n) == int and n >= 0 and n < len(self.lines):
            return self.lines[n]
        else:
            return 'Line does not exist'
        
        

# equation = NewPage()
# equation.loadLines('test2.xopp')
# equation.printLines()


