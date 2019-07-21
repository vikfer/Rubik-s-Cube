# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:36:05 2019

@author: victo_000
"""

import numpy as np
import random as rd
from rubik_qol import nl, dc

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

