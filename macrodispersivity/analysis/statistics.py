#!/usr/bin/env python3
"""Created on Fri Mar 14 16:25:36 2025

@author: alraune
"""

import numpy as np
from scipy.special import erf


def macrodispersivity_statistics(data_het_classes,
                                 verbose = True,
                                 ):

    for het_level in data_het_classes:

        aL_het = data_het_classes[het_level]["aL_het"]
        weights_het = data_het_classes[het_level]["weights_het"]

        meanw_het = np.average(aL_het,weights=weights_het)
        stdw_het = np.sqrt(np.average(aL_het**2,weights=weights_het)-meanw_het**2)

        mean_het = np.mean(aL_het)
        std_het = np.std(aL_het)

        log_meanw = np.log(meanw_het**2/np.sqrt(meanw_het**2+stdw_het**2))
        log_varw = np.log(1+(stdw_het/meanw_het)**2)

        if verbose:
            print("\nLevel of Heterogeneity: ", het_level)
            print(f" Number of sites: {len(aL_het)}")
            print(f" Mean of AL (weighted): {meanw_het:.2f}")
            print(f" Std of AL: (weighted) {stdw_het:.2f}")
            # print(" Mean of AL (not weighted): {:.2f}".format(mean_het))
            # print(" Std of AL (not weighted): {:.2f}".format(std_het))
            print(f" Coefficient of Variation CV: {stdw_het/meanw_het:.2f}")

        data_het_classes[het_level]["number_sites"] = len(aL_het)
        data_het_classes[het_level]["mean_w_al"] = meanw_het
        data_het_classes[het_level]["std_w_al"] = stdw_het
        data_het_classes[het_level]["cv_w_al"] = stdw_het/meanw_het
        data_het_classes[het_level]["mean_al"] = mean_het
        data_het_classes[het_level]["std_al"] = std_het
        data_het_classes[het_level]["log_meanw"] = log_meanw
        data_het_classes[het_level]["log_varw"] = log_varw

    return data_het_classes

def cdf(x,log_mean,log_var):
    """Cumulative density function for log-normal distribution.

    Input
    -----
    x : float or np.array of floats
        argument values
    log_mean: 
        log-mean value
    log_var: 
        log-varience value

    Output
    ------
    cdf: float or np.array of floats
        function values for arguments    
    """
    cdf = 0.5*(1+erf((np.log(x)-log_mean)/np.sqrt(2*log_var)))
    return cdf
