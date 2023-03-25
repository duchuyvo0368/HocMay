import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

url = "D:/Users/duchuy/PycharmProjects/HocMay/lab3/housing.csv"
data = pd.read_csv(url, header=None)
print(data.head(10))

data1 = {'name': ['Alice', 'Bob', 'Charlie', 'Dave'],
         'age': [25, 20, np.nan, 30],
         'gender': ['F', 'M', 'M', 'M'],
         'income': [50000, 60000, 40000, np.nan]}

df = pd.DataFrame(data1)
mean_age = df['age'].mean()
mean_income = df['income'].mean()
df['age'].fillna(mean_age, inplace=True)
df['income'].fillna(mean_income, inplace=True)

print(df)
gender_map = {'F': 0, 'M': 1}
df['gender'] = df['gender'].map(gender_map)
print(df)

data = pd.read_csv(url, header=None)

# Tách biến độc lập và biến phụ thuộc
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Tách tập huấn luyện và tập kiểm tra với tỷ lệ 80-20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# In số lượng mẫu trong mỗi tập
print("Tập huấn luyện có", len(X_train), "mẫu")
print("Tập kiểm tra có", len(X_test), "mẫu")

model = LinearRegression()

# danh sách các biến độc lập
independent_vars = ['x1', 'x2', 'x3', 'x4', 'x5']

# fit model lần lượt cho từng biến độc lập
for var in independent_vars:
    # tạo tập train và test với biến độc lập hiện tại
    X_train = train_df[var].values.reshape(-1, 1)
    y_train = train_df['dependent_var'].values.reshape(-1, 1)
    X_test = test_df[var].values.reshape(-1, 1)
    y_test = test_df['dependent_var'].values.reshape(-1, 1)

    # fit model cho biến độc lập hiện tại
    model.fit(X_train, y_train)

    # in ra kết quả trên tập test
    y_pred = model.predict(X_test)
    print('Results for independent variable', var)
    print('R-squared:', model.score(X_test, y_test))
    print('Coefficients:', model.coef_)
    print('Intercept:', model.intercept_)
    print('-------------------------')
