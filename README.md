# StockTradingWithML
This repository is trying to do Stock Trading prediction with Machine Learning Algorithm. This is different with stock closing price prediction, and I do not focus on closing price prediction because it would be impossible to predict the price because of the marketing inefficiency. And even you got not much perfect predicted closing price, there would not be much help for trading especially in a market with T+1 trading rule.

In this project, we setup a benchmark stock data with China "pingan" stock with number "601318". Refer https://github.com/waditu/Tushare to get the stock data.
The full data is from 20080401 to 20190530, and the total data number is 2562:
1. training data is 0~2341
2. validation data is 2342~2542
3. data from 2543 to 2562 is for reserve purpose

The simple buy and hold strategy profit is 55.67%. 

We use a machine learning mechanism to do trading, and get the profit of 76.94%. 

The legend of below figure is:
1. Red: buy
2. Green: sell
3. Blue: hold

![Trading Diagram](https://github.com/LizhongJin/StockTradingWithML/blob/master/images/trading_1.png)


We post the data because we would like to hear more exciting data that other algorithm could reach. Feel free to post here.
