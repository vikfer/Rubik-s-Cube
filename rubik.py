# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:41:27 2019

@author: victo_000
"""

# Rubix

import numpy as np
#import random as rd
import time

from rubik_qol import nl, notify, dc
from rubik_cube_class import cube

from rubik_tests import G0, G1_1, G1_2, G2_1, G2_2, G2, fullcheck
from rubik_rtd import rtd,rtdold,rtdG1_1,rtdG1_1old,rtdG1_2old,rtdG2old,rtdG3old

def populate(x,y):
    for i in x:
        y.append(i)
    x = []

def step(stri):
    nl(3)
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

from rubik_generator import rubix

solved = dc(rubix)
scramble = []
rubix.scramble(5,scramble)

"""################################ Fun part ##############################"""

init = dc(rubix) # 1st pos
save = dc(rubix) # Save

movelist = []
movelist_temp = []

layer_list = [rubix.u_layer,rubix.f_layer,rubix.l_layer,rubix.b_layer,rubix.r_layer,rubix.d_layer]

color_u = rubix.u_layer[1,1] #Color 
color_f = rubix.f_layer[1,1] #Color 
color_l = rubix.l_layer[1,1] #Color 
color_b = rubix.b_layer[1,1] #Color 
color_r = rubix.r_layer[1,1] #Color 
color_d = rubix.d_layer[1,1] #Color 


start = time.time()


save = dc(rubix)
i = 1
movelist_temp = []
while G0(rubix) == False:
    rubix = dc(save) # Quickload
    movelist_temp = [] #Clear
    rtd(rubix,movelist_temp,i)
    i += 1
step("1/7: G0 -> G1 (corrected edges) (optimized)")

save = dc(rubix)
i = 1
movelist_temp = []
while G1_1(rubix) == False:
    rubix = dc(save)
    movelist_temp = []
    rtdG1_1(rubix,movelist_temp,i)
    i += 1
step("2/7: G1 -> G1* (u/d cross) (optimized)")

save = dc(rubix)
i = 1
movelist_temp = []
while G1_2(rubix) == False:
    rtdG1_2old(rubix,movelist_temp)
    if len(movelist_temp) > 30: #HAX double OLL, (+)Temps // (-)N°Moves
        rubix = dc(save) # Quickload
        movelist_temp = [] #Clear
step("3/7: G1* -> G2 (u/d same color) (non-opti semi-manual OLL)")

save = dc(rubix)
i = 1
switch = 0
movelist_temp = []
while G2_1(rubix) == False:
    rtdG2old(rubix,movelist_temp)
    if len(movelist_temp) > 7: #avg 3.2
        rubix = dc(save) # Quickload
        movelist_temp = [] #Clear
step("4/7: G2 -> G2* (U corners corrected)")

save = dc(rubix)
i = 1
switch = 0
movelist_temp = []
while G2_2(rubix) == False:
    rtdG2old(rubix,movelist_temp)
    if len(movelist_temp) > 12: #???
        rubix = dc(save) # Quickload
        movelist_temp = [] #Clear
step("5/7: G2* -> G2** (All corners corrected)")

save = dc(rubix)
i = 1
switch = 0
movelist_temp = []
while G2(rubix) == False:
    rtdG2old(rubix,movelist_temp)
    if len(movelist_temp) > 6*1.5: #???6
        rubix = dc(save) # Quickload
        movelist_temp = [] #Clear
step("6/7: G2** -> G3 (Bicolor state + corners)")

save = dc(rubix)
i = 1
switch = 0
movelist_temp = []
while fullcheck(rubix,solved) == False:
    rtdG3old(rubix,movelist_temp)
    if len(movelist_temp) > 15: #11 ?
        rubix = dc(save)
        movelist_temp = []
step("7/7: G3 -> Solved")

nl(5)
print(movelist)
print("solved in {} moves".format(len(movelist)))
end = time.time()

chrono = round(end-start,2)
minutes = int(chrono // 60)
secondes = chrono-(minutes*60)

elapsed = "Solution found in {} minutes, {} seconds".format(str(minutes),str(secondes))
notify("Rubik.py", elapsed)
