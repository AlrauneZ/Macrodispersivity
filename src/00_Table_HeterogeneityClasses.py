#!/usr/bin/env python3

import numpy as np
import pandas as pd

xl = pd.ExcelFile('../data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

print("###########################################")
print("Table 1: Averages for heterogeneity classes")
print("###########################################")

for het_level in [1,2,3]:
    filter_het = (data['Heterogeneity class']==het_level)*np.isfinite(data['A_L'])

    aL_het = np.compress(filter_het,data['A_L'])
    weights_het = np.compress(filter_het,data['Weights'])

    mean_het = np.mean(aL_het)
    std_het = np.std(aL_het)
    
    meanw_het = np.average(aL_het,weights=weights_het)
    stdw_het = np.sqrt(np.average(aL_het**2,weights=weights_het)-meanw_het**2)
    
    print("\nLevel of Heterogeneity: ", het_level)
    print(" Number of sites: {}".format(len(aL_het)))    
    print(" Mean of AL (weighted): {:.2f}".format(meanw_het))
    print(" Std of AL: (weighted) {:.2f}".format(stdw_het))
    # print(" Mean of AL (not weighted): {:.2f}".format(mean_het))
    # print(" Std of AL (not weighted): {:.2f}".format(std_het))
    print(" Coefficient of Variation CV: {:.2f}".format(stdw_het/meanw_het))
