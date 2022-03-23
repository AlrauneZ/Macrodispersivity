#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import erfc,erf

### Read in data from Excel file
xl = pd.ExcelFile('../data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

def cdf(alpha_range,log_mean,log_var):
    # cdf = 1-0.5*erfc((np.log(alpha_range)-log_mean)/np.sqrt(2*log_var))
    cdf = 0.5*(1+erf((np.log(alpha_range)-log_mean)/np.sqrt(2*log_var)))
    return cdf

### Plot settings
textsize = 8
cc = ['C1','C2','C4']
plt.close('all')
plt.rc('text', usetex=True)

plt.figure(1,figsize=[3.75,2.7])
for ii,het_level in enumerate([1,2,3]):
    filter_het = (data['Heterogeneity class']==het_level)*np.isfinite(data['A_L'])
    aL_het = np.compress(filter_het,data['A_L'])
    plt.plot(np.sort(aL_het),np.linspace(0,1,len(aL_het)+2)[1:-1],'o',ls='',ms=5,c=cc[ii],label='Class {}  data'.format(het_level))

for ii,het_level in enumerate([1,2,3]):
    filter_het = (data['Heterogeneity class']==het_level)*np.isfinite(data['A_L'])
    aL_het = np.compress(filter_het,data['A_L'])
    weights_het = np.compress(filter_het,data['Weights'])

    meanw_het = np.average(aL_het,weights=weights_het)
    std_het = np.std(aL_het)

    log_mean = np.log(meanw_het**2/np.sqrt(meanw_het**2+std_het**2))
    log_var = np.log(1+(std_het/meanw_het)**2)

    alpha_range = np.arange(0.001,13,0.1)
    lognorm_cdf = cdf(alpha_range,log_mean,log_var)

    plt.plot(alpha_range,lognorm_cdf,c=cc[ii],lw=2,label='CDF')
    
plt.xlim([0,13])
plt.ylim([0,1])
plt.legend(loc='lower right',fontsize=textsize,ncol=2)
plt.xlabel(r'Longitudinal dispersivity $\alpha_L$ [m]',fontsize=textsize)    
plt.ylabel('CFD',fontsize=textsize)    
plt.tick_params(axis="both",which="major",labelsize=textsize)
plt.grid(True)

# plt.savefig("../results/Longitudinal_Dispersivities.png", dpi=300)
plt.savefig("../results/Figure_01_CDF.pdf")
print('Save figure of longitudinal dispersivity to ./results')
