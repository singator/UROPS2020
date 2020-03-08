#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 22:01:54 2020

@author: wenhan
"""

import numpy as np
import pandas as pd
lst = []
with open('/home/wenhan/git/UROPS2020/SCG/new_lines.scgink', 'r') as f:
    f.readline()
    numline = f.readline()
    for i in range(int(numline)):
        f.readline()
        f.readline()
        ycoor = float(f.readline().split(' ')[1])
        lst.append(ycoor)
f.close()

start = np.delete(np.insert(np.asarray(lst), 0, 0), 30)
end = np.asarray(lst)
d = {"start": start,
     'end': end}
df = pd.DataFrame(d)
fname = '/home/wenhan/git/UROPS2020/'
   
df.to_pickle(fname+'line_coordinates')

newdf = pd.read_pickle(fname+'line_coordinates')
print(newdf)