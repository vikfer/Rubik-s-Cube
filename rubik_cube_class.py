# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:36:05 2019

@author: victo_000
"""

import numpy as np
from rubik_qol import sequencetoreadeable,readeabletosequence,invertsequence,dc

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
        
    def no(self):
        return self

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
    
    def move(self,sequence=[]):
        
        moves = {0:self.no,
                 1:self.r,    
                 2:self.r_pr,    
                 3:self.l,    
                 4:self.l_pr,    
                 
                 5:self.f,
                 6:self.f_pr,
                 7:self.b,
                 8:self.b_pr,
                 
                 9:self.u,    
                 10:self.u_pr,    
                 11:self.d,    
                 12:self.d_pr, 
                 
                 13:self.u2,
                 14:self.d2,
                 15:self.l2,
                 16:self.r2,
                 17:self.f2,
                 18:self.b2,
                 }
        
        for i in sequence:
            moves[i]()
        
        return self

    
    def scramble(self,n,movelist):
        
        sequence = np.random.choice(np.arange(1,18+1,1),n)
        self.move(sequence)
        movelist.extend(sequence)

        
        print(self)
        print()
        print("Scramble: {}".format(sequencetoreadeable(movelist)))
        print()
        print("Solve: {}".format(sequencetoreadeable(invertsequence(movelist))))
    
    def unittest(self):
        
        if (self.move([1]) == self.r() and
            self.move([2]) ==self.r_pr() and
            self.move([3]) ==self.l() and
            self.move([4]) ==self.l_pr() and
            
            self.move([5]) ==self.f() and
            self.move([6]) ==self.f_pr() and
            self.move([7]) ==self.b() and
            self.move([8]) ==self.b_pr() and
            
            self.move([9]) ==self.u() and
            self.move([10]) ==self.u_pr() and 
            self.move([11]) ==self.d() and
            self.move([12]) ==self.d_pr() and
            
            self.move([13]) ==self.u2() and
            self.move([14]) ==self.d2() and
            self.move([15]) ==self.l2() and
            self.move([16]) ==self.r2() and
            self.move([17]) ==self.f2() and
            self.move([18]) ==self.b2()):
            pass
        
        else:
            
            raise Exception("Unit test Failed")
    
    def __eq__(self,other):
        
        condi = True
        
        selflayers = [self.u_layer,
                self.f_layer,
                self.l_layer,
                self.b_layer,
                self.r_layer,
                self.d_layer,]
        
        otherlayers = [other.u_layer,
                other.f_layer,
                other.l_layer,
                other.b_layer,
                other.r_layer,
                other.d_layer,]
        
        for i in range(len(selflayers)):
            if False in (selflayers[i] == otherlayers[i]):
                condi = False
        
        return condi
        
    
    def __str__(self):
        names = ["U layer",
                "F layer",
                "L layer",
                "B layer",
                "R layer",
                "D layer",]
        
        layers = [self.u_layer,
                self.f_layer,
                self.l_layer,
                self.b_layer,
                self.r_layer,
                self.d_layer,]
        
        for i in range(len(layers)):
            print(names[i])
            print(layers[i])
            print()
        
        return ""
            
        

