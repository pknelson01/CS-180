import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [["M", "Brown", "Brown", "5'8\"", "160"],
        ["F", "Blonde", "Blue", "5'5\"", "110"],
        ["F", "Brown", "Blue", "4'0\"", "60"],
        ["M", "Blonde", "Brown", "4'8\"", "100"],
        [None, None, None, None, None],
        [None, None, None, None, None]]

x = pd.DataFrame(data, columns = ["Gender", "Hair Color", "Eye Color", "Height", "Weight (lbs)"], index = ["Parker", "Ava", "Margot", "Beckham", "Vincent", "Rory"])

x["Age"] = [36, 36, 6, 8, None, None]
x["Birth Year"] = 2037 - x["Age"]

# print(x)

x_sorted = x.sort_values(by = "Birth Year", ascending = True)

print(x_sorted)

# print(x.head())

# print(x.shape, "\n", x.columns, "\n", x.info(), "\n", x.describe())

# x['Age'].plot.hist()
# plt.show()

# print(x.loc['Parker' : 'Margot', 'Gender' : 'Eye Color'])
# print(x[x['Age'] > 10]) # return all data for those who are older than 10 years of age

print(x.isna().sum())

print(x["Age"].unique())

