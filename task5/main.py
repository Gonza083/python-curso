import pandas as pd

# Leer archivo Excel
df = pd.read_excel('archivo_excel.xlsx')

# Escribir archivo CSV
df.to_csv('archivo_csv.csv', index=False)