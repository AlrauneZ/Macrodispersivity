"""Tests for the macrodispersivity.data module.

@author: Alraune Zech
"""

#import numpy as np
import pandas as pd
#import pytest

from macrodispersivity.data.data_dispersivity_table import data_per_heterogeneity_class

###############################################################################
### Read in data from Excel file
xl = pd.ExcelFile("./data/Dispersivity_GeoStats.xlsx")
data = pd.read_excel(xl,skiprows = [1])

###############################################################################

class TestData:
    """Class for testing data routines."""

    def test_data_per_heterogeneity_class_01(self):
        data_het_classes = data_per_heterogeneity_class(data)
