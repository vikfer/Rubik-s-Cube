# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:48:25 2019

@author: victo_000
"""
"Various QoL Improvements"

import os
import copy
import time
import numpy as np
import math

try:
    from win10toast import ToastNotifier
except ModuleNotFoundError:
    pass


def notify(title, text, **kwargs):    
    
    sound=kwargs.get('sound', None)
    subtitle=kwargs.get('subtitle', None)
    duration=kwargs.get('duration', 5)
    
    if os.name == 'posix':
        if subtitle != None:
            os.system("""
                      osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "{}"'
                      """.format(text, title, subtitle, sound))
        else:
           os.system("""
                      osascript -e 'display notification "{}" with title "{}" sound name "{}"'
                      """.format(text, title, subtitle, sound))
            
    if os.name == 'nt':
        toaster = ToastNotifier()
        if subtitle != None:    
            toaster.show_toast(title,"{} - {}".format(subtitle,text),duration=duration)
        else:
            toaster.show_toast(title,"{}".format(text),duration=duration)
        while toaster.notification_active(): 
            time.sleep(0)


def clear():
    if os.name == 'nt': 
        os.system('cls') 
    else: 
        os.system('clear') 

def nl(n=1):
    for i in range(n):
        print('')

def dc(x):
    return copy.deepcopy(x)


def pause():
    test = input('Proceed ? Y/N: ')
    if 'y' in test or 'Y' in test:
        print('Proceeding')
    else:
        raise KeyboardInterrupt('Program Stopped')

def logn(x,base):
    try:
        return math.log(x)/math.log(base)
    except ValueError:
        return 0  

def average(*args):
    liste=[]
    for arg in args:
        if type(arg) == list or type(arg) == np.ndarray:
            for i in arg:
                liste.append(i)
        else:
            liste.append(arg)
        
    if type(liste) == list:        
        return sum(liste)/len(liste)
    else:
        raise TypeError

if __name__ == '__main__': ### ONLY executes when run directly (ie. NOT imported)
    #notify("Test", "Heres an alert", subtitle="jpp")
    print("")
    