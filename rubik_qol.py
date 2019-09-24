# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:48:25 2019

@author: victo_000
"""
"Various QoL Improvements"

import os
import math
import copy

def dc(x):
    return copy.deepcopy(x)

try:
    from plyer import notification
except ModuleNotFoundError:
    pass

def sequencetoreadeable(sequence):
    
    dicti = {0:'/',
             1:'R',    
             2:'R*',    
             3:'L',    
             4:'L*',    

             5:'F',
             6:'F*',
             7:'B',
             8:'B*',

             9:'U',    
             10:'U*',    
             11:'D',    
             12:'D*',
 
             13:'U2',
             14:'D2',
             15:'L2',
             16:'R2',
             17:'F2',
             18:'B2',
             }
    
    out = []
    
    for i in sequence:
        out.append(dicti[i])
    return out

def readeabletosequence(sequence):
    
    dicti = {'/':0,
            'R':1,
            'R*':2,
            'L':3,
            'L*':4,
            
            'F':5,
            'F*':6,
            'B':7,
            'B*':8,
            
            'U': 9,
            'U*':10,
            'D':11,
            'D*':12,
            
            'U2':13,
            'D2':14,
            'L2':15,
            'R2':16,
            'F2':17,
            'B2':18,
             }
    
    out = []
    
    for i in sequence:
        out.append(dicti[i])
    return out

def invertsequence(sequence):
    invert = {0: 0,
              
              1: 2,    
              2: 1,    
              3: 4,    
              4: 3,    
              
              5: 6,    
              6: 5,    
              7: 8,    
              8: 7,    
              
              9: 10,
              10: 9,
              11: 12,
              12: 11,
              
              13: 13,
              14: 14,
              15: 15,
              16: 16,
              17: 17,
              18: 18,
              }
    
    out = []
    
    for i in sequence:
        out.append(invert[i])
    return out[::-1]
    

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
        #toaster = ToastNotifier()
        #toaster.classAtom = ""
        if subtitle != None:    
            #toaster.show_toast(title,"{} - {}".format(subtitle,text),duration=duration)
            notification.notify(title=title,
                                message="{} - {}".format(subtitle,text),
                                timeout=duration)
        else:
            #toaster.show_toast(title,"{}".format(text),duration=duration)
            notification.notify(title=title,
                                message="{}".format(text),
                                timeout=duration)
        #while toaster.notification_active(): 
            #time.sleep(0)

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

if __name__ == '__main__': ### ONLY executes when run directly (ie. NOT imported)
    #notify("Test", "Heres an alert", subtitle="jpp")
    print("")
    