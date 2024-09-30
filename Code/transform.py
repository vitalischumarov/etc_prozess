import pandas as pd

df = pd.read_csv('./Staging_Area/staging_areaDB.csv')


#Delete id column
df = df.drop(columns=['ID'])


#Change column name
df = df.rename(columns={"Gehalt" : 'Gehalt / Jahr'})


#change column Gehalt im Jahr
df['Gehalt / Jahr'] = df['Gehalt / Jahr'].round(2)


#transform the date
df['Datum'] = pd.to_datetime(df['Datum'])
print('done')

