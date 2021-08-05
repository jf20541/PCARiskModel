import pandas as pd
import numpy as np
import config
from sklearn.decomposition import PCA


def pca_components(returns, var_ret):
    """
    Calculated the number of components needed to retain a given amount of variance
    returns: parameter returns calculate using pct_change()
    var_ret: varinace returns range [0,1]
    """
    if var_ret == 1:
        return returns.shape[1]

    # inititate Principal Component Analysis and fit on returns
    pca = PCA(n_components=returns.shape[1])
    pca.fit(returns)

    # set (n_components, total_var) to 0
    n_components = 0
    total_var = 0

    for i in range(0, returns.shape[1]):
        if total_var >= var_ret:
            var_sum = pca.explained_variance_ratio_[0:n_components].sum()
            print(f"Sum of all Variance Retained: {var_sum:.3f}%")
            return n_components
        else:
            # append to both local variables
            n_components += 1
            total_var += pca.explained_variance_ratio_[i]


if __name__ == "__main__":
    # import data, set index and calculate returns
    df = pd.read_csv(config.TRAINING_FILE)
    df = df.set_index("Date")
    df_returns = df.apply(lambda x: x.pct_change().dropna())

    # calculated the number of components needed to retain a given amount of variance
    num_components = pca_components(df_returns, 0.9)
    print(f"Number of Principal Components Needed: {num_components}")

    # Calculate the percentage of dimensionality reduction
    reduce_dim = ((df_returns.shape[1] - num_components) / df_returns.shape[1]) * 100
    print(f"Reduced the Dimenionality of the timeseries by: {reduce_dim}%")
