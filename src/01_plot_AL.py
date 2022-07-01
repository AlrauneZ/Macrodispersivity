#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Read in data from Excel file
xl = pd.ExcelFile('../data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

### Filter Reliability
filter_R1 = (data['Reliability – A_L']==1) #high reliability
filter_R2 = (data['Reliability – A_L']==2) #moderate reliability

### Plot settings
mec = 'k'
msize = 60
textsize = 12
c_R1, c_R2 = 'C3','C0'
plt.close('all')

### Plotting
plt.figure(1,figsize=[5.4,3.2])
plt.scatter(data['Scale'][filter_R1],data['A_L'][filter_R1],color=c_R1,marker='o',zorder = 11,edgecolor=mec,s=msize,label=r'high reliablity')
plt.scatter(data['Scale'][filter_R2],data['A_L'][filter_R2],color=c_R2,marker='o',zorder = 10,edgecolor=mec,s=msize,label=r'moderate reliablity')

plt.legend(loc='lower right',fontsize=textsize,facecolor='oldlace')
plt.xlabel('Plume travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Longitudinal dispersivity $\alpha_L$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,1e4])
plt.ylim([9e-2,20])
plt.tight_layout()

# plt.savefig("../results/Longitudinal_Dispersivities.png", dpi=300)
plt.savefig("../results/Longitudinal_Dispersivities.pdf")
print('Save figure of longitudinal dispersivity to ./results')
