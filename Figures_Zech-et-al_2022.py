"""
Created on Fri Mar 14 12:15:41 2025

@author: alraune
"""

import pandas as pd

from scripts.data.extract_data import data_per_heterogeneity_class
from scripts.data.extract_data import data_cape_cod, settings_cape_cod
from scripts.analysis.statistics import macrodispersivity_statistics
from scripts.analysis.functions import mass_monte_carlo_cape_cod
from scripts.visualize.plot_dispersivity_stats import plot_alphaL_cfd
from scripts.visualize.plot_concentrations import plot_cape_cod_example
###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile('./data/Dispersivity_GeoStats.xlsx')
data = pd.read_excel(xl,skiprows = [1])

###############################################################################
data_het_classes = data_per_heterogeneity_class(data)
    

print("###########################################")
print("Table 1: Averages for heterogeneity classes")
print("###########################################")

macrodispersivity_statistics(data_het_classes)

print("###################################################################")
print("Figure 1: Cumulative distribution of αL for heterogeneity classes")
print("###################################################################")


plot_alphaL_cfd(data_het_classes,
                save_fig = "./results/Zech-et-al-2022_Fig1_CDF.pdf")

print("###################################################################")
print("Figure 3: Cape Cod Illustrative example")
print("###################################################################")

data_cape_cod = data_cape_cod()
settings_cape_cod = settings_cape_cod()
mass_monte_carlo_cape_cod(data_cape_cod, settings_cape_cod)
                               
plot_cape_cod_example(data_cape_cod,
                      figsize=[9,3],
                      save_fig = "./results/Zech-et-al-2022_Fig3_CapeCod.pdf")
