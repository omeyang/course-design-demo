# stock_data_fetcher.py

import pandas as pd
import tushare as ts
import logging
import os


class StockDataFetcher:
    def __init__(self, token=os.getenv('TUSHARE_TOKEN')):
        self.token = token

    def get_stock_data(self, ts_code, start_date='20110101', end_date='20200101'):
        try:
            ts.set_token(self.token)
            pro = ts.pro_api()
            data = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
            data.set_index("trade_date", inplace=True)
            data.sort_index(inplace=True)
            data.index = pd.to_datetime(data.index)
            return data
        except Exception as e:
            logging.error(f"获取股票数据失败: {e}")
            return None

    @staticmethod
    def save_data_to_csv(data, save_path):
        # 检查目录是否存在，如果不存在，则创建
        directory = os.path.dirname(save_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            data.to_csv(save_path)
            logging.info(f"数据已保存到 {save_path}")
        except Exception as e:
            logging.error(f"保存数据失败: {e}")
