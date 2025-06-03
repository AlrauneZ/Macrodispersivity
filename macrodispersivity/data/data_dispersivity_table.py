#!/usr/bin/env python3
"""Created on Fri Mar 14 17:23:41 2025

@author: alraune
"""

import numpy as np


def data_per_heterogeneity_class(data):
    data_het_classes = dict()

    for het_level in [1,2,3]:
        filter_het = (data["Heterogeneity class"]==het_level)*np.isfinite(data["A_L"])
        data_het_classes[het_level]=dict(
            aL_het = data["A_L"][filter_het].values,
            weights_het = data["Info level"][filter_het].values/data["Reliability – A_L"][filter_het].values,
            )

    return data_het_classes

def ratios_data_alphaLTV(data):

    ### Filter Reliability
    filter_R1_aTaV = (data["Reliability – A_T/A_V"]==1) #high reliability
    filter_R2_aTaV = (data["Reliability – A_T/A_V"]==2) #moderate reliability

    ### Filter data for scales and alpha_T values for both reliabilities
    scale_aTV_R1 = data["Scale"][filter_R1_aTaV]
    scale_aTV_R2 = data["Scale"][filter_R2_aTaV]

    aT_R1 = data["A_T"][filter_R1_aTaV]
    aT_R2 = data["A_T"][filter_R2_aTaV]

    aV_R1 = data["A_V"][filter_R1_aTaV]
    aV_R2 = data["A_V"][filter_R2_aTaV]

    ### Filter AL data for ratio plots for both reliabilities
    aL_R1 = data["A_L"][filter_R1_aTaV]
    aL_R2 = data["A_L"][filter_R2_aTaV]

    ratios_alphaLTV = dict()
    ratios_alphaLTV["aL_aT_R1"] = aL_R1/aT_R1
    ratios_alphaLTV["aL_aT_R2"] = aL_R2/aT_R2
    ratios_alphaLTV["aT_aL_R1"] = aT_R1/aL_R1
    ratios_alphaLTV["aT_aL_R2"] = aT_R2/aL_R2

    ratios_alphaLTV["aL_aV_R1"] = aL_R1/aV_R1
    ratios_alphaLTV["aL_aV_R2"] = aL_R2/aV_R2
    ratios_alphaLTV["aV_aL_R1"] = aV_R1/aL_R1
    ratios_alphaLTV["aV_aL_R2"] = aV_R2/aL_R2

    ratios_alphaLTV["aT_aV_R1"] = aT_R1/aV_R1
    ratios_alphaLTV["aT_aV_R2"] = aT_R2/aV_R2
    ratios_alphaLTV["aV_aT_R1"] = aV_R1/aT_R1
    ratios_alphaLTV["aV_aT_R2"] = aV_R2/aT_R2

    ratios_alphaLTV["scale_aTV_R1"] = scale_aTV_R1
    ratios_alphaLTV["scale_aTV_R2"] = scale_aTV_R2

    return ratios_alphaLTV

def select_data_alphaTV(data):

    ### Filter Reliability
    filter_R1_aTaV = (data["Reliability – A_T/A_V"]==1) #high reliability
    filter_R2_aTaV = (data["Reliability – A_T/A_V"]==2) #moderate reliability

    data_alpha_TV = dict()
    ### Filter data for scales and alpha_T values for both reliabilities
    data_alpha_TV["scale_R1_aT"] = data["Scale"][filter_R1_aTaV].values
    data_alpha_TV["aT_R1"] = data["A_T"][filter_R1_aTaV].values
    data_alpha_TV["scale_R2_aT"] = data["Scale"][filter_R2_aTaV].values
    data_alpha_TV["aT_R2"] = data["A_T"][filter_R2_aTaV].values

    data_alpha_TV["scale_R1_aV"] = data["Scale"][filter_R1_aTaV].values
    data_alpha_TV["aV_R1"] = data["A_V"][filter_R1_aTaV].values
    data_alpha_TV["scale_R2_aV"] = data["Scale"][filter_R2_aTaV].values
    data_alpha_TV["aV_R2"] = data["A_V"][filter_R2_aTaV].values

    return data_alpha_TV

def select_data_alphaL(data):

    ### Filter Reliability
    filter_R1 = (data["Reliability – A_L"]==1) #high reliability
    filter_R2 = (data["Reliability – A_L"]==2) #moderate reliability

    data_alpha_L = dict()
    data_alpha_L["scale_R1"] = data["Scale"][filter_R1].values
    data_alpha_L["aL_R1"] = data["A_L"][filter_R1].values
    data_alpha_L["scale_R2"] = data["Scale"][filter_R2].values
    data_alpha_L["aL_R2"] = data["A_L"][filter_R2].values

    return data_alpha_L
