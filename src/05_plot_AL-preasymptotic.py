#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:50:21 2022

@author: zech0001
"""
import numpy as np
import matplotlib.pyplot as plt

def macrodispersivity_preassymptotic(sigmaY2,Ih,L,ee=1):
    
    be = anisotropy_factor(ee)
    alphaL_preasymp =  sigmaY2 * Ih * (1. - np.exp(-L/Ih * be))  
    
    return alphaL_preasymp

def anisotropy_factor(ee):

    if ee < 1 and ee > 0:
        e1 = (ee * ee - 1) ** 2
        e2 = np.sqrt(1.0 - ee * ee)
        bee = (
            1.0
            + ee * ee * (19.0 - 10 * ee * ee) / 16.0 / e1
            - ee * (13.0 - 4.0 * ee * ee) * np.arcsin(e2) / (16.0 * e2 * e1)
        )
    elif ee == 1:
        bee = 8.0 / 15.0
    elif ee == 0:
        bee = 1.0
    return bee

x = np.arange(0,10.1,0.1)

textsize = 8
plt.close('all')
plt.figure(1,figsize=[3.75,2.1])

for ie,ee in enumerate([0.1,0.5,1]):

    alpha_x = macrodispersivity_preassymptotic(sigmaY2 = 1, Ih = 1, L = x, ee = ee)
    plt.plot(x,alpha_x,lw = 2,label=r'$f  = {}$'.format(ee))

plt.legend(loc = 'lower right',fontsize=textsize)
plt.xlabel(r"Relative distance $L/I_h$",fontsize=textsize)
plt.ylabel(r"$\alpha_L/\alpha_L^{asymp}$",fontsize=textsize)
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.xlim([0,10])
plt.grid(True)
plt.tight_layout()
plt.savefig('../results/Figure_04_AL_preasymptotic.pdf')