import matplotlib.pyplot as plt


def plot_alphaL_vs_scale(data_alphaL,
                        figsize=[5.4,3.2],
                        marker_R1 = "o",
                        marker_R2 = "o",
                        color_R1 = "C3",
                        color_R2 = "C0",
                        label_R1 = "high reliablity",
                        label_R2 = "moderate reliablity",
                        mec = "k",
                        msize = 60,
                        textsize = 12,
                        save_fig = None,
                        xlabel = "Plume travel distance $L$ [m]",
                        ylabel = r"Longitudinal dispersivity $\alpha_L$ [m]",
                        xlim = [1,1e4],
                        ylim = [9e-2,20],
                        xscale = "log",
                        yscale = "log",
                        grid = True,
                        ):

    ### Plotting
    fig = plt.figure(figsize=figsize)
    plt.scatter(data_alphaL["scale_R1"],
                data_alphaL["aL_R1"],
                color=color_R1,
                marker=marker_R1,
                s=msize,
                edgecolor=mec,
                zorder = 11,
                label = label_R1)

    plt.scatter(data_alphaL["scale_R2"],
                data_alphaL["aL_R2"],
                color=color_R2,
                marker=marker_R2,
                s=msize,
                edgecolor=mec,
                zorder = 10,
                label=label_R2)

    plt.legend(loc="lower right",fontsize=textsize,facecolor="oldlace")
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
        print(f"Save figure to {save_fig}")

    return fig

def plot_aL_aquifer(
        data_aquifers,
        figsize=[5.4,3.2],
        exp_selection = [1,5,3,2,4,8],
        colors = ["C3","C0","C2","C4","gold","C1"],
        marker_R1 = "o",
        marker_R2 = "d",
        marker_sigmaL = "<",
        mec = "k",
        msize = 8,
        textsize = 12,
        ylim = [0.1,30],
        xlabel = "Travel distance [m]",
        ylabel = r"Macrodispersivity $\alpha_L$ [m]",
        xscale = "log",
        yscale = "log",
        grid = True,
        save_fig = None,
        ):

    fig = plt.figure(figsize=figsize)


    for j,i in enumerate(exp_selection): #range(1,10): #
        filter_exp = data_aquifers["Experiment"] == i
        site_name = data_aquifers["site name"].loc[filter_exp].iloc[0]
        reliability = data_aquifers["reliability"].loc[filter_exp].iloc[0]
        sigma = data_aquifers["sigma"].loc[filter_exp].iloc[0]
        ell = data_aquifers["ell"].loc[filter_exp].iloc[0]

        if reliability == 1:
            marker_type = marker_R1
        elif reliability == 2:
            marker_type = marker_R2

        plt.plot(data_aquifers["scale"].loc[filter_exp],
                 data_aquifers["AL"].loc[filter_exp],
                 marker = marker_type,
                 ms = msize,
                 mec = mec,
                 ls = "",
                 c = colors[j],
                 label = site_name,
                 zorder = 10,
                 )

        plt.scatter(330,sigma*ell,
                    marker = marker_sigmaL,
                    s = 80,
                    edgecolors = mec,
                    color = colors[j],
                    )

        plt.plot([300,300],ylim,c="k",lw = 0.8)

    plt.xscale(xscale)
    plt.yscale(yscale)
    plt.xlabel(xlabel,fontsize = textsize)
    plt.ylabel(ylabel,fontsize = textsize)
    plt.ylim(ylim)
    plt.grid(grid)

    plt.legend(ncols=2,
               fontsize = textsize,
               loc = "upper left",
#               bbox_to_anchor=(0.9, 1.25),
               framealpha = 1,
               shadow=True,
               facecolor="oldlace")

    plt.tight_layout()

    if isinstance(save_fig, str):
        plt.savefig(save_fig,dpi=300)
        print(f"Save figure to {save_fig}")

    return fig

def plot_alphaTV_vs_scale(data_alpha_TV,
                          figsize=[5.4,4],
                          marker_AT = "o",
                          marker_AV = "^",
                          color_R1 = "C3",
                          color_R2 = "C0",
                          mec = "k",
                          msize = 60,
                          textsize = 12,
                          xlabel = "Observation scale $L$ [m]",
                          ylabel = r"Transverse dispersivities [m]",
                          xlim = [.3,1e5],
                          ylim = [0.0003,2800],
                          xscale = "log",
                          yscale = "log",
                          loc="upper left",
                          grid = True,
                          save_fig = None,
                          ):

    ### Plotting
    fig = plt.figure(figsize=figsize)
    if marker_AT is not False:
        plt.scatter(data_alpha_TV["scale_R1_aT"],
                    data_alpha_TV["aT_R1"],
                    color=color_R1,
                    marker=marker_AT,
                    s=msize,
                    edgecolor=mec,
                    zorder = 12,
                    label = r"$\alpha_T$ - R1")

        plt.scatter(data_alpha_TV["scale_R2_aT"],
                    data_alpha_TV["aT_R2"],
                    color=color_R2,
                    marker=marker_AT,
                    s=msize,
                    edgecolor=mec,
                    zorder = 10,
                    label=r"$\alpha_T$ - R2")

    if marker_AV is not False:
        plt.scatter(data_alpha_TV["scale_R1_aV"],
                    data_alpha_TV["aV_R1"],
                    color=color_R1,
                    marker=marker_AV,
                    s=msize,
                    edgecolor=mec,
                    zorder = 13,
                    label = r"$\alpha_V$ - R1")

        plt.scatter(data_alpha_TV["scale_R2_aV"],
                    data_alpha_TV["aV_R2"],
                    color=color_R2,
                    marker=marker_AV,
                    s=msize,
                    edgecolor=mec,
                    zorder = 11,
                    label = r"$\alpha_V$ - R2")


    plt.legend(loc=loc,fontsize=textsize,facecolor="oldlace")
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
        print(f"Save figure to {save_fig}")

    return fig

def plot_ratios_alpha_vs_scale(ratios_alphaLTV,
                              figsize=[5.4,4],
                              marker_AL_AT = "d",
                              marker_AT_AL = False,
                              marker_AL_AV = "v",
                              marker_AV_AL = False,
                              marker_AT_AV = "s",
                              marker_AV_AT = False,
                              color_R1 = "C3",
                              color_R2 = "C0",
                              mec = "k",
                              msize = 60,
                              textsize = 12,
                              xlabel = "Observation scale $L$ [m]",
                              ylabel = "Ratios of dispersivities [-] [m]",
                              xlim = [0.3,100000],
                              ylim = [0.1,200000],
                              xscale = "log",
                              yscale = "log",
                              loc="upper right",
                              ncols = 1,
                              grid = True,
                              save_fig = None,
                              ):

    fig = plt.figure(figsize=figsize)

    scale_aTV_R1 = ratios_alphaLTV["scale_aTV_R1"]
    scale_aTV_R2 = ratios_alphaLTV["scale_aTV_R2"]

    if marker_AL_AT is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aL_aT_R1"],
                    color=color_R1,marker=marker_AL_AT,edgecolor=mec,
                    s=msize,label=r"$\alpha_L/\alpha_T$ (R1)",zorder = 16)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aL_aT_R2"],
                    color=color_R2,marker=marker_AL_AT,edgecolor=mec,
                    s=msize,label=r"$\alpha_L/\alpha_T$ (R2)",zorder = 10)

    if marker_AT_AL is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aT_aL_R1"],
                    color=color_R1,marker=marker_AT_AL,edgecolor=mec,
                    s=msize,label=r"$\alpha_T/\alpha_L$ (R1)",zorder = 17)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aT_aL_R2"],
                    color=color_R2,marker=marker_AT_AL,edgecolor=mec,
                    s=msize,label=r"$\alpha_T/\alpha_L$ (R2)",zorder = 11)

    if marker_AL_AV is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aL_aV_R1"],
                    color=color_R1,marker=marker_AL_AV,edgecolor=mec,
                    s=msize,label=r"$\alpha_L/\alpha_V$ (R1)",zorder = 18)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aL_aV_R2"],
                    color=color_R2,marker=marker_AL_AV,edgecolor=mec,
                    s=msize,label=r"$\alpha_L/\alpha_V$ (R2)",zorder = 12)

    if marker_AV_AL is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aV_aL_R1"],
                    color=color_R1,marker=marker_AV_AL,edgecolor=mec,
                    s=msize,label=r"$\alpha_V/\alpha_L$ (R1)",zorder = 19)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aV_aL_R2"],
                    color=color_R2,marker=marker_AV_AL,edgecolor=mec,
                    s=msize,label=r"$\alpha_V/\alpha_L$ (R2)",zorder = 13)

    if marker_AT_AV is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aT_aV_R1"],
                    color=color_R1,marker=marker_AT_AV,edgecolor=mec,
                    s=msize,label=r"$\alpha_T/\alpha_V$ (R1)",zorder = 20)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aT_aV_R2"],
                    color=color_R2,marker=marker_AT_AV,edgecolor=mec,
                    s=msize,label=r"$\alpha_T/\alpha_V$ (R2)",zorder = 14)

    if marker_AV_AT is not False:
        plt.scatter(scale_aTV_R1,ratios_alphaLTV["aV_aT_R1"],
                    color=color_R1,marker=marker_AV_AT,edgecolor=mec,
                    s=msize,label=r"$\alpha_V/\alpha_T$ (R1)",zorder = 21)
        plt.scatter(scale_aTV_R2,ratios_alphaLTV["aV_aT_R2"],
                    color=color_R2,marker=marker_AV_AT,edgecolor=mec,
                    s=msize,label=r"$\alpha_V/\alpha_T$ (R2)",zorder = 15)

    plt.legend(loc=loc,fontsize=textsize,ncols = ncols, facecolor="oldlace",framealpha = 1,shadow=True)
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
        print(f"Save figure to {save_fig}")

    return fig
