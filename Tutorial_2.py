# BRAIN Basics Tutorial 2

## Operators in BRAIN
"""
Details in the operator.py file.
"""

## PV Alphas vs. Fundamental Alphas


### 1. PV Alphas
"""Price-Volume (PV) Alphas
PV data includes stock prices - highest, lowest, open, close, and other trading related data:
    volume of shares
    market capitalization 


Price data could be represented in candlestick charts

Volume indicates the shares investors transacted that day
such as: adv20; 20 days average volume.
    ts_mean(volume, n) could compute n days volumes mean
"""

#### 1.1. VWAP (Volume-weighted average price)
"""Volume weighted average price
VWAP represents average daily stock price, which is weighted by trading volume. 
Since, low trading volume might give false picture

    VWAP = sum(price * volume)/sum(volume)
"""
#### 1.2. PV-data Alpha idea:
"""
1. Momentum
Assume that stock performed well which will continuely perform well. While stocks performed poorly, it will do so as well. 

Momentum effect: typically appears over longer periods (several months or more)

2. Reversion
The hypothesis is that if something increases today, it will fall tomorrow. 
But this hypothesis could apply on any indicator: price, volume, correlation between two things. 

Reversion effect: appears over shorter periods (days or weeks).
"""
#### 1.3. Technical Anlaysis
"""Technical analysis
TA is an analyzed method that seeks to predict future price movements based on historical price and volume data.


"""

### 2. Fundamental Alphas
"""Fundamental Alphas

"""

