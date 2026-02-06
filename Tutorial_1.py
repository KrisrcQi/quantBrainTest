# BRAIN Basics Tutorial 1
# What's an Alpha?
## 1. Concepts
""" Alpha
Mathematical models that seek to predict the future price movement of various financial instruments as Alphas. 

An Alpha is a type of algorithmic trading strategy used in quantitative finance to generate excess returns above a benchmark index. 
Alphas are designed to exploit market inefficiencies and can be based on various factors such as momentum, value, or sentiment.
"""

""" Backtesting
Backtesting is the process of testing a trading strategy or model using historical data to see how it would have performed in the past.

Implement our idea using code and test its potential performance in the market, a process called backtesting.
"""

## 2. Alpha of "-returns"
"""returns
"returns" is a data field that has the stock's returns for each company on each date.

The "-returns" Alpha is going to bet against the returns.
It is a simple trading strategy that buys an asset when its price decreases and sells it when its price increases.

In other words, the alpha is:
We predicted that companies with high returns yesterday will see price decreases, while those with low returns will see price increases.

This is a type of alpha: Price Reversion
"""

## 3. Operators
"""_summary_
Operators transform data fields into new data fields by applying mathematical operations.

For example, the "-" operator negates the values of a data field.
"""
## 4. Operator: rank()
"""rank()
The rank() operator ranks the values of a data field across all companies on each date.
"""

## 5. Alpha Performance Metrics
"""Alpha Performance Metrics
1. PnL graph
The PnL (Profit and Loss) graph shows the cumulative returns of the alpha over time.

2. IS Summary
The IS (Information Score) Summary provides statistical measures of the alpha's performance, including:

2.1. Sharpe Ratio
sharpe is the measure of risk-adjusted return by alpha, 
calculated as the average return divided by the standard deviation of returns.
    Sharpe ratio = Average Annulized Return / Annulized Std.Dev. of Return # Higher is better; annualized value (squrt(250))
    
2.2. Turnover
Turnover is the percentage of the capital which the alpha trades each day. 
So, turnover measures how frequently the alpha changes its positions. 

A high turnover indicates that the alpha is trading frequently, which can lead to higher transaction costs.

2.3. Fitness
Fitness is a composite score that combines multiple performance metrics into a single value to evaluate the overall quality

In the BRAIN:
    Fitness = sharpe * sqrt(abs(returns))/ Max(turnover, 0.125)

Good Alphas have high fitness. You can optimize the performance of your Alphas by increasing Sharpe (or returns) and reducing turnover

2.4. Returns
Returns indicates how much profit an Alpha can generate. 

Since BRAIN simulations assume a long-short portfolio (which we'll explain in the next step)
The total investment amount equals half of the book size.

2.5. Max Drawdown
Drawdown represents the percentage of the largest loss incurred during any year in the backtesting.

return-to-drawdown ratio > 1 is considered good.
The higher the ratio of returns to drawdown, the better it may be for your alpha.

2.6. Margin
Margin represents how much PnL you obtained relative to the traded amount (not total capital). 

It's calculated by dividing total PnL by the total traded amount. 
    Margin = Total PnL / Total Traded Amount

Note that Margin uses basis points (bps, ‱, or ten thousandths) as its unit of measurement, not %!
"""
