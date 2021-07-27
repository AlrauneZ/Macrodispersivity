# -*- coding: utf-8 -*-
"""
Script to visualize reliable macrodispersivity data from field tracer tests
@author: A. Zech
Licence MIT, A.Zech, 2020
"""

import numpy as np
import matplotlib.pyplot as plt

#########################################
### Load Data ###
#########################################

data_values = np.array(np.genfromtxt('../data/dispersivities.csv',skip_header = 1,delimiter = ','))#,names = True)

index_aL = (data_values[:,1]!=-9999)
index_aT = (data_values[:,2]!=-9999)
index_aV = (data_values[:,3]!=-9999)

index_R1 = (data_values[:,4]==1) # high reliablity
index_R2 = (data_values[:,4]==2) # medium reliability

mec = 'k'
msize = 40
textsize = 12
plt.close('all')
plt.rc('text', usetex=True)

plt.figure(1,figsize=[5.4,3.2])
plt.scatter(data_values[index_aL*index_R1,0],data_values[index_aL*index_R1,1], color='C2',marker='o',zorder = 11,edgecolor=mec,s=msize,label=r'high reliablity')
plt.scatter(data_values[index_aL*index_R2,0],data_values[index_aL*index_R2,1], color='gold',marker='o',zorder = 10,edgecolor=mec,s=msize,label=r'moderate reliablity')
plt.legend(loc='lower left',fontsize=textsize)
plt.xlabel('Plume Travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Longitudinal dispersivity $\alpha_L$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,1e4])
plt.ylim([3e-4,3e1])
plt.tight_layout()
plt.savefig("../results/Longitudinal_Dispersivity.png", dpi=300)
print('Save figure of longitudinal dispersivity to ./results')

plt.figure(2,figsize=[5.4,3.2])
plt.scatter(data_values[index_aT*index_R1,0],data_values[index_aT*index_R1,2], color='C2',marker='s',zorder = 11,edgecolor=mec,s=msize,label=r'high reliablity')
plt.scatter(data_values[index_aT*index_R2,0],data_values[index_aT*index_R2,2], color='gold',marker='s',zorder = 10,edgecolor=mec,s=msize,label=r'moderate reliablity')
plt.legend(loc='upper right',fontsize=textsize)
plt.xlabel('Plume Travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Transverse horizontal dispersivity $\alpha_T$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,1e4])
plt.ylim([3e-4,3e1])
plt.tight_layout()
plt.savefig("../results/Trans_horizontal_Dispersivity.png", dpi=300)
print('Save figure of transverse horizontal dispersivity to ./results')

plt.figure(3,figsize=[5.4,3.2])
plt.scatter(data_values[index_aV*index_R1,0],data_values[index_aV*index_R1,3], color='C2',marker='^',zorder = 11,edgecolor=mec,s=msize,label=r'high reliablity')
plt.scatter(data_values[index_aV*index_R2,0],data_values[index_aV*index_R2,3], color='gold',marker='^',zorder = 10,edgecolor=mec,s=msize,label=r'moderate reliablity')
plt.legend(loc='upper right',fontsize=textsize)
plt.xlabel('Plume Travel distance $L$ [m]',fontsize=textsize)    
plt.ylabel(r'Transverse vertical dispersivity $\alpha_V$',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.xlim([1,1e4])
plt.ylim([3e-4,3e1])
plt.tight_layout()
plt.savefig("../results/Trans_vertical_Dispersivity.png", dpi=300)
print('Save figure of transverse vertical dispersivity to ./results')

