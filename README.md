[![DOI](https://zenodo.org/badge/329326997.svg)](https://zenodo.org/badge/latestdoi/329326997)

# Overview

This project aims to provide visualizations of reliable values of 
macrodispersivity from field tracer tests.

## Target Parameters
 - longitudinal macrodispersivity
 - transverse horizontal dispersivity
 - transverse vertical dispersivity

## Data source
The data collection is based on the meta-studies (and references therein): 

> Evidence based Estimation of Macrodispersivity for Groundwater Transport Applications
> Alraune Zech, Sabine Attinger, Alberto Bellin, Vladimir Cvetkovic, Gedeon Dagan, Peter Dietrich, Aldo Fiori, and Georg Teutsch; 
> Groundwater, under revision, 2022

> A Critical Analysis of Transverse Dispersivity Field Data; 
> Alraune Zech, Sabine Attinger, Alberto Bellin, Vladimir Cvetkovic, Gedeon Dagan, Peter Dietrich, Aldo Fiori, and Georg Teutsch; 
> Groundwater, 57 (4), 632-639, 2019
> https://doi.org/10.1111/gwat.12838

> Is unique scaling of aquifer macrodispersivity supported by field data?; 
> Alraune Zech, Sabine Attinger, Vladimir Cvetkovic, Gedeon Dagan, Peter Dietrich, Aldo Fiori, Yoram Rubin, and Georg Teutsch; 
> Water Resources Research 51, 7662–7679; 2015
> https://dx.doi.org/10.1002/2015WR017220


## Structure

The project is organized as follows:

- `README.md` - description of the project
- `results/` - folder with plots
- `data/` - folder containing table with field data
- `src/` - folder containing the Python scripts of the project:
  + `00_Table_HeterogeneityClasses.py` - load macrodispersivity data from table and identify averages for heterogeneity classes (Tab 1, Zech et al., 2022)
  + `01_plot_AL.py` - visualize longitudinal macrodispersivity data (Fig 4, Zech et al., 2015)
  + `02_plot_AT_AV.py` - visualize transverse dispersivity data (Fig 1b, Zech et al., 2019)
  + `03_plot_AL_CDFs.py` - visualize cumulative density functions of dispersivity for heterogeneity classes (Fig 1, Zech et al., 2022) 
  + `04_plot_CapeCod.py` - visualize illustration example for an instantaneous injection in a low heterogeneous aquifer with comparison to observations from the Cape Cod experiment. (Fig 3, Zech et al., 2022) 
  + `05_plot_AL-preasymptotic.py` - visualize evolution of pre-asymptotic longitudinal macrodistispersivity as function of travel distance L relative to integral scales (Fig 4, Zech et al., 2022) 

## Python environment

To make the example reproducible, we provide the following files:
- `requirements.txt` - requirements for [pip](https://pip.pypa.io/en/stable/user_guide/#requirements-files) to install all needed packages

You can install them with `pip` (potentially in a virtual environment):
```bash
pip install -r requirements.txt
```

## Contact

You can contact us via <a.zech@uu.nl>.

## License

MIT © 2022
