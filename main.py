import pandas as pd

df = pd.read_csv('ZILL-Z77006_A.csv')
# print(df)

#print(df.head())
#print(df['Value'].head())

df['Value'].to_csv('newcsv3.csv')
df.set_index('Date', inplace=True)
print(df['Value'].head())

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df.columns = ['House Prices']

print(df.head())

df.to_csv('newcsv3.csv')

df.to_csv('newcsv4.csv', header=False)

df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'], index_col=0)
print(df.head())

df.to_html('example.html')

# Cargar y renombrar columnas
df = pd.read_csv('newcsv4.csv', names = ['Date','House_Price'])
print(df.head())

df.rename(columns={'House_Price':'Prices'}, inplace=True)
df.set_index('Date', inplace=True)
print(df.head())

