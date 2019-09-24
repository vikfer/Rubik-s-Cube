# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:15:36 2019

@author: victo_000
"""

from rubik_cube_class import cube as cube_class
cube = cube_class()

color_u = cube.u_layer[1,1] #Color 
color_f = cube.f_layer[1,1] #Color 
color_l = cube.l_layer[1,1] #Color 
color_b = cube.b_layer[1,1] #Color 
color_r = cube.r_layer[1,1] #Color 
color_d = cube.d_layer[1,1] #Color 

def G0(cube):
    if (
        cube.f_layer[0,1] != color_u and cube.f_layer[0,1] != color_d and 
        cube.f_layer[1,0] != color_u and cube.f_layer[1,0] != color_d and 
        cube.f_layer[1,2] != color_u and cube.f_layer[1,2] != color_d and 
        cube.f_layer[2,1] != color_u and cube.f_layer[2,1] != color_d and 
        
        cube.b_layer[0,1] != color_u and cube.b_layer[0,1] != color_d and 
        cube.b_layer[1,0] != color_u and cube.b_layer[1,0] != color_d and 
        cube.b_layer[1,2] != color_u and cube.b_layer[1,2] != color_d and 
        cube.b_layer[2,1] != color_u and cube.b_layer[2,1] != color_d and 
        
        cube.u_layer[0,1] != color_f and cube.u_layer[0,1] != color_b and 
        cube.u_layer[1,0] != color_f and cube.u_layer[1,0] != color_b and 
        cube.u_layer[1,2] != color_f and cube.u_layer[1,2] != color_b and 
        cube.u_layer[2,1] != color_f and cube.u_layer[2,1] != color_b and 
        
        cube.d_layer[0,1] != color_f and cube.d_layer[0,1] != color_b and 
        cube.d_layer[1,0] != color_f and cube.d_layer[1,0] != color_b and 
        cube.d_layer[1,2] != color_f and cube.d_layer[1,2] != color_b and 
        cube.d_layer[2,1] != color_f and cube.d_layer[2,1] != color_b and
        
        cube.l_layer[0,1] != color_u and cube.l_layer[0,1] != color_d and         
        cube.l_layer[2,1] != color_u and cube.l_layer[2,1] != color_d and
        cube.r_layer[0,1] != color_u and cube.r_layer[0,1] != color_d and         
        cube.r_layer[2,1] != color_u and cube.r_layer[2,1] != color_d and
        
        cube.r_layer[1,0] != color_f and cube.r_layer[1,0] != color_b and 
        cube.r_layer[1,2] != color_f and cube.r_layer[1,2] != color_b and 
        cube.l_layer[1,0] != color_f and cube.l_layer[1,0] != color_b and 
        cube.l_layer[1,2] != color_f and cube.l_layer[1,2] != color_b):
        return True
    else:
        return False

def G1_1(cube):
    if (G0(cube) == True and
        
        (cube.u_layer[0,1] == color_u or cube.u_layer[0,1] == color_d) and 
        (cube.u_layer[1,0] == color_u or cube.u_layer[1,0] == color_d) and 
        (cube.u_layer[1,2] == color_u or cube.u_layer[1,2] == color_d) and 
        (cube.u_layer[2,1] == color_u or cube.u_layer[2,1] == color_d) and 
        
        (cube.d_layer[0,1] == color_u or cube.d_layer[0,1] == color_d) and 
        (cube.d_layer[1,0] == color_u or cube.d_layer[1,0] == color_d) and 
        (cube.d_layer[1,2] == color_u or cube.d_layer[1,2] == color_d) and 
        (cube.d_layer[2,1] == color_u or cube.d_layer[2,1] == color_d)):
        return True
    else:
        return False

def G1_2(cube):
    up = []
    down = []
    test = 0
    for i in cube.u_layer:
        for j in i:
            up.append(j)
    for i in cube.d_layer:
        for j in i:
            down.append(j)
    
    colors = [color_f,color_b,color_l,color_r]
    for i in colors:
        if ((i in up) or (i in down)):
            test += 1
    if test != 0:
        return False
    else:
        return True

def G2_1(cube):
    if (G1_2(cube) == True and
        cube.u_layer[0,0] == color_u and cube.u_layer[0,2] == color_u and
        cube.u_layer[2,0] == color_u and cube.u_layer[2,2] == color_u):
        return True
    else:
        return False

def G2_2(cube):
    if (G2_1(cube) == True and
        cube.f_layer[0,0] == cube.f_layer[0,2] and
        cube.f_layer[2,0] == cube.f_layer[2,2] and
        cube.l_layer[0,0] == cube.l_layer[0,2] and
        cube.l_layer[2,0] == cube.l_layer[2,2] and
        cube.r_layer[0,0] == cube.r_layer[0,2] and
        cube.r_layer[2,0] == cube.r_layer[2,2] and
        cube.b_layer[0,0] == cube.b_layer[0,2] and
        cube.b_layer[2,0] == cube.b_layer[2,2]):
        return True
    else:
        return False

def G2_3(cube):
    if (G2_2(cube) == True and
        cube.f_layer[0,0] == cube.f_layer[1,1] and cube.f_layer[2,2] == cube.f_layer[1,1] and
        cube.b_layer[0,0] == cube.b_layer[1,1] and cube.b_layer[2,2] == cube.b_layer[1,1] and 
        cube.l_layer[0,0] == cube.l_layer[1,1] and cube.l_layer[2,2] == cube.l_layer[1,1] and 
        cube.r_layer[0,0] == cube.r_layer[1,1] and cube.r_layer[2,2] == cube.r_layer[1,1] and
        cube.u_layer[0,0] == cube.u_layer[1,1] and cube.u_layer[2,2] == cube.u_layer[1,1] and
        cube.d_layer[0,0] == cube.d_layer[1,1] and cube.d_layer[2,2] == cube.d_layer[1,1]):
        return True
    else:
        return False        

def G2(cube):
    left = []
    right = []
    front = []
    back = []
    test = 0
    for i in cube.l_layer:
        for j in i:
            left.append(j)
    for i in cube.d_layer:
        for j in i:
            right.append(j)
    for i in cube.f_layer:
        for j in i:
            front.append(j)
    for i in cube.b_layer:
        for j in i:
            back.append(j)
    
    colors = [color_f,color_b]
    for i in colors:
        if ((i in left) or (i in right)):
            test += 1
    colors = [color_l,color_r]
    for i in colors:
        if ((i in front) or (i in back)):
            test += 1

    if test != 0 or G2_3(cube) == False:
        return False
    else:
        return True

def test(face):
    liste = []
    for i in face:
        x = i
        for x in i:
            liste.append(x)
            
    str1 = ''.join(liste)
    return len(set(str1))==1
   
def fullcheck(cube):
    if cube == cube_class():
        return True
    else:
        return False
#    liste = [cube.u_layer,cube.f_layer,cube.l_layer,cube.b_layer,cube.r_layer,cube.d_layer]
#    final = []
#    for i in liste:
#        final.append(test(i))
#    if False in final:
#        return False
#    else:
#        return True
