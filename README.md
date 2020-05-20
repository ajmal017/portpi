# PortPi

----

## Getting Started
### Required Packages:

* pandas
* yfinance
* investpy
* datetime

### Installation

Current installation is basically cloning the library to the working directory. Basic import statements can be used after this step.

----

## Packages
### Data Management
Data management functionality can be found in the data_management package. Access to this module can be done with the statement;

`from data_management import data_management`

This module houses the data class. The Data class is responsible for;
* Gathering the data and saving it
* Merging the Close data of individual assets to a single DataFrame

### Time Series Analysis
Time series analysis functionality is located in time_series_analysis package. This functionality can be access via the import code;

`from time_series_analysis import returns`

This package currently contains the returns module which works with daily returns of individual assets.

The classes stored in this module are, **Returns** and **Distributions**.

#### Returns
Calculates and handling of daily asset returns data.

Can be initialized by the code;

`ret = Returns(compiled_close_dataframe)`

#### Distributions
Does the calculations of basic statistics (mean, standard deviation, kurtosis) for any given dataset.

Can be initialized by the code;

`dsit = Distributions(data_dataframe):`

----

## Issues

Current version lacks documentation on some functions. These will be soon adressed.

----
