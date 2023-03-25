import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def load_housing_data():
    # Tải bộ dữ liệu về từ UCI Machine Learning Repository
    url = "D:/Users/duchuy/PycharmProjects/HocMay/lab1/housing.csv"
    return pd.read_csv(url)


# Tải bộ dữ liệu và hiển thị 5 dòng đầu tiên của DataFrame
housing = load_housing_data()

print("Mean price:", housing)

# housing.plot(kind="scatter", x="longitude", y="latitude")
#
# # Thêm tiêu đề và tên trục
# plt.title("Housing Prices")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.show()
#
#
# start = datetime.datetime(2010, 1, 1)
# end = datetime.datetime(2023, 2, 14)
# symbol = 'AAPL'
# data_source = 'yahoo'
#
# df = web.DataReader(symbol, data_source, start, end)
