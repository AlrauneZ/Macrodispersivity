import numpy as np
from scipy.special import erf
from scipy.stats import lognorm

def cdf(x,log_mean,log_var):
    """
    Cumulative density function for log-normal distribution.

    Input
    -----
    x : float or np.array of floats
        argument values
    log_mean: 
        log-mean value
    log_var: 
        log-varience value

    Output
    ------
    cdf: float or np.array of floats
        function values for arguments    
    """
    
    cdf = 0.5*(1+erf((np.log(x)-log_mean)/np.sqrt(2*log_var)))
    return cdf

def MonteCarloAlpha(x,
                    t,
                    v,
                    alphaL_mean, 
                    alphaL_std,
                    cumulative = False,
                    **kwargs,
                    ):

    """
    ### Monte Carlo Procedure to create mass distributions for random values 
    of dispersivity from log-normal distribution

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    t : TYPE
        DESCRIPTION.
    U : TYPE
        DESCRIPTION.
    alphaL : TYPE
        DESCRIPTION.

    Returns
    -------
    m : TYPE
        DESCRIPTION.

    """

    r_alpha = random_alpha(alphaL_mean, alphaL_std,**kwargs)

    if cumulative:
        m = mass_cumulative(x,t,v,r_alpha)
    else:
        m = mass_density(x,t,v,r_alpha)
    
    m_median = np.median(m,axis=0)
    m_90p = np.percentile(m,90,axis = 0)
    m_10p = np.percentile(m,10,axis = 0)

    return m_median, m_90p, m_10p


def random_alpha(alphaL_mean,
                 alphaL_std,
                 n_sample = 1000,
                 **kwargs,
                 ):
    """
    random values from log-normal distribution

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    t : TYPE
        DESCRIPTION.
    U : TYPE
        DESCRIPTION.
    alphaL : TYPE
        DESCRIPTION.

    Returns
    -------
    m : TYPE
        DESCRIPTION.

    """

    log_mean = np.log(alphaL_mean**2/np.sqrt(alphaL_mean**2+alphaL_std**2))
    log_var = np.log(1+(alphaL_std/alphaL_mean)**2)
    #median = np.exp(log_mean)   
    r_alpha = lognorm.rvs(np.sqrt(log_var),scale=np.exp(log_mean),size=n_sample)

    return r_alpha

def mass_density(x,t,U,alphaL):
    """
    mass density

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    t : TYPE
        DESCRIPTION.
    U : TYPE
        DESCRIPTION.
    alphaL : TYPE
        DESCRIPTION.

    Returns
    -------
    m : TYPE
        DESCRIPTION.

    """

    alphaL = np.array(alphaL,ndmin=1)
    xx = np.tile(x,(len(alphaL),1))
    aa = np.tile(alphaL,(len(x),1)).T
    X11 = 2*aa*U*t
    m = 1./np.sqrt(2*np.pi*X11)*np.exp(-(xx-U*t)**2/(2*X11))
    return m
    
def mass_cumulative(x,t,U,alphaL):
    """
    cumulative mass

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    t : TYPE
        DESCRIPTION.
    U : TYPE
        DESCRIPTION.
    alphaL : TYPE
        DESCRIPTION.

    Returns
    -------
    m : TYPE
        DESCRIPTION.

    """

    xx = np.tile(x,(len(alphaL),1))
    aa = np.tile(alphaL,(len(x),1)).T
    X11 = 2*aa*U*t
    m = 0.5*(1-erf(-(xx-U*t)/np.sqrt(2*X11)))
    return m
