import config
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt


def factor_exposure(pca, beta_idx, beta_cols):
    """Factor Exposure shows how exposed each asset is to each risk factor.
        A specific variance of assets that is not explained by the risk factors.
    Args:
        pca [object]: dimensionality reduction
        beta_idx [date]: 1 dimensional np-array containing index-dates
        beta_cols [int]: 1 dimensional np-array of (n_components - 1)
    Returns:
        [float]: Pandas DataFrame of Factor Exposure (B)
    """
    return pd.DataFrame(pca.components_.T, beta_idx, beta_cols)


def factor_returns(pca, returns, return_idx, return_cols):
    """Measures the returns of your portfolio that is due to the alpha vector.
        Depends on the stock universe and time window of our theoretical portfolio
    Args:
        pca [object]: dimensionality reduction
        returns [float]: daily returns dataframe
        return_idx [float]: dimensional np-array containing index-dates
        return_cols [int]: 1 dimensional np-array of (n_components - 1)
    Returns:
        [float]: Pandas DataFrame of Factor Returns (f)
    """
    return pd.DataFrame(pca.transform(returns), return_idx, return_cols)


def idiosyncratic_var_matrix(returns, factor_returns, factor_exposure, ann_factor):
    """Idiosyncratic risk matrix (original returns data minus the part we represent with the PCA)
    Args:
        returns [float]: daily returns dataframe
        factor_returns [float]: output of the factor_returns function
        factor_exposure [float]: output of the factor_exposure function
        ann_factor [int]: annualized of 252 trading days
    Returns:
        [float]: Pandas DataFrame of Idiosyncratic Risk (S)
    """
    common_returns = pd.DataFrame(
        np.dot(factor_returns, factor_exposure.T), returns.index, returns.columns
    )
    residuals = returns - common_returns
    return pd.DataFrame(
        np.diag(np.var(residuals)) * ann_factor, returns.columns, returns.columns
    )


def factor_cov_matrix(factor_returns, ann_factor):
    """Calculate the cov matrix of the residuals and set the off diagonal elements to zero
    Args:
        factor_returns [float]: output of the factor_exposure function
        ann_factor [int]: annualized of 252 trading days
    Returns:
        [float]: calculated the annualized factor covariance in diagonal np-array
    """
    return np.diag(factor_returns.var(axis=0, ddof=1) * ann_factor)


class PCARiskModel:
    """
    Using PCA to reduce the dimensionality of the data and that captures
    max amount of their variance. Minimize risk as part of an optimization problem
    """

    def __init__(self, returns, ann_factor, n_components, pca):
        self.factor_exposure_ = factor_exposure(
            pca, returns.columns.values, np.arange(n_components)
        )
        self.factor_returns_ = factor_returns(
            pca, returns, returns.index, np.arange(n_components)
        )
        self.factor_cov_matrix_ = factor_cov_matrix(self.factor_returns_, ann_factor)
        self.idiosyncratic_var_matrix_ = idiosyncratic_var_matrix(
            returns, self.factor_returns_, self.factor_exposure_, ann_factor
        )


if __name__ == "__main__":
    df_returns = pd.read_csv(config.TRAINING_FILE)

    # initiate PCA and fit daily returns
    pca = PCA(n_components=4, svd_solver="full")
    pca.fit(df_returns)

    # Call the PCARiskModel class to plot 4 component returns
    pca_model = PCARiskModel(df_returns, 252, 4, pca)

    for idx, val in enumerate(pca.explained_variance_ratio_):
        print(f"Principal Component  {idx} for {val}")

    # plot Total Percent Variance Explained and Factor Returns
    def plot():
        plt.bar(np.arange(4), pca.explained_variance_ratio_)
        plt.title("Total Percent Variance Explained")
        plt.ylabel("Explained Variance (%)")
        plt.xlabel("Number of Components")
        plt.savefig("../plots/TotalPCA.png")

        pca_model.factor_returns_.loc[:, 0:3].cumsum().plot()
        plt.title("Factor Returns")
        plt.ylabel("Component Returns(%)")
        plt.xlabel("Time")
        plt.savefig("../plots/Factor Returns.png")
        plt.show()

    plot()
