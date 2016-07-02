params={}
Globals=[]
dataSource={}
algo={}
#-------------------------------------------------------------------------------------------
# 0)自定义数据获取参数

dataSource['dataProvider']='tushare'
dataSource['storageFormat']='mongodb'

dataSource['symbol']='600028'
dataSource['dateStart']='2015-12-21'
dataSource['dateEnd']='2015-12-24'
dataSource['dataPeriod']='D'

# 1)自定义zipline运行参数
# 1.1)简单类型参数
# 1.1.1)用户未自定义sim_params对象参数时，系统内部将以以下三参数作为参数生成sim_params
#       如果用户有自定义sim_params对象参数，系统内部将使用sim_params的定义，而丢弃以下三值
from datetime import datetime
import pytz
import pandas as pd
algo['capital_base']=1000
algo['start'] = datetime(2015, 12, 27,1,30 ,tzinfo=pytz.timezone('utc')) # set Shanghai to utc time
algo['end'] = datetime(2015, 12, 30,7,0, tzinfo=pytz.timezone('utc'))

algo['instant_fill']=True
algo['data_frequency'] = 'daily'  #data_frequency == 'minute'
# 1.2)交易日历指定
from TradingCalendar import shTradingCalendar
tradingcalendar = shTradingCalendar


# 1.3)交易环境指定
'''mid
TradingEnvironment()类定义交易的环境，包括：
1.交易日历(哪天交易，哪天不交易)
2.交易基准数据，包括指数回报，国债回报
3.交易所时区

这些环境数据若不自定义，系统会默认使用纽交所的数据，而且是实时下载，数据来源有两个，
若有一个连接不可用时，会导致无限等待。
所以，这个东西有必要自定义
另外，若要应用到中国市场，这些数据也必须要自定义
'''
from zipline.finance.trading import TradingEnvironment
from loaders.yahooLoader import load_market_data
algo['env']=TradingEnvironment(load=load_market_data,
                               #bm_symbol='000001',
                               exchange_tz="Asia/Shanghai",
                               max_date=None,
                               env_trading_calendar = tradingcalendar,
                               asset_db_path=':memory:') 

# 1.4)参数对象设定
from zipline.utils.factory import create_simulation_parameters
algo['sim_params'] = create_simulation_parameters(year=2015,             # start and end overwrites year
                                                  capital_base=1000,
                                                  start = algo['start'],
                                                  end=algo['end'],       # mid end overwrites num_days
                                                  env=algo['env'],
                                                  #num_days=None,
                                                  data_frequency='daily',
                                                  emission_rate='daily'
                                                  )
#-------------------------------------------------------------------------------------------    
params['dataSource'] = dataSource
params['algo'] = algo  