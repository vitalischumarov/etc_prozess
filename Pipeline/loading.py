import pandas as pd

df = pd.read_csv('./Staging_Area/staging_areaDB.csv')

with open('./Data_Warehouse/data_warehouse.csv','x') as file:
    df.to_csv('./Data_Warehouse/Data_Warehouse.csv')
    print('successfully loaded into data warehouse')