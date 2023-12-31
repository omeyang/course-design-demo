
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from stock_data_processor import StockDataProcessor

class StockAnalysis:
    """
    股票分析类，用于分析股票之间的关系并进行可视化。
    """

    def __init__(self):
        self.processor = StockDataProcessor()

    def analyze_stock_relationship(self, zs_file, zx_file):
        """
        分析两只股票的收益率关系。

        :param zs_file: 上海证券交易所指数数据文件
        :param zx_file: 中兴通讯股票数据文件
        """
        zs_ret = self.processor.prepare_stock_data(zs_file)
        zx_ret = self.processor.prepare_stock_data(zx_file)

        if zs_ret is None or zx_ret is None:
            return

        data = pd.merge(pd.DataFrame(zs_ret), pd.DataFrame(zx_ret), left_index=True, right_index=True)
        model = self.linear_regression(data.iloc[:, 0], data.iloc[:, 1])
        print(model.summary())

        self.plot_data(data.iloc[:, 0], data.iloc[:, 1], "zs_ret", "zx_ret", "散点图和拟合直线")
        self.plot_residuals(model)

    def linear_regression(self, x, y):
        """
        执行一元线性回归分析。

        :param x: 自变量数据
        :param y: 因变量数据
        :return: 回归模型对象
        """
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        return model

    def plot_data(self, x, y, x_label, y_label, title):
        """
        绘制散点图和拟合直线。

        :param x: x轴数据
        :param y: y轴数据
        :param x_label: x轴标签
        :param y_label: y轴标签
        :param title: 图表标题
        """
        plt.scatter(x, y)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.show()

    def plot_residuals(self, model):
        """
        绘制拟合值和残差的散点图。

        :param model: 线性回归模型对象
        """
        plt.scatter(model.fittedvalues, model.resid)
        plt.xlabel("拟合值")
        plt.ylabel("残差")
        plt.title("拟合值和残差的散点图")
        plt.show()
