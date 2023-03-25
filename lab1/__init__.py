import pandas as pd

# Đọc tập dữ liệu từ file csv và lưu vào dataframe
housing_data = pd.read_csv('housing.csv')
mean_price1 = housing_data['total_rooms'].mean()
mean_price2 = housing_data['total_rooms'].median()
mean_price3 = housing_data['total_rooms'].mode()

print("Mean total_rooms:", mean_price1)
print("Median total_rooms:", mean_price2)
print("Mode total_rooms:", mean_price3)
