import numpy as np
from scipy.special import erf
from scipy.stats import lognorm


def mass_monte_carlo_cape_cod(data_cape_cod,
                              settings_cape_cod,
                              x = np.arange(0,300,1), #m
                              **kwargs,
                              ):

    for index, (ti, data_ti) in enumerate(data_cape_cod.items()):

        m_median, m_90p, m_10p = monte_carlo_alpha(x,ti,**settings_cape_cod)
        data_ti["m_median"] = m_median
        data_ti["m_90p"] = m_90p
        data_ti["m_10p"] = m_10p
        data_ti["x"] = x

        mcum_median, mcum_90p, mcum_10p = monte_carlo_alpha(x,ti,cumulative = True,**settings_cape_cod)
        data_ti["mcum_median"] = mcum_median
        data_ti["mcum_90p"] = mcum_90p
        data_ti["mcum_10p"] = mcum_10p

    return data_cape_cod

def monte_carlo_alpha(x, #m
                      t, #d
                      v =1, #m/d
                      alphaL_mean = 1., #m
                      alphaL_std = 1, #m
                      cumulative = False,
                      **kwargs,
                      ):
    """### Monte Carlo Procedure to create mass distributions for random values
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

    Returns:
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
    """Random values from log-normal distribution

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

    Returns:
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
    """Mass density

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

    Returns:
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
    """Cumulative mass

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

    Returns:
    -------
    m : TYPE
        DESCRIPTION.

    """
    xx = np.tile(x,(len(alphaL),1))
    aa = np.tile(alphaL,(len(x),1)).T
    X11 = 2*aa*U*t
    m = 0.5*(1-erf(-(xx-U*t)/np.sqrt(2*X11)))
    return m
