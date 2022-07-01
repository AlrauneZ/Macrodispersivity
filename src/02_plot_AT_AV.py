#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Read in data from Excel file
xl = pd.ExcelFile('../data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

### Filter Reliability
filter_R1 = (data['Reliability – A_T/A_V']==1) #high reliability
filter_R2 = (data['Reliability – A_T/A_V']==2) #moderate reliability

filter_AT = np.isfinite(data['A_T'])
filter_AV = np.isfinite(data['A_V'])

### Plot settings
mec = 'k'
msize = 60
textsize = 12
c_R1, c_R2 = 'C3','C0'
plt.close('all')

### Plotting
plt.figure(1,figsize=[5.4,3.2])

plt.scatter(data['Scale'][filter_R1*filter_AT],data['A_T'][filter_R1*filter_AT],color=c_R1,marker='h',zorder = 11,edgecolor=mec,s=msize,label=r'$\alpha_T$')
plt.scatter(data['Scale'][filter_R2*filter_AT],data['A_T'][filter_R2*filter_AT],color=c_R2,marker='h',zorder = 10,edgecolor=mec,s=msize,label=r'$\alpha_T$')

plt.scatter(data['Scale'][filter_R1*filter_AV],data['A_V'][filter_R1*filter_AV],color=c_R1,marker='^',zorder = 11,edgecolor=mec,s=msize,label=r'$\alpha_V$ - high reliablity')
plt.scatter(data['Scale'][filter_R2*filter_AV],data['A_V'][filter_R2*filter_AV],color=c_R2,marker='^',zorder = 10,edgecolor=mec,s=msize,label=r'$\alpha_V$ - moderate reliablity')

plt.legend(loc='upper center',fontsize=textsize,ncol=2,facecolor='oldlace')
plt.xlabel('Plume travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Transverse dispersivity $\alpha_T$, $\alpha_V$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim([9,1.1e3])
plt.ylim([3e-4,10])
plt.tight_layout()

# plt.savefig("../results/Transverse_Dispersivities.png", dpi=300)
plt.savefig("../results/Transverse_Dispersivities.pdf")
print('Save figure of transverse horizontal dispersivity to ./results')
