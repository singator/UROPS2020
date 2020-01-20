#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:51:44 2020

@author: wenhan
"""

import os
import argparse

parser = argparse.ArgumentParser(description='Run Seshat to get latex file')
parser.add_argument('scgfile')
args = parser.parse_args()

inputfile = f'{args.scgfile}'   
outputfile = '/home/wenhan/git/UROPS2020/Latex/' + str(inputfile).strip('scgink') + 'tex'

cmd = './seshat -c Config/CONFIG -i /home/wenhan/git/UROPS2020/SCG/' + inputfile +' -o out.inkml -r render.pgm -d out.dot > ' + outputfile
os.system(cmd)

with open(outputfile, "r") as f:
    line = f.readlines()[-1] 
f.close()
print(line)
with open(outputfile, "w") as f:
    f.write('\\documentclass{article}\n')
    f.write('\\usepackage[utf8]{inputenc}\n')
    f.write('\\begin{document}\n')
    f.write(line)
    f.write('\\end{document}\n')
f.close()
