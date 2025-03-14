"""
Created on Fri Mar 14 12:15:41 2025

@author: alraune
"""

import pandas as pd
from scripts.visualize.plot_dispersivity_data import plot_alphaL_vs_scale


###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile('./data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

### Filter Reliability
filter_R1 = (data['Reliability – A_L']==1) #high reliability
filter_R2 = (data['Reliability – A_L']==2) #moderate reliability

### Reproducing Figure 2b
plot_alphaL_vs_scale(data['Scale'][filter_R1],data['A_L'][filter_R1],
                     data['Scale'][filter_R2],data['A_L'][filter_R2],
                     figsize=[5.4,4],
                     marker_R1 = 'h',
                     marker_R2 = 'h',
                     xlim = [.3,1e5],
                     ylim = [0.0003,2800],
                     )

###############################################################################

