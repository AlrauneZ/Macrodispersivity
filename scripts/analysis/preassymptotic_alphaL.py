#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 21:47:23 2025

@author: alraune
"""

import numpy as np

def sets_preasymptotic_alphaL(sigmaY2s = [1],
                             Ihs = [1],
                             ees = [1],
                             x = np.arange(0,10.1,0.1),                             
                            ):
    
    alpha_sets = dict()
    i = 0
    for sigmaY2 in sigmaY2s:
        for Ih in Ihs:
            for ee in ees:
                alphaL = preassymptotic_alphaL(x, sigmaY2 = sigmaY2, Ih = Ih, ee = ee)
                alpha_sets[i] = dict(
                    sigmaY2 = sigmaY2,
                    Ih = Ih,
                    ee = ee,
                    x = x,
                    alphaL = alphaL,
                    )
                i+=1
    return alpha_sets

def preassymptotic_alphaL(x,sigmaY2,Ih,ee=1):
    
    be = anisotropy_factor(ee)
    alphaL_preasymp =  sigmaY2 * Ih * (1. - np.exp(-x/Ih * be))  
    
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
