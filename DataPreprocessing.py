import pandas as pd

data = pd.DataFrame({
    'A': [1, 2, None, 4, 5],
    'B': ['apple', 'banana', 'cherry', 'date', 'egg'],
    'C': [0.1, 0.2, 0.3, 0.4, None]
})

data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)

data = pd.get_dummies(data, columns=['B'], drop_first=True)

data['A'] = (data['A'] - data['A'].min()) / (data['A'].max() - data['A'].min())

Q1 = data['C'].quantile(0.25)
Q3 = data['C'].quantile(0.75)
IQR = Q3 - Q1
data['C'] = data['C'].clip(lower=Q1 - 1.5 * IQR, upper=Q3 + 1.5 * IQR)

data['C'] = (data['C'] - data['C'].mean()) / data['C'].std()

print(data)
