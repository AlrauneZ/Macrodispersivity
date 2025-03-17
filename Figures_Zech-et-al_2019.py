"""
Created on Fri Mar 14 12:15:41 2025

@author: alraune
"""

import pandas as pd
from scripts.data.data_dispersivity_table import select_data_alphaTV, select_data_alphaL, ratios_data_alphaLTV
from scripts.visualize.plot_dispersivity_data import plot_alphaL_vs_scale,plot_alphaTV_vs_scale,plot_ratios_alpha_vs_scale

###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile('./data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

data_alphaL = select_data_alphaL(data)

### Reproducing Figure 2b
plot_alphaL_vs_scale(data_alphaL,
                     figsize=[5.4,4],
                     marker_R1 = 'h',
                     marker_R2 = 'h',
                     xlim = [.3,1e5],
                     ylim = [0.0003,2800],
                     )

###############################################################################

data_alpha_TV = select_data_alphaTV(data)

plot_alphaTV_vs_scale(data_alpha_TV,
                      save_fig = './results/Zech-et-al-2019_Fig2_Transverse_dispersivities.pdf')

ratios_alphaLTV = ratios_data_alphaLTV(data)

plot_ratios_alpha_vs_scale(ratios_alphaLTV,
                           save_fig = './results/Zech-et-al-2019_Fig3_Ratios_dispersivities.pdf')

