# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:39:25 2019

@author: victo_000
"""

import numpy as np
import random as rd
from rubik_qol import logn
from rubik_cube_class import cube
from rubik_generator import rubix

color_u = rubix.u_layer[1,1] #Color 
color_f = rubix.f_layer[1,1] #Color 
color_l = rubix.l_layer[1,1] #Color 
color_b = rubix.b_layer[1,1] #Color 
color_r = rubix.r_layer[1,1] #Color 
color_d = rubix.d_layer[1,1] #Color 

switch = 0

def search(i,df):
    
    i = int(i)
    #y = i
    df = int(df)
    
    degrees = np.floor(logn(i,df))
    out = []

    while degrees >= 0:
        out.append(int(i % df))
        degrees -= 1
        i -= (i % df)
        i /= df
    
    out.reverse()
    #if y % 1000 == 0:
    #    print(y,len(out))
    #print(i, degrees, out)
    return out


def rtd(cube,movelist,i):
    
    for rtd in search(i,18+1):
    #rtd = rd.randint(1,18) #Inclus
        if rtd == 1 or rtd == 0:
            cube.u()
            movelist.append("U")
        if rtd == 2:
            cube.u_pr()
            movelist.append("U*")
        if rtd == 3:
            cube.d()
            movelist.append("D")
        if rtd == 4:
            cube.d_pr()
            movelist.append("D*")
        if rtd == 5:
            cube.r()
            movelist.append("R")
        if rtd == 6:
            cube.r_pr()
            movelist.append("R*")
        if rtd == 7:
            cube.l()
            movelist.append("L")
        if rtd == 8:
            cube.l_pr()
            movelist.append("L*")
        if rtd == 9:
            cube.f()
            movelist.append("F")
        if rtd == 10:
            cube.f_pr()
            movelist.append("F*")
        if rtd == 11:
            cube.b()
            movelist.append("B")
        if rtd == 12:
            cube.b_pr()
            movelist.append("B*")
        if rtd == 13:
            cube.u2()
            movelist.append("U2")
        if rtd == 14:
            cube.d2()
            movelist.append("D2")
        if rtd == 15:
            cube.l2()
            movelist.append("L2")
        if rtd == 16:
            cube.r2()
            movelist.append("R2")
        if rtd == 17:
            cube.f2()
            movelist.append("F2")
        if rtd == 18:
            cube.b2()
            movelist.append("B2")

def rtdold(cube,movelist):
    
    #for rtd in search(i,18+1):
    rtd = rd.randint(1,18) #Inclus
    if rtd == 1 or rtd == 0:
        cube.u()
        movelist.append("U")
    if rtd == 2:
        cube.u_pr()
        movelist.append("U*")
    if rtd == 3:
        cube.d()
        movelist.append("D")
    if rtd == 4:
        cube.d_pr()
        movelist.append("D*")
    if rtd == 5:
        cube.r()
        movelist.append("R")
    if rtd == 6:
        cube.r_pr()
        movelist.append("R*")
    if rtd == 7:
        cube.l()
        movelist.append("L")
    if rtd == 8:
        cube.l_pr()
        movelist.append("L*")
    if rtd == 9:
        cube.f()
        movelist.append("F")
    if rtd == 10:
        cube.f_pr()
        movelist.append("F*")
    if rtd == 11:
        cube.b()
        movelist.append("B")
    if rtd == 12:
        cube.b_pr()
        movelist.append("B*")
    if rtd == 13:
        cube.u2()
        movelist.append("U2")
    if rtd == 14:
        cube.d2()
        movelist.append("D2")
    if rtd == 15:
        cube.l2()
        movelist.append("L2")
    if rtd == 16:
        cube.r2()
        movelist.append("R2")
    if rtd == 17:
        cube.f2()
        movelist.append("F2")
    if rtd == 18:
        cube.b2()
        movelist.append("B2")

def rtdG1_1(cube,movelist,i):
    for rtd in search(i,10+1):
    #rtd = rd.randint(1,10) #Inclus
        if rtd == 1 or rtd == 0:
            cube.u()
            movelist.append("U")
        if rtd == 2:
            cube.u_pr()
            movelist.append("U*")
        if rtd == 3:
            cube.d()
            movelist.append("D")
        if rtd == 4:
            cube.d_pr()
            movelist.append("D*")
        if rtd == 5:
            cube.f()
            movelist.append("F")
        if rtd == 6:
            cube.f_pr()
            movelist.append("F*")
        if rtd == 7:
            cube.b()
            movelist.append("B")
        if rtd == 8:
            cube.b_pr()
            movelist.append("B*")
        if rtd == 9:
            cube.l2()
            movelist.append("L2")
        if rtd == 10:
            cube.r2()
            movelist.append("R2")

def rtdG1_1old(cube,movelist):
    rtd = rd.randint(1,10) #Inclus
    if rtd == 1 or rtd == 0:
        cube.u()
        movelist.append("U")
    if rtd == 2:
        cube.u_pr()
        movelist.append("U*")
    if rtd == 3:
        cube.d()
        movelist.append("D")
    if rtd == 4:
        cube.d_pr()
        movelist.append("D*")
    if rtd == 5:
        cube.f()
        movelist.append("F")
    if rtd == 6:
        cube.f_pr()
        movelist.append("F*")
    if rtd == 7:
        cube.b()
        movelist.append("B")
    if rtd == 8:
        cube.b_pr()
        movelist.append("B*")
    if rtd == 9:
        cube.l2()
        movelist.append("L2")
    if rtd == 10:
        cube.r2()
        movelist.append("R2")

def rtdG1_2old(cube,movelist):
    oll_test_u = []
    oll_case_u = 0

    for j in [cube.u_layer[0,0],cube.u_layer[0,2],cube.u_layer[2,0],cube.u_layer[2,2]]:
        if j == color_u or j == color_d:
            oll_test_u.append(j)
            
    oll_case_u = len(oll_test_u)
    trigg = False

    if oll_case_u == 2:
        if ((cube.b_layer[0,0] == color_u or cube.b_layer[0,0] == color_d)
        and (cube.b_layer[0,2] == color_u or cube.b_layer[0,2] == color_d)):
            #U / Superman
            trigg = True
            cube.r2().d_pr().r().u2().r_pr().d().r().u2().r()
            movelist.extend(["R2", "D*", "R", "U2", "R*", "D", "R", "U2", "R"])
        
        elif ((cube.l_layer[0,0] == color_u or cube.l_layer[0,0] == color_d)
        and (cube.r_layer[0,2] == color_u or cube.r_layer[0,2] == color_d)):
            	#T
            trigg = True
            cube.r_pr().f_pr().r().b_pr().r_pr().f().r().b()
            movelist.extend(["R*", "F*", "R", "B*", "R*", "F", "R", "B"])
        
        elif ((cube.r_layer[0,0] == color_u or cube.r_layer[0,0] == color_d)
        and (cube.b_layer[0,2] == color_u or cube.b_layer[0,2] == color_d)):
            	#L
            trigg = True
            cube.r().b_pr().r_pr().f().r().b().r_pr().f_pr()
            movelist.extend(["R", "B*", "R*", "F", "R", "B", "R*", "F*"])
        
    elif oll_case_u == 1:
        if ((cube.b_layer[0,2] == color_u or cube.b_layer[0,2] == color_d)
        and (cube.l_layer[0,2] == color_u or cube.l_layer[0,2] == color_d)
        and (cube.f_layer[0,2] == color_u or cube.f_layer[0,2] == color_d)):
            #Sune
            trigg = True
            cube.r().u_pr().l_pr().u().r_pr().u_pr().l().u()
            movelist.extend(["R", "U*", "L*", "U", "R*", "U*", "L", "U"])
        
        elif ((cube.b_layer[0,0] == color_u or cube.b_layer[0,0] == color_d)
        and (cube.l_layer[0,0] == color_u or cube.l_layer[0,0] == color_d)
        and (cube.r_layer[0,0] == color_u or cube.r_layer[0,0] == color_d)):
            	#A-Sune
            trigg = True
            cube.u_pr().l_pr().u().r().u_pr().l().u().r_pr()
            movelist.extend(["U*", "L*", "U", "R", "U*", "L", "U", "R*"])
        
    elif oll_case_u == 0:
        if ((cube.f_layer[0,0] == color_u or cube.f_layer[0,0] == color_d)
        and (cube.f_layer[0,2] == color_u or cube.f_layer[0,2] == color_d)
        and (cube.b_layer[0,0] == color_u or cube.b_layer[0,0] == color_d)
        and (cube.b_layer[0,2] == color_u or cube.b_layer[0,2] == color_d)):
            #H
            trigg = True
            cube.r_pr().f2().r2().u2().r_pr().f2().r().u2().r2().f2().r().u2()
            movelist.extend(["R*", "F2", "R2", "U2", "R*", "F2", "R", "U2", "R2", "F2", "R", "U2"])
        
        elif ((cube.f_layer[0,0] == color_u or cube.f_layer[0,0] == color_d)
        and (cube.f_layer[0,2] == color_u or cube.f_layer[0,2] == color_d)
        and (cube.l_layer[0,0] == color_u or cube.l_layer[0,0] == color_d)
        and (cube.r_layer[0,2] == color_u or cube.r_layer[0,2] == color_d)):
            	#pi
            trigg = True
            cube.r().f_pr().d2().f().r_pr().u_pr().r().f_pr().d2().f().r_pr().u()
            movelist.extend(["R", "F*", "D2", "F", "R*", "U*", "R", "F*", "D2", "F", "R*", "U"])
           
    elif oll_case_u == 4:
        trigg = True
        cube.f2().r2().b2().l2()
        movelist.extend(["F2", "R2", "B2", "L2"])
    
    if trigg == False:
        rtdG1_1old(cube,movelist)
        

def rtdG2(cube,movelist,i):
    for rtd in search(i,8+1):
    #rtd = rd.randint(1,8) #Inclus
        if rtd == 1 or rtd == 0:
            cube.u()
            movelist.append("U")
        if rtd == 2:
            cube.u_pr()
            movelist.append("U*")
        if rtd == 3:
            cube.d()
            movelist.append("D")
        if rtd == 4:
            cube.d_pr()
            movelist.append("D*")
        if rtd == 5:
            cube.f2()
            movelist.append("F2")
        if rtd == 6:
            cube.b2()
            movelist.append("B2")
        if rtd == 7:
            cube.l2()
            movelist.append("L2")
        if rtd == 8:
            cube.r2()
            movelist.append("R2")

def rtdG2old(cube,movelist):
    global switch
    rtd = rd.randint(1,10)
    while rtd == switch:
        rtd = rd.randint(1,10)
    
    if rtd == 1 or rtd == 0:
        switch = rtd
        cube.u()
        movelist.append("U")
    if rtd == 2:
        switch = rtd
        cube.u_pr()
        movelist.append("U*")
    if rtd == 3:
        switch = rtd
        cube.d()
        movelist.append("D")
    if rtd == 4:
        switch = rtd
        cube.d_pr()
        movelist.append("D*")
    if rtd == 5:
        switch = rtd
        cube.f2()
        movelist.append("F2")
    if rtd == 6:
        switch = rtd
        cube.b2()
        movelist.append("B2")
    if rtd == 7:
        switch = rtd
        cube.l2()
        movelist.append("L2")
    if rtd == 8:
        switch = rtd
        cube.r2()
        movelist.append("R2")
    if rtd == 9:
        switch = rtd
        cube.u2()
        movelist.append("U2")
    if rtd == 10:
        switch = rtd
        cube.d2()
        movelist.append("D2")

def rtdG3(cube,movelist,i):
    for rtd in search(i,6+1):
    #rtd = rd.randint(1,6) #Inclus
        if rtd == 1 or rtd == 0:
            cube.u2()
            movelist.append("U2")
        if rtd == 2:
            cube.d2()
            movelist.append("D2")
        if rtd == 3:
            cube.f2()
            movelist.append("F2")
        if rtd == 4:
            cube.b2()
            movelist.append("B2")
        if rtd == 5:
            cube.l2()
            movelist.append("L2")
        if rtd == 6:
            cube.r2()
            movelist.append("R2")       

def rtdG3old(cube,movelist):
    global switch
    rtd = rd.randint(1,6)
    while rtd == switch:
        rtd = rd.randint(1,6)
    if rtd == 1 or rtd == 0:
        switch = rtd
        cube.u2()
        movelist.append("U2")
    if rtd == 2:
        switch = rtd
        cube.d2()
        movelist.append("D2")
    if rtd == 3:
        switch = rtd
        cube.f2()
        movelist.append("F2")
    if rtd == 4:
        switch = rtd
        cube.b2()
        movelist.append("B2")
    if rtd == 5:
        switch = rtd
        cube.l2()
        movelist.append("L2")
    if rtd == 6:
        switch = rtd
        cube.r2()
        movelist.append("R2")  
