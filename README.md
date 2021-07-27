# Overview

This project aims to provide visualizations of reliable values of 
macrodispersivity from field tracer tests.

## Target Parameters
 - longitudinal macrodispersivity
 - transverse horizontal dispersivity
 - transverse vertical dispersivity

## Data source
The data collection is based on the meta-studies (and references therein): 

> Is unique scaling of aquifer macrodispersivity supported by field data?; 
> Alraune Zech, Sabine Attinger, Vladimir Cvetkovic, Gedeon Dagan, Peter Dietrich, Aldo Fiori, Yoram Rubin, and Georg Teutsch; 
> Water Resources Research 51, 7662–7679; 2015
> https://dx.doi.org/10.1002/2015WR017220

> A Critical Analysis of Transverse Dispersivity Field Data; 
> Alraune Zech, Sabine Attinger, Alberto Bellin, Vladimir Cvetkovic, Gedeon Dagan, Peter Dietrich, Aldo Fiori, and Georg Teutsch; 
> Ground Water, 57 (4), 632-639, 2019
> https://doi.org/10.1111/gwat.12838


## Structure

The project is organized as follows:

- `README.md` - description of the project
- `results/` - folder with plots
- `data/` - folder containing table with field data
- `src/` - folder containing the Python scripts of the project:
  + `01_plot_dispersivity.py` - visualize macrodispersivity data

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

MIT © 2021
