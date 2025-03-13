import pandas as pd

ruta_archivo = "C:/Users/jfran/OneDrive/Documentos/ventas.xlsx"

# Carguemos el archivo en un data frame
df = pd.read_excel(ruta_archivo)

# Ver las primeras filas del archivo 
print(df.head())