# PCARiskModel & PCASectorETF

## Objective for PCARiskModel
Principal Component Analysis (PCA): Reduces the dimensionality of the data and finds the optimal number of components that captures the max amount of explained variance

PCA Risk-Factor Model:\
![](https://latex.codecogs.com/gif.latex?%5Cdpi%7B120%7D%20%5Cbg_white%20%5CLARGE%20%5Cmathbf%7Br%20%3D%20Bf%20&plus;%20s%7D)


## Objective for PCASectorETF
Using Principal Component Analysis (PCA) as a Risk-Factor Model to reduces the dimensionality of these data and finds a representation of them that explains a maximum amount of their variance

## Repository File Structure
    ├── src          
    │   ├── main.py              # Use Principal Component Analysis as a Risk Factor Model
    │   ├── data.py              # Clean data and get daily returns for all 10 SPDR ETF Sector ETFs
    │   ├── config.py            # Define path as global variable
    │   ├── ETF_main.py          # Calculated n-components needed to retain a given amount of variance and percentage of dimensionality reduction
    │   ├── ETF_webscrape.py     # Webscrape the SP500 WikiTable using BeautifulSoup and append all assets into a list
    │   ├── ETF_data.py          # Extract Adjusted-Closing price of all SP500 Equities from the webscrape.py list
    ├── plots
    │   ├── Factor Returns.png   # Factor Returns time-series
    │   └── TotalPCA.png         # Total Percent Variance Explained
    ├── inputs
    │   ├── train.csv            # Adj-Closing Price for SPDR Sector ETF
    │   ├── sp_train.py          # SPDR Sector ETF Adj-Closing Price 
    │   └── train.csv            # Adj-Closing Price data
    ├── requierments.txt         # Packages used for project
    └── README.md
        
## Output for PCA Risk Model
```bash
Principal Component  0 for 0.6286258454061395
Principal Component  1 for 0.18822793060925014
Principal Component  2 for 0.06392275282080973
Principal Component  3 for 0.04026355667943605
```
## Output for PCA Sector ETF
```
Sum of all Variance Retained: 0.928%
Number of Principal Components Needed: 4
Reduced the Dimenionality of the timeseries by: 70.0%
```

## Parameters
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

![alt text](https://github.com/jf20541/PCARiskModel/blob/main/plots/Factor%20Returns.png?raw=true)
