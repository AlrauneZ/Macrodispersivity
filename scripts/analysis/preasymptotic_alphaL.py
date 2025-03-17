#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 21:47:23 2025

@author: alraune
"""

import numpy as np

def sets_preasymptotic_alphaL(sigmaY2s = [1],
                             Ihs = [1],
                             ees = [1],
                             x = np.arange(0,10.1,0.1),                             
                            ):
    
    alpha_sets = dict()
    i = 0
    for sigmaY2 in sigmaY2s:
        for Ih in Ihs:
            for ee in ees:
                alphaL = preasymptotic_alphaL(x, sigmaY2 = sigmaY2, Ih = Ih, ee = ee)
                alpha_sets[i] = dict(
                    sigmaY2 = sigmaY2,
                    Ih = Ih,
                    ee = ee,
                    x = x,
                    alphaL = alphaL,
                    )
                i+=1
    return alpha_sets

def preasymptotic_alphaL(x,sigmaY2,Ih,ee=1):
    
    be = anisotropy_factor(ee)
    alphaL_preasymp =  sigmaY2 * Ih * (1. - np.exp(-x/Ih * be))  
    
    return alphaL_preasymp

def anisotropy_factor(ee):

    if ee < 1 and ee > 0:
        e1 = (ee * ee - 1) ** 2
        e2 = np.sqrt(1.0 - ee * ee)
        bee = (
            1.0
            + ee * ee * (19.0 - 10 * ee * ee) / 16.0 / e1
            - ee * (13.0 - 4.0 * ee * ee) * np.arcsin(e2) / (16.0 * e2 * e1)
        )
    elif ee == 1:
        bee = 8.0 / 15.0
    elif ee == 0:
        bee = 1.0
    return bee

def preasymptotic_alphaL_FirstOrder(x,sigma,ell):
    """
    First order approximation of preasymptotic alpha_L as used in paper
    Zech et al., 2015 (eventually very similar to other function, but 
                       does not account for anisotropy)
    """
    y = ell/x
    z = np.exp(-x/ell)

    alpha = sigma*ell*(1 - 24.*y**4*(z-1) - 24.*y**3*z - 4.*y**2*(2*z + 1))
    # alpha = 0.5*(-2.0*(-24.0*ell**3/x**4+8.0*np.exp(-x/ell)*ell**3/x**4+16.0*np.exp(-x/ell)*ell**2*(1.0+ell/x)/x**3+4.0*ell/x**2+8.0*np.exp(-x/ell)*ell*(1.0+ell/x)/x**2)+2.0/ell)*sigma*ell**2
    return alpha

def log_uniform(x_range,size, N=10000):

    """ Draw samples from a uniform distribution at logspace - base 10

    Definition
    ----------
    def log_uniform():


    Input
    -----
    x_range: tuple of 2 floats (lower, upper)
        lower and upper boundary of the output interval 
    size:    tuple of 2 ints (m, n)       
        output shape, number of samples drawn: m * n
 
    Options
    -------
    N       (integer)               : transfer value

    Output
    ------
    out : (ndarray)                 : Drawn samples, with shape size
     
    """ 
    X_lin=np.random.randint(1,N,size)
    X_log=np.logspace(np.log10(x_range[0]),np.log10(x_range[1]),num=N)
    out=np.zeros(size)
    
    for i in range(0,size[0]):      
        for j in range(0,size[1]):
            out[i,j]=X_log[X_lin[i,j]]
    
    return out     

def generate_random_preasymptotic_alpha(n_aquifers = 50,
                               n_locations = 5,
                               x_range = [5,300],
                               sigma_range = [0.1,1.0],
                               ell_range = [0.2,10],
                               first_order = True,
                               seed = 20250319,
                              ):
    """
    Generating preasymptic values of longitudinal macrodispersivities aL as function of plume travel distance.
    Macrodispersivities are calculated from statistical parameters of hydraulic conductivity following first order theory (Daga, 1989).
    
    Random values of aquifer statistics (log-conductivity variance and correlation length) are randomly generated for 
    a number of virtual aquifers. Also a number of aquifer locations are generated for these aquifers. For these locations
    and aquifer statistics preasymptotic macrodispersivities are calculated.
    
    Input
    -----
    n_aquifers: int
        number of random aquifers
    n_locations: int
        number of sample locations per aquifer
    x_range: tuple of 2 floats (lower, upper)
        lower and upper boundary of sample locations
    sigma_range: tuple of 2 floats (sigma_min, sigma_max)
        range of random log-conductivity variances
    ell_range: tuple of 2 floats (ell_min, ell_max)
        range of random correllation lengths

    Output
    ------
    x_range: array of shape (n_aquifers,n_locations)
        sample locations `n_locations` for each of the `n_aquifers`
    alpha_random: array of shape (n_aquifers,n_locations)
        values of preasymptotic macrodispersivity 
        - for `n_aquifers` aquifers with random statistics
        - with `n_locations` values per aquifer
    """
    np.random.seed(seed)
    x_random=np.sort(log_uniform(x_range,[n_aquifers,n_locations]),axis=1) # generating locations via uniform sampling, but at log-scale
    sigma_random=np.random.uniform(sigma_range[0],sigma_range[1],n_aquifers) # generating random log-K variance 
    ell_random=np.random.uniform(ell_range[0],ell_range[1],n_aquifers) # generating random correlation length

    alpha_random=np.zeros((n_aquifers,n_locations))

    for i in range(n_aquifers):
        if first_order:
            alpha_random[i,:]=preasymptotic_alphaL_FirstOrder(x_random[i,:],sigma_random[i],ell_random[i])
        else:
            alpha_random[i,:]=preasymptotic_alphaL(x_random[i,:],sigma_random[i],ell_random[i])

    return x_random,alpha_random

def random_selection(x_random,alpha_random):
    i_alpha_min = np.argmin(alpha_random[:,-1])
    i_alpha_max = np.argmax(alpha_random[:,-1])
    alpha_mid = np.sqrt(alpha_random[i_alpha_min,-1]*alpha_random[i_alpha_max,-1])
    i_alpha_mid = np.argmin(np.abs(alpha_random[:,-1]-alpha_mid))
    range_select = [i_alpha_min,i_alpha_mid,i_alpha_max]
    #return [i_alpha_min,i_alpha_mid,i_alpha_max]    

    return x_random[range_select,:],alpha_random[range_select,:]
    