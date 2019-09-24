# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:41:27 2019

@author: victo_000
"""

# Rubix

import numpy as np
#import random as rd
import time
import copy

from rubik_qol import notify,sequencetoreadeable,readeabletosequence,invertsequence
from rubik_cube_class import cube
from rubik_tests import G0, G1_1, G1_2, G2_1, G2_2, G2, fullcheck

import itertools

class GetOutOfLoop( Exception ):
    pass


def dc(x):
    return copy.deepcopy(x)

def nl(x):
    return print('\n'*x)

def populate(x,y):
    y.extend(x)
    x = []

def step(stri):
    nl(1)
    print(stri)
    print(rubix)
    populate(movelist_temp,movelist)
    print(movelist_temp)

def register(face,n):    
    array = ["Up","Front","Left","Back","Right","Down"]
    string = input(("Veuillez Renseigner la Face {}".format(array[n])))
    if len(string) != 9:
        print("Invalid")
    else:
        for i in range(len(string)):
            face[i//3,i%3] = string[i]

def simplify(liste):
    for i in range(liste-1):
        if liste[i+1] == liste[i]:
            print("to be continued")

"""
##################################################################
############################## MAIN ##############################
##################################################################
"""


rubix = cube()
solved = dc(rubix)

#register(rubix.u_layer,0)
#register(rubix.f_layer,1)
#register(rubix.l_layer,2)
#register(rubix.b_layer,3)
#register(rubix.r_layer,4)
#register(rubix.d_layer,5)

scramble = []
rubix.scramble(5,scramble)

#rubix.move([6,14,15])
#print(rubix)
#print([6,14,15])
#print(sequencetoreadeable([6,14,15]))

"""################################ Fun part ##############################"""

init = dc(rubix) # 1st pos
save = dc(rubix) # Save

movelist = []
movelist_temp = []

layer_list = [rubix.u_layer,
              rubix.f_layer,
              rubix.l_layer,
              rubix.b_layer,
              rubix.r_layer,
              rubix.d_layer]

color_u = rubix.u_layer[1,1] #Color 
color_f = rubix.f_layer[1,1] #Color 
color_l = rubix.l_layer[1,1] #Color 
color_b = rubix.b_layer[1,1] #Color 
color_r = rubix.r_layer[1,1] #Color 
color_d = rubix.d_layer[1,1] #Color 

start = time.time()

func_list_condition = [G0,
                       G1_1,
                       G1_2,
                       G2_1,
                       G2_2,
                       G2,
                       fullcheck
                       ]

output = ["1/7: G0 -> G1 (corrected edges) (optimized)",
          "2/7: G1 -> G1* (u/d cross) (optimized)",
          "3/7: G1* -> G2 (u/d same color) (non-opti semi-manual OLL)",
          "4/7: G2 -> G2* (U corners corrected)",
          "5/7: G2* -> G2** (All corners corrected)",
          "6/7: G2** -> G3 (Bicolor state + corners)",
          "7/7: G3 -> Solved"]

movelist_limits = [10,
                   10,
                   30,
                   7,
                   12,
                   9,
                   15]

availiable = [1,
              5,
              5,
              9,
              9,
              9,
              13]

test_lenght = np.array([len(func_list_condition),
                        len(output),
                        len(movelist_limits),
                        len(availiable)])

if test_lenght.std() != 0:
    raise

for stepnum in range(len(func_list_condition)):
    
    try:
        
        save = dc(rubix)
        
        for maximum in np.arange(0,movelist_limits[stepnum]+1,1,dtype=int): #until max lenght (utile pour le repeat de la boucle en dessous)
            print(maximum)
            for sequence in itertools.product(np.arange(availiable[stepnum],18+1),repeat=maximum):
                
                    sequence = list(sequence)
                    rubix.move(sequence)
            
                    if func_list_condition[stepnum](rubix) == False:
                        
                        rubix = dc(save) 
                        nextstep = False
                    
                    else:
                        nextstep = True
            
                    if nextstep == True:
                        
                        nl(1)
                        print(output[stepnum])
                        print(rubix)
                        print(sequence)
                        print(sequencetoreadeable(sequence))
                        populate(sequence,movelist)
                        
                        test = dc(init)
                        
                        if test.move(movelist) == rubix:
                            pass
                        else:
                            raise Exception("Unit Test Fail: The cubes are not matching")
                        
                        raise GetOutOfLoop
        
        raise Exception("Maximum Reached without a solution, this shouldn't happen")
    
    except GetOutOfLoop:
        pass
    
    
    
    
#    save = dc(rubix)
#    i = 1
#    movelist_temp = []
#    
#    if stepnum == len(func_list_condition)-1:
#        while func_list_condition[stepnum](rubix,solved) == False:
#    
#            func_list_rtd[stepnum](rubix,movelist_temp)
#        
#            if len(movelist_temp) > movelist_limits[stepnum]:
#        
#                rubix = dc(save) # Quickload
#                movelist_temp = [] #Clear        
#            i += 1 
#    else:
#        while func_list_condition[stepnum](rubix) == False:
#            
#            func_list_rtd[stepnum](rubix,movelist_temp)
#
#            if len(movelist_temp) > movelist_limits[stepnum]:
#            
#                rubix = dc(save) # Quickload
#                movelist_temp = [] #Clear            
#            i += 1
#
#    step(output[stepnum])

nl(3)
print(movelist)
print(sequencetoreadeable(movelist))
print("solved in {} moves".format(len(movelist)))
end = time.time()

chrono = round(end-start,2)
minutes = int(chrono // 60)
secondes = chrono-(minutes*60)

elapsed = "Solution found in {:.0f}m {:.2f}s".format(minutes,secondes)
print(elapsed)
notify("Rubik.py", elapsed)
