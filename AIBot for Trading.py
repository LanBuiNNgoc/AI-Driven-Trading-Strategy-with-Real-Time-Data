#This is a project used to analyze, predict (uncover/study) the trends, and give some visualization 
#import the libraries used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#download  SPY data from Yahoo finance
data = yf.download("SPY", start = '2009-04-02', end='2023-4-1')

#ploting the closing price
plt.figure(figsize=(10,6))
plt.plot(data['Close'],label='SPY Close Price')
plt.title('SPY Price History')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

#set initial parameters
initial_lookback = 30
ceiling, floor = 20,15
initialStopRisk = 0.98
trailingStopRisk = 0.9

#Calculate rolling volatility using pandas' rolling ans std method
data['vol_30'] = data['Close'].rolling(window=30).std()

#stimulate the breakout strategy
lookbacks = []
high_prices = []
stop_prices = []
invested = False
breakoutlvl = 0
highestPrice = 0

for i in range(30, len(data)):
  #dynamically determine lookback length
  close = data['Close'][i-31:i].values

  #check if there is enough data for std calculation
  if len(close[1:31]) > 1 and len(close[0:30]) > 1:
    todayvol = np.std(close[1:31])
    yesterdatvol = np.std(close[0:30])


    #check for the zero division
    if todayvol != 0:
      deltavol = (todayvol - yesterdatvol) / todayvol
    else:
      deltavol = 0
  else:
    deltavol = 0


  lookback = round(initial_lookback * (1 + deltavol))

  if lookback > ceiling:
    lookback = ceiling
  elif lookback < floor:
    lookback = floor

  lookbacks.append(lookback)

  #check for breakout condition
  high_values = data['High'][i-lookback:i-1].values
  high_values = high_values[~np.isnan(high_values)]

  if len(high_values) > 0:
    high = max(high_values)
  else:
    high = 0

  high_prices.append(high)

  # If not invested and breakout occurs
  if not invested and data['Close'].iloc[i].item() >= high:
        invested = True
        breakoutlvl = high
        highestPrice = breakoutlvl
        stop_price = initialStopRisk * breakoutlvl
        stop_prices.append(stop_price)
        print(f"Breakout at {data.index[i]}: Buying SPY at {data['Close'].iloc[i]}")
  elif invested:
        # Update stop loss
        if data['Close'].iloc[i].item() > highestPrice:
            highestPrice = data['Close'].iloc[i].item()
            stop_price = trailingStopRisk * highestPrice
        stop_prices.append(stop_price)

        # If stop loss hit, exit position
        if data['Close'].iloc[i].item() < stop_price:
            invested = False
            print(f"Stopped out at {data.index[i]}: Selling SPY at {data['Close'].iloc[i]}")
        else:
            stop_prices.append(np.nan)  # Reset stop price when not invested
  else:
        stop_prices.append(np.nan)  # No stop price when not invested

#Convert the dataframe into plotting
plot_data = pd.DataFrame(index = data.index[30:])
plot_data['lookback'] = pd.Series(lookbacks[-len(data.index[30:]):], index = data.index[30:])
plot_data['stop_price'] = pd.Series(stop_prices[-len(data.index[30:]):], index = data.index[30:])
plot_data['high_price'] = pd.Series(high_prices[-len(data.index[30:]):], index = data.index[30:])


#plotting the data
fig, ax = plt.subplots(figsize = (12,6))

#Plot SPY Close Price
ax.plot(data['Close'], label='SPY Close Price', color='blue')

# Plot High Price (Breakout Level)
ax.plot(plot_data['high_price'], label='High Price (Breakout Level)', color='green', linestyle='--')

# Plot Stop Price
ax.plot(plot_data['stop_price'], label='Stop Price', color='red', linestyle='-.')

# Highlight buy and sell signals
# Buy signals (where stop_price is not NaN and previous value was NaN)
buy_signals = plot_data[(~plot_data['stop_price'].isnull()) & (plot_data['stop_price'].shift(1).isnull())]
ax.scatter(buy_signals.index, buy_signals['stop_price'], marker='^', color='green', s=100, label='Buy Signal')

# Sell signals (where stop_price is NaN and previous value was not NaN)
ax.scatter(sell_signals.index, data['Close'].loc[sell_signals.index], marker='v', color='red', s=100, label='Sell Signal')

ax.set_title('SPY Price with Dynamic Lookback and Breakout Strategy')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend()
plt.grid(True)
plt.tight_layout()
plt.show()



