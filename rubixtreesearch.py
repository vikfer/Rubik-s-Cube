#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 16:49:15 2019

@author: vpfernandez
"""

"""
searchtree

goal: if 2 possibilités

0 = []
1 = [1]
2 = [2]
3 = [1,1]
4 = [1,2]
5 = [2,1]
6 = [2,2]
7 = [1,1,1]
....
"""

import math
import numpy as np

def logn(x,base):
    try:
        return math.log(x)/math.log(base)
    except:
        return 0

def search(i,df):
    
    degrees = np.floor(logn(i,df))
    out = []

    while degrees >= 0:
        out.append(int(i % df))
        degrees -= 1
        i -= (i % df)
        i /= df
    
    out.reverse()
    print(i, degrees, out)
    return out