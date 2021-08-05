# PCASectorETF

### Objective
Using Principal Component Analysis (PCA) as a Risk-Factor Model 
PCA reduces the dimensionality of these data and finds representation of them that explains a maximum amount of their variance

### Outputs
```bash
Sum of all Variance Retained: 0.928%
Number of Principal Components Needed: 3
Reduced the Dimenionality of the timeseries by: 70.0%
```

### Code
Created 4 modules
- `config.py`: Define path global variables
- `main.py`: Calculated n-components needed to retain a given amount of variance and percentage of dimensionality reduction
- `data.py`: Extract adjusted-closing price of all SP500 Equities from the webscrape.py list
- `webscrape.py`: Webscrape the SP500 WikiTable using BeautifulSoup and append all assets into a list


### Install
Python libraries installed:

- [Pandas](http://pandas.pydata.org)
- [Sklearn](https://scikit-learn.org/stable/)
- [bs4.BeautifulSoup](https://pypi.org/project/pmdarima/)
- [YFinance](https://pypi.org/project/yfinance/)


### Run
In a terminal or command window, navigate to the top-level project directory `PCASectorETF/` and run one of the following command:

```bash
pip install --upgrade pip && pip install -r requirements.txt
```

### Sources
