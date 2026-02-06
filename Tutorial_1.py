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

## 6. Simulation
"""Positions introduction
long & short positions
long = buy
short = sell

Column D is the mean of Alpha value, Column C is the Alpha value for each stock. 
"""

"""Long-Short Portfolio 
Half of the capital is allocated to long positions (stocks with positive market-neutralized alpha),
and the other half to short positions (stocks with negative market-neutralized alpha).

Long-short portfolio helps minimize market risk influence and reain only the pure signal effect.

1. Market Neutralization
After calculating rank(), we can neutralize the alpha by subtracting the average rank across all companies on each date.
This process is called market neutralization, which helps to remove any market-wide effects and focuses on the relative performance of individual companies.

Column E is the market-neutralized alpha, which is obtained by subtracting the average rank (Column D) from the original rank (Column C).
    market-neutralized alpha = original rank - average rank 

2. Position: Centred around Zero
The market-neutralized alpha (Column E) is centered around zero, meaning that the average value across all companies on each date is zero.

    If the result is positive, it indicates that the stock is ranked higher than the average, suggesting a potential long position.
    If the result is negative, it indicates that the stock is ranked lower than the average, suggesting a potential short position.

Then, compute each absolute value of the market-neutralized alpha (Column F) and total absolute value

3. Normalized Weights
Each normalized weight is calculated by dividing the market-neutralized alpha (Column E) by the total absolute value:
    Normalized weight = Market-Neutralized Alpha value / Total absolute value   

Total of the normalized weights across all companies on each date will be 1, which means that the total capital is fully allocated to the long and short positions.

4. Assigning Capital
The normalized weights are then multiplied by the total capital to determine the amount of capital allocated to each stock. 
    Capital allocated to each stock = Normalized weight * Total capital

5. PnL Calculation
The PnL for each stock is calculated by multiplying the capital allocated to that stock by the return of that stock on the next day.
    PnL for each stock = Capital allocated to each stock * Return of that stock on the next day
    Total PnL = Sum of PnL for all stocks

But, be attention on red and green with their position. Cuz if the position is long (positive weight), a positive return will generate a positive PnL, while a negative return will generate a negative PnL.

"""

## 7. Decay
"""Decay
Decay is a technique used to reduce the influence of older data points in a time series.
By applying a decay factor, we can give more weight to recent data points while diminishing the impact of older data points.

Because changing too many positions in one day can lead to issues such as portfolio unstable, high transaction costs, and market impact

if applying a 3-day:
    Decayed Alpha = (Alpha on Day 1 * 0.5) + (Alpha on Day 2 * 0.3) + (Alpha on Day 3 * 0.2)
or 
    Decayed Alpha = (Alpha on Day 1 * 3) + (Alpha on Day 2 * 2) + (Alpha on Day 3 * 1)/6

Higher decay lower Alpha turnover, which can help to reduce transaction costs and market impact, but it may also reduce the responsiveness of the alpha to recent market changes.
Also alpha's sharpe ratio might decrease because of the reduced responsiveness to recent market changes, which can lead to lower returns.
"""

## 8. Truncation
"""Truncation
Truncation is a technique used to limit the maximum weight a single stock can have in a portfolio.

TOP3000, using about 0.01 is typical. 
However, TOP200, using about higher maximum positions might be better, like 0.05.
"""


## 8. Pasteurization
"""Pasteurization
Pasteurization is a technique used to reduce the influence of extreme values in a data set.

such as, leave the stock not in the top 3000, but assign it a weight as NaN
This can help to improve the stability of the alpha by preventing extreme values from dominating the performance metrics.
"""