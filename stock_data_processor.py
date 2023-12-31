import pandas as pd
import numpy as np


class StockDataProcessor:
    """
    股票数据处理类，用于读取和处理股票数据。
    """

    def prepare_stock_data(self, filepath, column='close'):
        """
        读取股票数据并计算对数收益率。

        :param filepath: 数据文件路径
        :param column: 要处理的列名，默认为收盘价 'close'
        :return: 对数收益率的Series对象
        """
        try:
            stock_data = pd.read_csv(filepath, index_col="trade_date")
            stock_data = stock_data.sort_values("trade_date")
            stock_return = np.log(stock_data[column] / stock_data[column].shift(1))
            return stock_return.dropna()
        except Exception as e:
            print(f"数据读取或处理出错: {e}")
            return None