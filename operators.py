# Accumulated operators in BRAIN
import numpy as np
import pandas as pd


# 1. mius (-)
def negate(data_field):
    """ -
    the "-" operator negates the values of a data field.

    For example, applying the "-" operator to the "returns" 
    Data field will create a new data field that contains the negative returns for each company on each date.
    """
    return -data_field

# 2. rank()
def rank(data_field):
    """ rank()
    The rank() operator ranks the values of a data field across all companies on each date. 
    
    """
    # Assuming data_field is a pandas DataFrame with companies as columns and dates as index
    ranked_field = data_field.rank(axis=1, method='average', ascending=True)
    return ranked_field

# 3. ts_rank()
def ts_rank(data_field, window):
    """ ts_rank()
    The ts_rank() operator ranks the values of a data field over a specified time window for each company.
    
    Args:
        data_field (pd.DataFrame): DataFrame with companies as columns and dates as index.
        window (int): The time window over which to compute the rank. 
    """
    def rank_within_window(x):
        return x.rolling(window=window).apply(lambda y: pd.Series(y).rank().iloc[-1])

    ts_ranked_field = data_field.apply(rank_within_window, axis=0)
    return ts_ranked_field

""" examples
HYPOTHESIS: if the "cashflow" increases over the past 3 days, the stock price will go up.
"""
# Sample data of cashflow for three companies over 10 days
data = {
    'CompanyA': [100, 105, 110, 120, 130, 140, 150, 160, 170, 180],
    'CompanyB': [200, 195, 190, 185, 180, 175, 170, 165, 160, 155],
    'CompanyC': [300, 310, 320, 330, 340, 350, 360, 370, 380, 390]
}
dates = pd.date_range(start='2023-01-01', periods=10)
data_field = pd.DataFrame(data, index=dates)
# Applying ts_rank with a window of 3 days
window = 3
ts_ranked_data = ts_rank(data_field, window)
print(data_field)
print(ts_ranked_data)

# Somehow this testing example is failed. 
# The origal idea is:
""" ts_rank(operating_income, 252)
HYPOTHESIS: 
If the operating income of a company is currently higher than its past 1 year history, buy the company's stock and vice-versa.
 
IMPLEMENTATION: 
Using ts_rank to identify current performance of the company compared to its own history, using the fundamental data field "operating_income".    

HINT TO IMPROVE THE ALPHA: 
Rather than comparing the value directly, can calculating a ratio that includes stock market moves, improve the signal?
"""