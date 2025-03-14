#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 12:15:41 2025

@author: alraune
"""

import pandas as pd
from scripts.visualize.plot_dispersivity_data import plot_alphaL_vs_scale,plot_aL_aquifer


###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile('./data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

### Filter Reliability
filter_R1 = (data['Reliability – A_L']==1) #high reliability
filter_R2 = (data['Reliability – A_L']==2) #moderate reliability

plot_alphaL_vs_scale(data['Scale'][filter_R1],data['A_L'][filter_R1],
                     data['Scale'][filter_R2],data['A_L'][filter_R2],
                     save_fig = './results/Zech-et-al-2015_Fig4_Longitudinal_Dispersivities.pdf')

###############################################################################

data_aquifers = pd.read_excel('./data/Aquifer_dispersivities_assympotic.xlsx')


plot_aL_aquifer(data_aquifers,
                figsize= [6,4],
                ylim = [0.1,200],
                save_fig = './results/Zech-et-al-2015_Fig5_Aquifer_dispersivities.pdf')