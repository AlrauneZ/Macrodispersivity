#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 19:33:50 2025

@author: alraune
"""

import numpy as np
import matplotlib.pyplot as plt

def plot_cape_cod_example(data_cape_cod,                          
                          figsize=[7.5,2.7],
                          color_mass = 'C3',
                          color_percentiles = 'C0',
                          color_data = 'k',
                          marker_data = 'o',
                          msize = 4, 
                          lw=2,
                          xlim =[0,300],
                          ylim1 = [0,0.06],
                          ylim2 = [0,1],
                          alpha = 0.5,
                          xlabel = r'Distance $x$ [m]',
                          ylabel1 = 'Mass distribution',
                          ylabel2 = 'Cumulative mass',
                          legend_percentiles = '10-90 percentile',
                          legend_median = 'median',
                          legend_data = 'data',
                          grid = True,
                          textsize = 12,
                          save_fig = None,
                          ):

    ### Plotting
    fig = plt.figure(figsize=figsize)
    ax1=plt.subplot(121)  
    ax2=plt.subplot(122)

    for index, (ti, data_ti) in enumerate(data_cape_cod.items()):
    
        ax1.plot(data_ti['x'],data_ti['m_median'],
                 color=color_mass,
                 lw=lw,
                 zorder=2,
                 )

        ax1.fill_between(data_ti['x'],data_ti['m_10p'],data_ti['m_90p'],
                         color=color_percentiles,
                         zorder=1,
                         alpha = alpha,
                         )
        iano = np.argmax(data_ti['m_median'])

        ax1.annotate('{} days'.format(ti),
                     xy = (data_ti['x'][iano+5],data_ti['m_median'][iano+5]),
                     xytext = (1.2*data_ti['x'][iano+5],1.2*data_ti['m_median'][iano+5]),
                     arrowprops = dict(arrowstyle='->')
                     )
        ax2.plot(data_ti['xcum_data'],data_ti['mcum_data'],
                marker = marker_data,
                color = color_data,
                ls = '',
                ms=msize,
                zorder=3
                )

        ax2.plot(data_ti['x'],data_ti['mcum_median'],
                 color=color_mass,
                 lw=lw,
                 zorder=2)

        ax2.fill_between(data_ti['x'],data_ti['mcum_10p'],data_ti['mcum_90p'],
                         color=color_percentiles,
                         zorder=1,
                         alpha = alpha,
                         )

 
        ax2.annotate('{} days'.format(ti),
                     xy = (data_ti['x'][iano],data_ti['mcum_median'][iano]),
                     xytext = (1.2*data_ti['x'][iano],1.2*data_ti['mcum_median'][iano]),
                     arrowprops = dict(arrowstyle='->')
                     )

        # ax2.annotate('{} days'.format(t1),xy = (85,0.5),xytext = (105,0.62),arrowprops = dict(arrowstyle='->'))
        # ax2.annotate('{} days'.format(t2),xy = (195,0.5),xytext = (215,0.62),arrowprops = dict(arrowstyle='->'))
            
    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim1)
    ax1.set_xlabel(xlabel,fontsize=textsize)    
    ax1.set_ylabel(ylabel1,fontsize=textsize)   
    ax1.tick_params(axis="both",which="major",labelsize=textsize)
    ax1.grid(grid)

    ax2.set_xlim(xlim)
    ax2.set_ylim(ylim2)
    ax2.set_xlabel(xlabel,fontsize=textsize)    
    ax2.set_ylabel(ylabel2,fontsize=textsize)    
    ax2.tick_params(axis="both",which="major",labelsize=textsize)
    ax2.grid(grid)


    ax1.legend([legend_median,legend_percentiles],
               loc = 'upper right',
               fontsize=textsize,
               facecolor='oldlace',
               framealpha = 1,
               shadow=True)
    ax2.legend([legend_data],
               loc = 'lower right',
               fontsize=textsize,
               facecolor='oldlace',
               framealpha = 1,
               shadow=True)

    ax1.text(-0.13,-0.13,'(a)', bbox=dict(facecolor='w', alpha=1,boxstyle='round'),
             fontsize=textsize, transform=ax1.transAxes)
    ax2.text(-0.13,-0.13,'(b)', bbox=dict(facecolor='w', alpha=1,boxstyle='round'),
             fontsize=textsize, transform=ax2.transAxes)

    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print('Save figure to {}'.format(save_fig))


    return fig, ax1,ax2