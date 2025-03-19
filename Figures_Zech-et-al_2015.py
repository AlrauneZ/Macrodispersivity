#!/usr/bin/env python3
"""Created on Fri Mar 14 12:15:41 2025

@author: alraune
"""

import pandas as pd
from scripts.analysis.preasymptotic_alphaL import generate_random_preasymptotic_alpha
from scripts.analysis.preasymptotic_alphaL import random_selection
from scripts.data.data_dispersivity_table import select_data_alphaL
from scripts.visualize.plot_dispersivity_data import plot_aL_aquifer
from scripts.visualize.plot_dispersivity_data import plot_alphaL_vs_scale
from scripts.visualize.plot_dispersivity_preasymptotic import plot_random_alphaL_preasymptotic

###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile("./data/Dispersivity_GeoStats.xlsx")
data = pd.read_excel(xl,skiprows = [1])

### Read relevant data for plot from DataFrame
data_alphaL = select_data_alphaL(data)

print("#################################33333##################################")
print("Figure 4: Reliable field data of Longitudinal Macrodispersivity vs scale")
print("######################################33333#############################")

plot_alphaL_vs_scale(data_alphaL,
                     save_fig = "./results/Zech-et-al-2015_Fig4_Longitudinal_Dispersivities.pdf")

###############################################################################

data_aquifers = pd.read_excel("./data/Aquifer_dispersivities_assympotic.xlsx")

print("###################################################################")
print("Figure 5: Aquifer specific Longitudinal macrodispersivity vs scale")
print("###################################################################")

plot_aL_aquifer(data_aquifers,
                figsize= [6,4],
                ylim = [0.1,200],
                save_fig = "./results/Zech-et-al-2015_Fig5_Aquifer_dispersivities.pdf")

print("###################################################################")
print("Figure 6: Computational example")
print("###################################################################")

x_random,alpha_random = generate_random_preasymptotic_alpha()
x_select,alpha_select = random_selection(x_random,alpha_random)

fig = plot_random_alphaL_preasymptotic(x_random,
                                 alpha_random,
                                 x_select = x_select,
                                 alpha_select = alpha_select,
                                 save_fig = "./results/Zech-et-al-2015_Fig6_Computational_Example.pdf",
                                 )
