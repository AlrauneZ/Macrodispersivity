#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 20:40:04 2025

@author: alraune
"""
import numpy as np

def data_cape_cod(file_name = './data/Cape_Cod_day_{}.csv',
                  times = [203,461], #d
                  ):

    data_cape_cod = dict()
    for i, ti in enumerate(times):    
        ### Read data values from Cape cod experiment
        data_m = np.loadtxt(file_name.format(ti),delimiter=',')   
        data_cape_cod[ti] = dict(    
            mcum_data = data_m[:,1],
            xcum_data = data_m[:,0],
            )

    return data_cape_cod

def settings_cape_cod(
                  v = 0.42, #m/d    
                  alphaL_mean = 1.1, #m
                  alphaL_std = 1.1, #m              
                  ):

    settings_cape_cod = dict(
        v = v, #m/d    
        alphaL_mean = alphaL_mean, #m
        alphaL_std = alphaL_std, #m        
        )

    return settings_cape_cod
