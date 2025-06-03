#!/usr/bin/env python3
"""Created on Fri Mar 14 16:30:22 2025

@author: alraune
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

sys.path.append("/home/alraune/GitHub/AlrauneZ/Macrodispersivity/")

from scripts.analysis.statistics import cdf
from scripts.analysis.statistics import macrodispersivity_statistics


def plot_alphaL_cfd(data_het_classes,
                    figsize=[5.4,3.2],
                    marker = "o",
                    msize = 7,
                    mec = "k",
                    colors = ["C1","C2","C4"],
                    lw=4,
                    xlim = [0,13],
                    ylim = [0,1],
                    xlabel = r"Longitudinal dispersivity $\alpha_L$ [m]",
                    ylabel = "cumulative density",
                    grid = True,
                    textsize = 12,
                    save_fig = None,
                    ):

                    # label_R1 = 'high reliablity',
                    # label_R2 = 'moderate reliablity',

    ### Plotting
    fig = plt.figure(figsize=figsize)

    macrodispersivity_statistics(data_het_classes,verbose = False)

    for index, (key, value) in enumerate(data_het_classes.items()):

        aL_het = value["aL_het"]
        plt.plot(np.sort(aL_het),
                 np.linspace(0,1,len(aL_het)+2)[1:-1],
                 marker = marker,
                 mec = mec,
                 ms=msize,
                 ls="",
                 c=colors[index],
                 zorder = 3,
                 label=f"data, level {key}  ",
                 )


    alpha_range = np.arange(0.001,13,0.1)
    for index, (key, value) in enumerate(data_het_classes.items()):
        lognorm_cdf = cdf(alpha_range,value["log_meanw"],value["log_varw"])
        plt.plot(alpha_range,
                 lognorm_cdf,
                 c=colors[index],
                 lw=lw,
                 zorder = 2,
                 label="CDF",
                 )

    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.legend(loc="lower right",
               fontsize=textsize,
               ncol=2,
               facecolor="oldlace",
               shadow = True)
    plt.xlabel(xlabel,fontsize=textsize)
    plt.ylabel(ylabel,fontsize=textsize)
    plt.tick_params(axis="both",which="major",labelsize=textsize)
    plt.grid(grid)
    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print(f"Save figure to {save_fig}")

    return fig
