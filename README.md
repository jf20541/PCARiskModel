# PCARiskModel

## Objective 
Principal Component Analysis (PCA): Reduces the dimensionality of the data and finds the optimal number of components that captures the max amount of explained variance\

PCA Risk-Factor Model: 𝐫 = 𝐁𝐟 + 𝐬

### Parameters
- `Factor Exposure (B)`: Number of ETFs X Number of Factors (matrix)
- `Factor Returns (f)`: Number of Factors X Number of Timestamps (matrix)
- `Idiosyncratic Risk (s)`: Number of ETFs X Number of Timestamps (matrix)
- `Returns (r)`: Number of ETFs X Number of Timestamps (matrix)

### Methods
- `Augmented Dickey Fuller (ADF) Test`: tests the null hypothesis that a unit root is present in a time series
- `Autocorrelation Function (ACF) `: Coefficient of correlation between two values in a time series 

### Output


### Code
Created 4 modules
- `config.py`: Define paths as global variables
- `main.py`: Use Principal Component Analysis as a Risk Factor Model 
- `data.py`: Clean data and get daily returns for all 10 SPDR ETF Sector ETFs


### Install
Python libraries installed:
- [Pandas](http://pandas.pydata.org)
- [NumPy](https://numpy.org/)
- [Sklearn](https://scikit-learn.org/stable/)
- [YFinance](https://pypi.org/project/yfinance/)


### Run
In a terminal or command window, navigate to the top-level project directory `PCARiskModel/` and run one of the following command:
```bash
pip install --upgrade pip && pip install -r requirements.txt
```

### Sources
