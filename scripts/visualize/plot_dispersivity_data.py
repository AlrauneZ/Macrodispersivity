import matplotlib.pyplot as plt

def plot_alphaL_vs_scale(scale_R1,
                        aL_R1,
                        scale_R2,
                        aL_R2,
                        figsize=[5.4,3.2],
                        marker_R1 = 'o',
                        marker_R2 = 'o',
                        color_R1 = 'C3',
                        color_R2 = 'C0',
                        label_R1 = 'high reliablity',
                        label_R2 = 'moderate reliablity',
                        mec = 'k',
                        msize = 60, 
                        textsize = 12,
                        save_fig = None,
                        xlabel = 'Plume travel distance $L$ [m]',
                        ylabel = r'Longitudinal dispersivity $\alpha_L$ [m]',
                        xlim = [1,1e4],
                        ylim = [9e-2,20],
                        xscale = 'log',
                        yscale = 'log', 
                        grid = True,
                        ):

    ### Plotting
    fig = plt.figure(figsize=figsize)
    plt.scatter(scale_R1,aL_R1,
                color=color_R1,
                marker=marker_R1,
                s=msize,
                edgecolor=mec,
                zorder = 11,
                label = label_R1)
    
    plt.scatter(scale_R2,aL_R2,
                color=color_R2,
                marker=marker_R2,
                s=msize,
                edgecolor=mec,
                zorder = 10,
                label=label_R2)
    
    plt.legend(loc='lower right',fontsize=textsize,facecolor='oldlace')
    plt.xlabel(xlabel,fontsize=textsize)    
    plt.ylabel(ylabel,fontsize=textsize)    
    plt.tick_params(axis="both",which="major",labelsize=textsize)
    plt.grid(grid)
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print('Save figure of longitudinal dispersivity to {}'.format(save_fig))

    return fig

def plot_aL_aquifer(
        data_aquifers,
        figsize=[5.4,3.2],
        exp_selection = [1,5,3,2,4,8],
        colors = ['C3','C0','C2','C4','gold','C1'],
        marker_R1 = 'o',
        marker_R2 = 'd',
        marker_sigmaL = '<',
        mec = 'k',
        msize = 8, 
        textsize = 12,
        ylim = [0.1,30],
        xlabel = 'Travel distance [m]',
        ylabel = r'Macrodispersivity $\alpha_L$ [m]',
        xscale = 'log',
        yscale = 'log', 
        grid = True,
        save_fig = None,
        ):
    
    fig = plt.figure(figsize=figsize)
    

    for j,i in enumerate(exp_selection): #range(1,10): #
        filter_exp = data_aquifers['Experiment'] == i
        site_name = data_aquifers['site name'].loc[filter_exp].iloc[0]
        reliability = data_aquifers['reliability'].loc[filter_exp].iloc[0]
        sigma = data_aquifers['sigma'].loc[filter_exp].iloc[0]
        ell = data_aquifers['ell'].loc[filter_exp].iloc[0]

        if reliability == 1:
            marker_type = marker_R1
        elif reliability == 2:
            marker_type = marker_R2
      
        plt.plot(data_aquifers['scale'].loc[filter_exp],
                 data_aquifers['AL'].loc[filter_exp],
                 marker = marker_type,
                 ms = msize,
                 mec = mec,
                 ls = '',
                 c = colors[j],
                 label = site_name
                 )
        
        plt.scatter(330,sigma*ell,
                    marker = marker_sigmaL,
                    s = 80,
                    edgecolors = mec,
                    color = colors[j]
                    )
        
        plt.plot([300,300],ylim,c='k',lw = 0.8)
    
    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlabel(xlabel,fontsize = textsize)
    plt.ylabel(ylabel,fontsize = textsize)
    plt.ylim(ylim)
    plt.grid(grid)

    plt.legend(ncols=2,
               fontsize = textsize,
               loc = 'upper left',
#               bbox_to_anchor=(0.9, 1.25),
               framealpha = 1,
               shadow=True,
               facecolor='oldlace')

    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print('Save figure of longitudinal dispersivity to {}'.format(save_fig))

    return fig
