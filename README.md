# PCARiskModel

## Objective 
Principal Component Analysis (PCA): Reduces the dimensionality of the data and finds the optimal number of components that captures the max amount of explained variance

PCA Risk-Factor Model:\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7Br%20%3D%20Bf%20&plus;%20s%7D)


### Parameters
- `Factor Exposure (B)`: Number of ETFs X Number of Factors (matrix)

- `Factor Returns (f)`: Number of Factors X Number of Timestamps (matrix)\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7Bf%20%3D%20B%5E%7BT%7Dr%7D)

- `Idiosyncratic Risk (s)`: Number of ETFs X Number of Timestamps (matrix)\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7Bs%20%3D%20r%20-%20Bf%7D)

- `Idiosyncratic Risk  of the Residuals (S)`:\
Calculated the covar matrix of the residuals and set off-diagonal elements to 0\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7BS%20%3D%20%5Cfrac%7B1%7D%7BT-1%7Dss%5E%7BT%7D%7D)

- `Returns (r)`: Number of ETFs X Number of Timestamps (matrix)\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7Br%20%3D%20Bf%20&plus;%20s%7D)
 
- `Factor Covariance Matrix (F)`:\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7BF%20%3D%20%5Cfrac%7B1%7D%7BT-1%7Dff%5E%7BT%7D%7D)


### Output
```bash
Principal Component  0 for 0.6286258454061395
Principal Component  1 for 0.18822793060925014
Principal Component  2 for 0.06392275282080973
Principal Component  3 for 0.04026355667943605
```

![alt text](https://github.com/jf20541/PCARiskModel/blob/main/plots/Factor%20Returns.png?raw=true)




### Code
Created 3 modules
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
