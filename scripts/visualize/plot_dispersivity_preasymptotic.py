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

def plot_random_alphaL_preasymptotic(
        x_random,
        alpha_random,
        x_select = False,
        alpha_select = False,
        figsize=[3.75,2.8],
        color_points = 'k',
        ms = 30,
        xscale = 'log',
        yscale = 'log',
        xlim = [4,330],
        ylim = [0.1,20],
        xlabel = r'Plume travel distance $x$ [m]',
        ylabel = r'Preasymptoptic $\alpha_L(x)$ [m]',
        textsize = 8,
        grid = False,
        save_fig = None,
        ):
    
    fig = plt.figure(figsize=figsize)
    plt.scatter(x_random[:,:],alpha_random[:,:],color = color_points,s = ms)
    for i in range(alpha_select.shape[0]):
        plt.scatter(x_select[i,:],alpha_select[i,:],s = 1.25*ms,edgecolor = 'k')

   # plt.legend(loc=loc,
   #            fontsize=textsize,
   #            facecolor='oldlace',
   #            shadow = True)

    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlim(xlim)
    plt.ylim(ylim) 
    plt.xlabel(xlabel,fontsize=textsize)    
    plt.ylabel(ylabel,fontsize=textsize)    
    plt.tick_params(axis="both",which="major",labelsize=textsize)
    plt.grid(grid)
    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print('Save figure to {}'.format(save_fig))
    
    return fig

