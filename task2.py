

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

print("\n Data Cleaning")
data = {
    "Age": [25, 30, np.nan, 40, 1000],
    "Gender": ["Male", "Female", "Female", "Male", "Male"],
    "Salary": [50000, 60000, 55000, 52000, 500000]
}

df = pd.DataFrame(data)
df['Age'].fillna(df['Age'].mean(), inplace=True)
df = df[df['Age'] < 120]
df = df[df['Salary'] < 200000]
df['Gender'] = LabelEncoder().fit_transform(df['Gender'])
df[['Age', 'Salary']] = StandardScaler().fit_transform(df[['Age', 'Salary']])
print(df)

