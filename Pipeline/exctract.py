import pandas as pd

df1 = pd.read_csv('./Source/data1.csv')
df2 = pd.read_csv('./Source/data2.csv')
df3 = pd.read_csv('./Source/data3.csv')


combinedDataFrame = pd.concat([df1,df2,df3], ignore_index = False)

with open('./Staging_Area/staging_areaDB.csv','x') as file:
    combinedDataFrame.to_csv('./Staging_Area/staging_areaDB.csv')
    print('successfully extracted to staging area')