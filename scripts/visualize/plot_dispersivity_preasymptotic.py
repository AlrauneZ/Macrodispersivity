#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 22:13:20 2025

@author: alraune
"""
# import numpy as np
import matplotlib.pyplot as plt

def plot_alphaL_preasymptotic(sets_aL,
                              figsize=[3.75,2.1],
                              lw = 2,
                              xlim = [0,10],
                              xlabel = r"Distance $L$",
                              ylabel = r"Dispersivity $\alpha_L$",
                              loc = 'lower right',
                              grid = True,
                              textsize = 8,
                              save_fig = None,
                              ):
    fig = plt.figure(figsize=figsize)

    for key, value in sets_aL.items():
    
        plt.plot(value['x'],value['alphaL'],lw = lw,label=r'$f  = {}$'.format(value['ee']))
   

    plt.xlim(xlim)
    # plt.ylim(ylim)
    plt.legend(loc=loc,
               fontsize=textsize,
               facecolor='oldlace',
               shadow = True)
    plt.xlabel(xlabel,fontsize=textsize)    
    plt.ylabel(ylabel,fontsize=textsize)    
    plt.tick_params(axis="both",which="major",labelsize=textsize)
    plt.grid(grid)
    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print('Save figure to {}'.format(save_fig))
    
    return fig

