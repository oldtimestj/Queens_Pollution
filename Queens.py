#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
import pandas as pd
from pylab import plot
from matplotlib import *
import matplotlib.pylab as plt
df = pd.read_csv('pollution_us_2000_2016.csv')

del df['Unnamed: 0']

df = df.dropna()

"""
将清洗后的数据重新写入文件
"""
df.to_csv('pollution_us_2000_2016.csv')
df = pd.read_csv('pollution_us_2000_2016.csv')
del df['Unnamed: 0']
df[df['County'] == 'Queens']
df['Date Local'] = pd.to_datetime(df['Date Local'])
# print(type(df['Date Local']))
# print(df.info())

"""
取出县级名称为皇后镇2000年的数据
"""
df_Queens = df[df['County'] == 'Queens']

"""
取出皇后镇2000年的数据
"""
df_Queens_2000 = df_Queens[df_Queens['Date Local'].dt.year == 2000]

"""
绘制出二氧化氮的平均值变化曲线
"""
(df_Queens_2000['NO2 Mean'].groupby(df_Queens_2000['Date Local'].dt.month).mean()).plot(kind='line', figsize=[10,5],legend=True, title='NO2 Mean of Queens in 2000 ', grid=True)
plt.show()
"""
绘制出臭氧的平均值变化曲线
"""
(df_Queens_2000['O3 Mean'].groupby(df_Queens_2000['Date Local'].dt.month).mean()).plot(kind='line',figsize=[10,5],legend=True,title='o3 Mean of Queens in 2000',grid=False)
plt.show()
"""
绘制出二氧化硫的平均值变化曲线
"""
(df_Queens_2000['SO2 Mean'].groupby(df_Queens_2000['Date Local'].dt.month).mean()).plot(kind='line', figsize=[10,5], legend=True, title='SO2 Mean of Queens in 2000 ', grid=True)
plt.show()
"""
绘制出一氧化碳的平均值变化曲线
"""
(df_Queens_2000['CO Mean'].groupby(df_Queens_2000['Date Local'].dt.month).mean()).plot(kind='line', figsize=[10,5], legend=True, title='CO Mean of Queens in 2000 ', grid=True)
plt.show()

"""
绘制出二氧化氮2000~2016年的平均值变化曲线
"""
(df_Queens['NO2 Mean'].groupby(df_Queens['Date Local'].dt.year).mean()).plot(kind='line',figsize=[10,5],legend=True,title='NO2 Mean of Queens in 2000-2016',grid=True)
plt.show()

"""
绘制出臭氧2000~2016年的平均值变化曲线
"""
(df_Queens['O3 Mean'].groupby(df_Queens['Date Local'].dt.year).mean()).plot(kind='line', figsize=[10,5], legend=True, title='O3 Mean of Queens in 2000-2016 ', grid=True)
plt.show()

"""
绘制出二氧化硫2000~2016年的平均值变化曲线
"""
(df_Queens['SO2 Mean'].groupby(df_Queens['Date Local'].dt.year).mean()).plot(kind='line', figsize=[10,5], legend=True, title='SO2 Mean of Queens in 2000-2016 ', grid=True)
plt.show()
"""
绘制出一氧化碳2000~2016年的平均值变化曲线
"""
(df_Queens['CO Mean'].groupby(df_Queens['Date Local'].dt.year).mean()).plot(kind='line', figsize=[10,5], legend=True, title='CO Mean of Queens in 2000-2016 ', grid=True)
plt.show()
"""
取整即得AQI=158。各种污染物的AQI值分别算出来后，取数值最大的那个即为最终报告的AQI值。比如SO2浓度为20.5μg/m3，算出来对应的AQI为29；PM10浓度为150.8μg/m3，对应的AQI为98；PM2.5浓度为130.7μg/m3，对应的AQI为190。最终报告的AQI值就是190，而贡献了那个最大值的PM2.5则称为首要污染物。
"""

df_Queens['AQI'] = df_Queens[['NO2 AQI','O3 AQI','SO2 AQI','CO AQI']].apply(lambda x:max(x),axis=1)

def AQI_level(e):
    if e <= 50:
        return 'Good'
    elif e > 50 and e < 100:
        return 'Modrate'
    elif e > 100 and e < 150:
        return 'Unhealthy for Sensitive Groups'
    elif e > 150 and e < 120:
        return 'Unhealthy'
    elif e > 200 and e < 300:
        return 'Very Unhealthy'
    else:
        return 'Hazardous'

df_Queens['AQI_level'] = df_Queens['AQI'].map(AQI_level)
print(df_Queens['AQI_level'].head())
print(df_Queens['AQI_level'].value_counts())


df_Queens['AQI'].plot(kind='hist',figsize=[5,5],legend=False,title='AQI 2000-2016')
plt.show()
"""
画出各种类型比例的饼状图，发现效果直观
"""
df_Queens['AQI_level'].value_counts().plot(kind='pie',figsize=[5,5],counterclock=True,legend=False,autopct='%3.1f%%',title='AQI 2000-2016')
plt.show()