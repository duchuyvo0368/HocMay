import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('cancer.csv', header=None)

le = LabelEncoder()

for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
print(df.head())
