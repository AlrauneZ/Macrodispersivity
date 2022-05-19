#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


### Read in data from Excel file
xl = pd.ExcelFile('../data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

### Filter Reliability
filter_R1 = (data['R – A_L']==1)#*np.isfinite(data['A_L'])
filter_R2 = (data['R – A_L']==2)#*np.isfinite(data['A_L'])

### Plot settings
mec = 'k'
msize = 60
textsize = 12
#c_R1, c_R2 = 'C2','gold'
c_R1, c_R2 = 'C3','C0'
plt.close('all')
plt.rc('text', usetex=True)

### Plotting
plt.figure(1,figsize=[5.4,3.2])
plt.scatter(np.compress(filter_R1,data['Scale']),np.compress(filter_R1,data['A_L']),color=c_R1,marker='o',zorder = 11,edgecolor=mec,s=msize,label=r'high reliablity')
plt.scatter(np.compress(filter_R2,data['Scale']),np.compress(filter_R2,data['A_L']),color=c_R2,marker='o',zorder = 10,edgecolor=mec,s=msize,label=r'moderate reliablity')

plt.legend(loc='lower right',fontsize=textsize)
plt.xlabel('Plume travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Longitudinal dispersivity $\alpha_L$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
# plt.xlim([1,1e4])
# plt.ylim([3e-4,3e1])
plt.tight_layout()

# plt.savefig("../results/Longitudinal_Dispersivities.png", dpi=300)
plt.savefig("../results/Longitudinal_Dispersivities.pdf")
print('Save figure of longitudinal dispersivity to ./results')
