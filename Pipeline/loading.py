import pandas as pd

df = pd.read_csv('./Staging_Area/staging_areaDB.csv')



with open('./Data_Warehouse/data_warehouse.csv','w') as file:
    df.to_csv('./Data_Warehouse/Data_Warehouse.csv', index=False)
    print('successfully loaded into data warehouse')

print(df.columns)