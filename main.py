from stock_data_fetcher import StockDataFetcher

"""
  使用TuShare获取股票数据。

  参数:
  - ts_code: 股票代码。
  - start_date: 数据开始日期，默认为'20110101'。
  - end_date: 数据结束日期，默认为'20200101'。
  - token: TuShare API令牌，默认从环境变量'TUSHARE_TOKEN'获取。
  - 000063.SZ 中兴通讯
  - 600000.SH 浦东发展银行 你原来的那个 000002.SH现在查不到, 我随便找了个替换下
  """


def first_problem(token, ts_codes=['000063.SZ', '600000.SH'], start_date='20110101', end_date='20200101',
                  save_paths=['./data/000063.SZ.csv', './data/600000.SH.csv']):
    fetcher = StockDataFetcher(token)

    for ts_code, save_path in zip(ts_codes, save_paths):
        data = fetcher.get_stock_data(ts_code, start_date, end_date)
        if data is not None:
            fetcher.save_data_to_csv(data, save_path)


if __name__ == '__main__':
    tushare_token = '6ce83125505f27b1cdf3a2d6d99fda0608a36c1d787ddb3d7fb9b90b'
    first_problem(tushare_token)
