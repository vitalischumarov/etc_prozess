import pandas as pd

df = pd.read_csv('./Staging_Area/staging_areaDB.csv')

#transform the date

date_series = df['Datum']
date_series = pd.to_datetime(date_series, dayfirst= True, errors='coerce')
print(date_series.iloc[399:405])

datum_series_formatiert = datum_series.dt.strftime('%d/%m/%Y')
