#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 08:21:15 2019

@author: vpfernandez
"""
import math
import numpy as np

#def rtd_cross(cube,movelist):
#    rtd = rd.randint(1,7) #Inclus
#    if rtd == 1:
#        cube.u()
#        movelist.append("U")
#    if rtd == 2:
#        cube.u_pr()
#        movelist.append("U*")
#    if rtd == 3:
#        cube.u().u()
#        movelist.append("U2")
#    if rtd == 4 and cube.r_layer[2,1] != color_r:
#        cube.r().r()
#        movelist.append("R2")
#    if rtd == 5 and cube.l_layer[2,1] != color_l:
#        cube.l().l()
#        movelist.append("L2")
#    if rtd == 6 and cube.f_layer[2,1] != color_f:
#        cube.f().f()
#        movelist.append("F2")
#    if rtd == 7 and cube.b_layer[2,1] != color_b:
#        cube.b().b()
#        movelist.append("B2")
#
#def rtd_face(cube,movelist):
#    rtd = rd.randint(1,11) #Inclus
#    if rtd == 1:
#        cube.u()
#        movelist.append("U")
#    if rtd == 2:
#        cube.u_pr()
#        movelist.append("U* ")
#    if rtd == 3:
#        cube.r()
#        movelist.append("R")
#    if rtd == 4:
#        cube.r_pr()
#        movelist.append("R* ")
#    if rtd == 5:
#        cube.l()
#        movelist.append("L")
#    if rtd == 6:
#        cube.l_pr()
#        movelist.append("L* ")
#    if rtd == 7:
#        cube.f()
#        movelist.append("F")
#    if rtd == 8:
#        cube.f_pr()
#        movelist.append("F* ")
#    if rtd == 9:
#        cube.b()
#        movelist.append("B")
#    if rtd == 10:
#        cube.b_pr()
#        movelist.append("B* ")
#    if rtd == 11:
#        cube.u().u()
#        movelist.append("U2")
#
#def rtd_face2(cube,movelist):
#    rtd = rd.randint(1,9) #Inclus
#    if rtd == 1:
#        cube.u()
#        movelist.append("U")
#    if rtd == 2:
#        cube.u_pr()
#        movelist.append("U* ")
#    if rtd == 3:
#        cube.r()
#        movelist.append("R")
#    if rtd == 4:
#        cube.r_pr()
#        movelist.append("R* ")
#    if rtd == 5:
#        cube.l()
#        movelist.append("L")
#    if rtd == 6:
#        cube.l_pr()
#        movelist.append("L* ")
#    if rtd == 7:
#        cube.f()
#        movelist.append("F")
#    if rtd == 8:
#        cube.f_pr()
#        movelist.append("F* ")
#    if rtd == 9:
#        cube.u().u()
#        movelist.append("U2")
#
#def rtdOLL(cube,moveist):
#    if (cube.u_layer[1,0] == color_u and 
#            cube.u_layer[1,2] == color_u):
#            cube.f().r().u().r_pr().u_pr().f_pr()
#            movelist.extend(["F","R","U","R* ","U* ","F* "])
#            
#    elif (cube.u_layer[0,1] == color_u and 
#        cube.u_layer[1,0] == color_u) or (
#        cube.u_layer[0,1] != color_u and 
#        cube.u_layer[1,0] != color_d and 
#        cube.u_layer[1,2] != color_u and 
#        cube.u_layer[2,1] != color_u):
#        cube.f().r().u().r_pr().u_pr().r().u().r_pr().u_pr().f_pr()
#        movelist.extend(["F","R","U","R* ","U* ","R","U","R* ","U* ","F* "])
#            
#    else:
#        cube.u()
#        movelist.extend(["U"])




"""
"""
#
#def cross(cube):
#    if (cube.d_layer[0,1] == color_d 
#    and cube.d_layer[1,0] == color_d 
#    and cube.d_layer[1,2] == color_d 
#    and cube.d_layer[2,1] == color_d):
#        return True
#    else:
#        return False
#
#def cross_fix(cube):
#    if (cross(cube) == True and 
#        cube.f_layer[2,1] == color_f and 
#        cube.l_layer[2,1] == color_l and 
#        cube.r_layer[2,1] == color_r and 
#        cube.b_layer[2,1] == color_b):
#        return True
#    else:
#        return False
#
#def F2L1(cube): #Back Right
#    if (cross_fix(cube) == True and
#        cube.d_layer[2,2] == color_d and
#        cube.r_layer[2,2] == color_r and
#        cube.b_layer[2,0] == color_b and
#        cube.r_layer[1,2] == color_r and
#        cube.b_layer[1,0] == color_b):
#        return True
#    else:
#        return False  
#
#def F2L2(cube): #Back left
#    if (F2L1(cube) == True and 
#        cube.d_layer[2,0] == color_d and
#        cube.l_layer[2,0] == color_l and
#        cube.b_layer[2,2] == color_b and
#        cube.l_layer[1,0] == color_l and
#        cube.b_layer[1,2] == color_b):
#        return True
#    else:
#        return False
#
#def F2L3(cube): #Front Left
#    if (F2L2(cube) == True and 
#        cube.d_layer[0,0] == color_d and
#        cube.l_layer[2,2] == color_l and
#        cube.f_layer[2,0] == color_f and
#        cube.l_layer[1,2] == color_l and
#        cube.f_layer[1,0] == color_f):
#        return True
#    else:
#        return False
#
#def F2L4(cube): #Front Right
#    if (F2L3(cube) == True and 
#        cube.d_layer[0,2] == color_d and
#        cube.r_layer[2,0] == color_r and
#        cube.f_layer[2,2] == color_f and
#        cube.r_layer[1,0] == color_r and
#        cube.f_layer[1,2] == color_f):
#        return True
#    else:
#        return False     
#        
#    
#def OLL1(cube):
#    if F2L4(cube) == True:
#        if (cube.u_layer[0,1] == color_u and 
#            cube.u_layer[1,0] == color_u and 
#            cube.u_layer[1,2] == color_u and 
#            cube.u_layer[2,1] == color_u):
#            return True
#        else:
#            return False
#        
#    else:
#        return False    
#


"""
"""



#
#
#
##### Phase 1: White cross 
#
#save = dc(rubix)
#while cross(rubix) == False:
#    rtd(rubix,movelist_temp)
#    if len(movelist_temp) > 8:
#        rubix = dc(save) # Quickload
#        movelist_temp = [] #Clear
#step("White Cross")
#
##### Phase 2: White fix
#
#save = dc(rubix)
#movelist_temp = []
#while cross_fix(rubix) == False:#and:
#    rtd_cross(rubix,movelist_temp)
#    if len(movelist_temp) > 11:
#        rubix = dc(save) # Quickload
#        movelist_temp = [] #Clear
#step("White Fix")
#
##### Phase 3: White Full
##F2L 1
#save = dc(rubix)
#movelist_temp = []
#while F2L1(rubix) == False:
#    rtd_face(rubix,movelist_temp)
#    if len(movelist_temp) > 13:
#        rubix = dc(save) # Quickload
#        movelist_temp = [] #Clear
#step("F2L 1 (B/R)")
#
##F2L 2
#save = dc(rubix)
#movelist_temp = []
#while F2L2(rubix) == False:
#    rtd_face(rubix,movelist_temp)
#    if len(movelist_temp) > 11:
#        rubix = dc(save) # Quicksave
#        movelist_temp = [] #Clear
#step("F2L 2 (B/L)")
#
##F2L 3
#save = dc(rubix)
#movelist_temp = []
#while F2L3(rubix) == False:
#    rtd_face2(rubix,movelist_temp)
#    if len(movelist_temp) > 11:
#        rubix = dc(save) # Quicksave
#        movelist_temp = [] #Clear
#step("F2L 3 (F/L)")
#
##F2L 4
#save = dc(rubix)
#movelist_temp = []
#while F2L4(rubix) == False:
#    rtd_face2(rubix,movelist_temp)
#    if len(movelist_temp) > 9:
#        rubix = dc(save) # Quicksave
#        movelist_temp = [] #Clear
#step("F2L 4 (F/R)")
#
#
##OLL 1
#save = dc(rubix)
#movelist_temp = []
#while OLL1(rubix) == False:
#    rtdOLL(rubix,movelist_temp)
#step("OLL 1")
#


def logn(x,base):
    try:
        return math.log(x)/math.log(base)
    except:
        return 0

def search(i,df):
    
    i = int(i)
    y = i
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
    print(i, degrees, out)
    return out



for i in range(100):
    search(i,7)