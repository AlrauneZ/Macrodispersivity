#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.stats import lognorm

### Plot settings
textsize = 8
cc = ['C1','C2','C4']
plt.close('all')
# plt.rc('text', usetex=True)

def m(x,t,U,alphaL):
    ### mass density
    alphaL = np.array(alphaL,ndmin=1)
    xx = np.tile(x,(len(alphaL),1))
    aa = np.tile(alphaL,(len(x),1)).T
    X11 = 2*aa*U*t
    m = 1./np.sqrt(2*np.pi*X11)*np.exp(-(xx-U*t)**2/(2*X11))
    return m
    
def M(x,t,U,alphaL):
    ### cumulatice mass
    xx = np.tile(x,(len(alphaL),1))
    aa = np.tile(alphaL,(len(x),1)).T
    X11 = 2*aa*U*t
    m = 0.5*(1-erf(-(xx-U*t)/np.sqrt(2*X11)))
    return m

x = np.arange(0,300,1) #m
t1 = 203 #d
t2 = 461 #d
U = 0.42 #m/d    
alphaL_mean = 1.1
alphaL_std = 1.1
log_mean = np.log(alphaL_mean**2/np.sqrt(alphaL_mean**2+alphaL_std**2))
log_var = np.log(1+(alphaL_std/alphaL_mean)**2)
median = np.exp(log_mean)

### Read data values
file_name = '../data/Cape_Cod_day_{}.csv'
data_t1 = np.loadtxt(file_name.format(t1),delimiter=',')
data_t2 = np.loadtxt(file_name.format(t2),delimiter=',')

##############################################################################
### Monte Carlo Procedure
### generate dispersivity values from log-normal distribution
#m0 = m(x,t1,U,median)[0,:]

s = np.sqrt(log_var)
scale = np.exp(log_mean)
n_sample = 1000
r = lognorm.rvs(s,scale=scale,size=n_sample)

m1 = m(x,t1,U,r)
M1 = M(x,t1,U,r)
 
m1_median = np.median(m1,axis=0)
M1_median = np.median(M1,axis=0)
m1_90p = np.percentile(m1,90,axis = 0)
m1_10p = np.percentile(m1,10,axis = 0)
M1_90p = np.percentile(M1,90,axis = 0)
M1_10p = np.percentile(M1,10,axis = 0)
   
m2 = m(x,t2,U,r)
M2 = M(x,t2,U,r)
 
m2_median = np.median(m2,axis=0)
M2_median = np.median(M2,axis=0)
m2_90p = np.percentile(m2,90,axis = 0)
m2_10p = np.percentile(m2,10,axis = 0)
M2_90p = np.percentile(M2,90,axis = 0)
M2_10p = np.percentile(M2,10,axis = 0)

plt.figure(figsize=[7.5,2.7])
ax1=plt.subplot(121)  
ax2=plt.subplot(122)

ax1.plot(x,m1_median,color='C3',zorder=2,lw=2)
ax1.fill_between(x,m1_10p,m1_90p,color='C0',zorder=1,alpha = 0.5)
ax1.plot(x,m2_median,color='C3',zorder=2,lw=2)
ax1.fill_between(x,m2_10p,m2_90p,color='C0',zorder=1,alpha = 0.5)
ax1.set_xlim([0,300])
ax1.set_ylim([0,0.06])
# plt.legend(loc='lower right',fontsize=textsize,ncol=2)
ax1.set_xlabel(r'Distance $x$ [m]',fontsize=textsize)    
ax1.set_ylabel('Mass distribution',fontsize=textsize)   

ax1.tick_params(axis="both",which="major",labelsize=textsize)
ax1.grid(True)
ax1.text(-0.13,-0.13,'(a)', bbox=dict(facecolor='w', alpha=1,boxstyle='round'),fontsize=textsize, transform=ax1.transAxes)
ax1.annotate('{} days'.format(t1),xy = (90,0.03),xytext = (110,0.035),arrowprops = dict(arrowstyle='->'))
ax1.annotate('{} days'.format(t2),xy = (200,0.02),xytext = (220,0.025),arrowprops = dict(arrowstyle='->'))

ax2.plot(x,M1_median,color='C3',zorder=2,lw=2)
ax2.fill_between(x,M1_10p,M1_90p,color='C0',zorder=1,alpha = 0.5)
ax2.plot(x,M2_median,color='C3',zorder=2,lw=2)
ax2.fill_between(x,M2_10p,M2_90p,color='C0',zorder=1,alpha = 0.5)

ax2.plot(data_t1[:,0],data_t1[:,1],'ok',ms=4)
ax2.plot(data_t2[:,0],data_t2[:,1],'ok',ms=4)
ax2.annotate('{} days'.format(t1),xy = (85,0.5),xytext = (105,0.62),arrowprops = dict(arrowstyle='->'))
ax2.annotate('{} days'.format(t2),xy = (195,0.5),xytext = (215,0.62),arrowprops = dict(arrowstyle='->'))

ax2.set_xlim([0,300])
ax2.set_ylim([0,1])
ax2.set_xlabel(r'Distance $x$ [m]',fontsize=textsize)    
ax2.set_ylabel('Cumulative mass',fontsize=textsize)    
ax2.tick_params(axis="both",which="major",labelsize=textsize)
ax2.grid(True)
ax2.text(-0.13,-0.13,'(b)', bbox=dict(facecolor='w', alpha=1,boxstyle='round'),fontsize=textsize, transform=ax2.transAxes)
plt.tight_layout()

plt.savefig("../results/Figure_03_CapeCod.pdf")
print('Save figure to ../results')
