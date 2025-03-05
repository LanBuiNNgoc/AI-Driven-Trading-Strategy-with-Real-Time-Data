# AI Driven Trading Strategy with Real Time Data
## Project background:
This is the project that I used to promote myself into the Investment Club of USF. As a student majoring in Statistics and minor in Economics, I do recognize that there is one typical problem for traders nowadays which is to commit to "day trading". Day Trading is a one of the most profitable investing method nowadays which individuals can buy and sell the securities within the same day thanks to its fast - paced form of investing, However, a lot of traders struggle with time commitment and tend to lose track of their trading history which obviously results in a huge loss of money,
## Executive Summary:
This project is to create an AI Strategy Bot with real Time Data. I have applied two main concepts into the way to function the AI: Volatility and "Buy Low Sell High".
The idea behind this trading bot is that: we will design algorithms to let the Bot run and track the fluctuation of the price in 3-month period, and whenever there is a peak in the price of chosen stock, the Bot will send the traders signals to whether buy or sell, and in vice versa with those situations when there is a bottom in a price.
## Insight- Deep Dive:
### 1. Equity Growth and Profitability
- The equity curve from 2009 to 2023 shows consistent growth in portfolio value, reaching **$684,082** by 2023.
- The net profit of **$474,591.54** demonstrates strong profitability, with effective returns outpacing market fees.
- While the growth is steady, the Sharpe ratio of **0.517** suggests that the bot’s returns are not optimally risk-adjusted.
  <br/>*A Sharpe ratio above 1.0 is typically considered good, indicating that the strategy may take on a higher level of risk relative to the returns it generates*
  <br/> <img width="434" alt="Image" src="https://github.com/user-attachments/assets/5b0d97ed-cde6-42e5-a90e-62ad80de8723" />
### 2. Portfolio Turnover
- The portfolio turnover chart suggests a low trading frequency, except for a notable spike around 2015. This low turnover indicates that the trading strategy is focused on maintaining positions for longer periods, reducing transaction costs and potentially enhancing net profits.
  <br/> <img width="421" alt="Image" src="https://github.com/user-attachments/assets/e05c9953-5410-43c4-8274-be43fcc4dd50" />
### 3. Drawdown Behavior
- The drawdown chart illustrates periods of equity decline, with significant drops observed around 2020-2025, reaching as low as -24%. This highlights that, while profitable, the strategy experiences volatility in returns, which aligns with the relatively low Sharpe ratio. The higher drawdowns could be impacting the risk-adjusted performance.
- The pattern of drawdowns shows some recovery, but the frequent dips in equity suggest the model could benefit from improved risk management during high-volatility periods to minimize losses.
### 4. Volatility, Risk, and Sharpe Ratio
- The Sharpe ratio of **0.517** suggests that the trading strategy is delivering returns with a moderate level of risk, but it’s not achieving optimal risk-adjusted performance. The bot may be generating returns, but with significant volatility, leading to lower overall efficiency in balancing risk and reward.
<br/> <img width="404" alt="Image" src="https://github.com/user-attachments/assets/23a06c91-e146-4769-b75c-27b33683c67b" />
## Assumption and Prediction
- The ratio suggests area for improvement by adopting advanced risk management or adjusting exposure in volatile markets to enhance the risk-return profile.
- The project assumes that market data used is accurate, reliable and updated im real-time.
- The bot assumes that current volatility models effectively capture market fluctuations for prediction.
## Prediction 
- The bot is expected to remain profitable, though growth may slow based on recent trends.
- Without enhanced risk management, significant drawdowns may continue to occur.
- Improving risk-adjusted measures could raise the Sharpe ratio, leading to more efficient returns.



