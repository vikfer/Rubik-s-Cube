# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:41:27 2019

@author: victo_000
"""

# Rubix

import numpy as np
import random as rd
import time

from qol import nl, notify, dc, logn

class cube:    
    def __init__(self):
        
        self.u_layer = np.chararray((3,3),unicode=True)
        self.f_layer = np.chararray((3,3),unicode=True)
        self.l_layer = np.chararray((3,3),unicode=True)
        self.b_layer = np.chararray((3,3),unicode=True)
        self.r_layer = np.chararray((3,3),unicode=True)
        self.d_layer = np.chararray((3,3),unicode=True)
        
        self.u_layer[:] = "y"
        self.f_layer[:] = "r"
        self.l_layer[:] = "b"
        self.b_layer[:] = "o"
        self.r_layer[:] = "g"
        self.d_layer[:] = "w"

    def u(self):
        temp = dc(self)
        self.u_layer = np.rot90(temp.u_layer,3)
        self.f_layer[0,:] = temp.r_layer[0,:]
        self.r_layer[0,:] = temp.b_layer[0,:]
        self.b_layer[0,:] = temp.l_layer[0,:]
        self.l_layer[0,:] = temp.f_layer[0,:]
        return self
    
    def u_pr(self):
        temp = dc(self)
        self.u_layer = np.rot90(temp.u_layer,1)
        self.f_layer[0,:] = temp.l_layer[0,:]
        self.l_layer[0,:] = temp.b_layer[0,:]
        self.b_layer[0,:] = temp.r_layer[0,:]
        self.r_layer[0,:] = temp.f_layer[0,:]
        return self
    
    def d(self):
        temp = dc(self)
        self.d_layer = np.rot90(temp.d_layer,3)
        self.f_layer[2,:] = temp.l_layer[2,:]
        self.l_layer[2,:] = temp.b_layer[2,:]
        self.b_layer[2,:] = temp.r_layer[2,:]
        self.r_layer[2,:] = temp.f_layer[2,:]
        return self
    
    def d_pr(self):
        temp = dc(self)
        self.d_layer = np.rot90(temp.d_layer,1)
        self.f_layer[2,:] = temp.r_layer[2,:]
        self.r_layer[2,:] = temp.b_layer[2,:]
        self.b_layer[2,:] = temp.l_layer[2,:]
        self.l_layer[2,:] = temp.f_layer[2,:]
        return self
    
    def r(self):
        temp = dc(self)
        self.r_layer = np.rot90(temp.r_layer,3)
        self.f_layer[:,2] = temp.d_layer[:,2]
        self.d_layer[:,2] = temp.b_layer[:,0][::-1]
        self.b_layer[:,0] = temp.u_layer[:,2][::-1]
        self.u_layer[:,2] = temp.f_layer[:,2]
        return self
    
    def r_pr(self):
        temp = dc(self)
        self.r_layer = np.rot90(temp.r_layer,1)
        self.f_layer[:,2] = temp.u_layer[:,2]
        self.u_layer[:,2] = temp.b_layer[:,0][::-1]
        self.b_layer[:,0] = temp.d_layer[:,2][::-1]
        self.d_layer[:,2] = temp.f_layer[:,2]
        return self
    
    def l(self):
        temp = dc(self)
        self.l_layer = np.rot90(temp.l_layer,3)
        self.f_layer[:,0] = temp.u_layer[:,0]
        self.u_layer[:,0] = temp.b_layer[:,2][::-1]
        self.b_layer[:,2] = temp.d_layer[:,0][::-1]
        self.d_layer[:,0] = temp.f_layer[:,0]
        return self
    
    def l_pr(self):
        temp = dc(self)
        self.l_layer = np.rot90(temp.l_layer,1)
        self.f_layer[:,0] = temp.d_layer[:,0]
        self.d_layer[:,0] = temp.b_layer[:,2][::-1]
        self.b_layer[:,2] = temp.u_layer[:,0][::-1]
        self.u_layer[:,0] = temp.f_layer[:,0]
        return self
    
    def f(self):
        temp = dc(self)
        self.f_layer = np.rot90(temp.f_layer,3)
        self.u_layer[2,:] = temp.l_layer[:,2][::-1]
        self.l_layer[:,2] = temp.d_layer[0,:]
        self.d_layer[0,:] = temp.r_layer[:,0][::-1]
        self.r_layer[:,0] = temp.u_layer[2,:]
        return self
    
    def f_pr(self):
        temp = dc(self)
        self.f_layer = np.rot90(temp.f_layer,1)
        self.u_layer[2,:] = temp.r_layer[:,0]
        self.r_layer[:,0] = temp.d_layer[0,:][::-1]
        self.d_layer[0,:] = temp.l_layer[:,2]
        self.l_layer[:,2] = temp.u_layer[2,:][::-1]
        return self
    
    def b(self):
        temp = dc(self)
        self.b_layer = np.rot90(temp.b_layer,3)
        self.u_layer[0,:] = temp.r_layer[:,2]
        self.r_layer[:,2] = temp.d_layer[2,:][::-1]
        self.d_layer[2,:] = temp.l_layer[:,0]
        self.l_layer[:,0] = temp.u_layer[0,:][::-1]
        return self
    
    def b_pr(self):
        temp = dc(self)
        self.b_layer = np.rot90(temp.b_layer,1)
        self.u_layer[0,:] = temp.l_layer[:,0][::-1]
        self.l_layer[:,0] = temp.d_layer[2,:]
        self.d_layer[2,:] = temp.r_layer[:,2][::-1]
        self.r_layer[:,2] = temp.u_layer[0,:]
        return self
    
    def u2(self):
        self.u().u()
        return self
    
    def d2(self):
        self.d().d()
        return self    
    
    def l2(self):
        self.l().l()
        return self    
    
    def r2(self):
        self.r().r()
        return self    
    
    def f2(self):
        self.f().f()
        return self    
    
    def b2(self):
        self.b().b()
        return self
    
    def scramble(self,n,movelist):
        for i in range(n):
            rtd = rd.randint(1,18) #Inclus
            if rtd == 1 or rtd == 0:
                self.u()
                movelist.append("U")
            if rtd == 2:
                self.u_pr()
                movelist.append("U*")
            if rtd == 3:
                self.d()
                movelist.append("D")
            if rtd == 4:
                self.d_pr()
                movelist.append("D*")
            if rtd == 5:
                self.r()
                movelist.append("R")
            if rtd == 6:
                self.r_pr()
                movelist.append("R*")
            if rtd == 7:
                self.l()
                movelist.append("L")
            if rtd == 8:
                self.l_pr()
                movelist.append("L*")
            if rtd == 9:
                self.f()
                movelist.append("F")
            if rtd == 10:
                self.f_pr()
                movelist.append("F*")
            if rtd == 11:
                self.b()
                movelist.append("B")
            if rtd == 12:
                self.b_pr()
                movelist.append("B*")
            if rtd == 13:
                self.u2()
                movelist.append("U2")
            if rtd == 14:
                self.d2()
                movelist.append("D2")
            if rtd == 15:
                self.f2()
                movelist.append("F2")
            if rtd == 16:
                self.b2()
                movelist.append("B2")
            if rtd == 17:
                self.l2()
                movelist.append("L2")
            if rtd == 18:
                self.r2()
                movelist.append("R2")
        print(self)
        nl()
        print("Scramble: {}".format(movelist))
        nl()
    
    def __eq__(self,other):
        return str(self.__dict__) == str(other.__dict__)
    
    def __str__(self):
        return str(self.__dict__)




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


def simplify(liste):
    for i in range(liste-1):
        if liste[i+1] == liste[i]:
            print("to be continued")


"""
##################################################################
############################## RTDs ##############################
##################################################################
"""


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

"""
##################################################################
############################## TESTS #############################
##################################################################
"""

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
   
def fullcheck(cube,solved):
    if cube == solved:
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
rubix.scramble(10,scramble)
#print(rubix)

"""
################################ Fun part ##############################
"""

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