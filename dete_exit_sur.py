import pandas as pd
import numpy as np
import matplotlib as plt

#  view data xem chưa có cái gì
df = pd.read_csv('C:\\Users\\Admin\\Desktop\\AdPython\\dete-exit-survey-january-2014.csv')

print(df.info)
print(df.head())
print('\n\n\n')

# view data các cột xem có missing data ko
missing_data = df.isna()  # or df.isnull()
print(missing_data)

print()
# view value các cột xem có mising data ko
print(df['Classification'].value_counts())

# xem số lượng missing data
print(df.isnull().sum())

# bỏ những cột quá nhiều missịng data
to_drop_df = df.columns[50:]
df_update = df.drop(to_drop_df, axis = 1)
print(df_update.info())

# chuẩn hóa theo kiểu dữ liệu như sau: 'abc_def'\
df_update.columns = df_update.columns.str.lower().str.strip().str.replace(' ', '_')
print(df_update.info())

# gom giá trị của những tường tương tự thành Resignation
print(df_update['separationtype'].value_counts())

df_update['separationtype'] = df_update['separationtype'].str.split('-').str[0]
print(df_update['separationtype'].value_counts())

df_resignation = df_update[df_update['separationtype'] == 'Resignation'].copy 