import pandas as pd

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
df = pd.read_csv(url, header=None,
                 names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'], delimiter=',\s+')

# Chuyển đổi giá trị của cột 'class' thành số
df['class'] = df['class'].replace(['sepal_length', 'sepal_width', 'petal_length'], [0, 1, 2])

# Kiểm tra lại dữ liệu đã được số hóa
print(df.head())
