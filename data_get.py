#########The code is only for study purpose############
import numpy as np
import math
import talib as ta
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts

token=xxx #here is your tushare token, register tushare to get
ts.set_token(token)
pro=ts.pro_api()

def featureExt(data_input=None):
  open    = data_input['open'].values.astype(np.float64)
  low     = data_input['low'].values.astype(np.float64)
  high    = data_input['high'].values.astype(np.float64)
  close   = data_input['close'].values.astype(np.float64)
  volume  = data_input['vol'].values.astype(np.float64)
  
  data_input['xclose']      = data_input['close']
  data_input['MA5']         = ta.MA(np.array(close), timeperiod=5)
  data_input['MA10']        = ta.MA(np.array(close), timeperiod=10)
  data_input['MA20']        = ta.MA(np.array(close), timeperiod=20)
  data_input['EMA12']       = ta.EMA(np.array(close), timeperiod=6)  
  data_input['EMA26']       = ta.EMA(np.array(close), timeperiod=12) 
  data_input['MACD'],data_input['MACDsignal'],data_input['MACDhist'] = ta.MACD(np.array(close),
                                    fastperiod=6, slowperiod=12, signalperiod=9)
  
  data_input['RSI']         = ta.RSI(np.array(close), timeperiod=12)     
  data_input['MOM']         = ta.MOM(np.array(close), timeperiod=5)
  
  data_input['K'],data_input['D'] = ta.STOCH(np.array(high),np.array(low),np.array(close),
                                      fastk_period=9,slowk_period=3,slowk_matype=0,
                                      slowd_period=3,slowd_matype=0)
  data_input['J']           = data_input.K*3-data_input.D*2
  
  ##########Volatility Indicator Functions########
  data_input['ATR']   = ta.ATR(np.array(high), np.array(low), np.array(close), timeperiod=14)
  
  #########Volume Indicator Functions#############
  data_input['OBV']   = ta.OBV(np.array(close), np.array(volume))
  data_input['AD']    = ta.AD(np.array(high),np.array(low),np.array(close), np.array(volume))
  data_input['ADOSC'] = ta.ADOSC(np.array(high),np.array(low),np.array(close), np.array(volume))
  
  #########Overlap Studies###########
  data_input['UPPERBAND'], data_input['MIDDLEBAND'], data_input['LOWERBAND'] = ta.BBANDS(np.array(close), timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
  data_input['DEMA'] = ta.DEMA(np.array(close), timeperiod=30)
  data_input['EMA'] = ta.EMA(np.array(close), timeperiod=30)
  data_input['HT_TRENDLINE'] = ta.HT_TRENDLINE(np.array(close))
  data_input['KAMA'] = ta.KAMA(np.array(close), timeperiod=30)
  data_input['MA'] = ta.MA(np.array(close), timeperiod=30, matype=0)
  data_input['MIDPOINT'] = ta.MIDPOINT(np.array(close), timeperiod=14)
  data_input['MIDPRICE'] = ta.MIDPRICE(np.array(high), np.array(low), timeperiod=14)
  data_input['SAR'] = ta.SAR(np.array(high), np.array(low), acceleration=0, maximum=0)
  data_input['SAREXT'] = ta.SAREXT(np.array(high), np.array(low), startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
  data_input['SMA'] = ta.SMA(np.array(close), timeperiod=30)
  data_input['T3'] = ta.T3(np.array(close), timeperiod=5, vfactor=0)
  data_input['TEMA'] = ta.TEMA(np.array(close), timeperiod=30)
  data_input['TRIMA'] = ta.TRIMA(np.array(close), timeperiod=30)
  data_input['WMA'] = ta.WMA(np.array(close), timeperiod=30)
  
  #########Momentum Indicators###########
  data_input['ADX'] = ta.ADX(np.array(high), np.array(low), np.array(close), timeperiod=14)
  #data_input['CCI'] = ta.CCI(np.array(high), np.array(low), np.array(close), timeperiod=14)
  #data_input['TRIX'] = ta.TRIX(np.array(close), timeperiod=30)

  return data_input

def get_data_frame(stock_name, start_date, end_date):
  """Parameter"""
  write_csv = "source/"+stock_name+"_"+start_date+"_"+end_date+".csv"
  try:
    tushare_frame = pd.read_csv(write_csv)
    tushare_frame = tushare_frame.iloc[:,1:]
    print("Successfully read stock data from source "+write_csv)
  except:
    """ get data from tushare """
    tushare_frame = pro.daily(ts_code=stock_name+'.SH', start_date=start_date, end_date=end_date)
    tushare_frame.to_csv(write_csv)
  data_frame = data_frame.sort_index(axis=0, ascending=False)
  ext_frame  = featureExt(data_frame)
  """
    ts_code           601318.SH
    trade_date         20180330
    open                  66.01
    high                  66.27
    low                    64.8
    close                 65.31
    pre_close             66.39
    change                -1.08
    pct_chg               -1.63
    vol                  842023
    amount           5.4991e+06
    xclose                65.31
    Ret                -1.06045
    MA5_talib           69.844
    MA10_talib           69.844
    MA20_talib           69.844
    EMA12               67.2954
    EMA26                68.631
    MACD                -1.3356
    MACDsignal        -0.459368
    MACDhist          -0.876233
    RSI                 34.8054
    MOM                   -4.99
    K                   13.2834
    D                   12.0084
    J                   15.8334
    ATR                 2.46165
    OBV             5.53109e+07
    AD              2.33885e+06
    ADOSC               -210932
    UPPERBAND           69.2919
    MIDDLEBAND           66.708
    LOWERBAND           64.1241
    DEMA                68.6564
    EMA                 69.8662
    HT_TRENDLINE        70.2023
    KAMA                71.5414
    MA                  69.4157
    MIDPOINT               69.7
    MIDPRICE              70.11
    SAR                    94.3
    SAREXT                -94.3
    SMA                 69.4157
    T3                    69.77
    TEMA                67.8101
    TRIMA               70.0201
    WMA                 69.5408
    ADX                 17.0099
    Name: 0, dtype: object
  """
  date_frame = ext_frame.values
  close_data = date_frame[90:, 5]
  raw_data   = date_frame[90:, 2:]
  """ get the values of each data """
  raw_data   = raw_data.astype(np.float64)

  return raw_data, close_data
  
  
