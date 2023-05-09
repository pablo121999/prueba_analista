import pandas as pd

# Lee el archivo Excel en un dataframe de Pandas
df = pd.read_excel('archivo_a_transformar.xlsx')

# Define las funciones para transformar las columnas según las especificaciones
def transformar_anio(valor):
    return str(valor).zfill(4)

def transformar_concepto(valor):
    return str(valor).ljust(10, '$')

def transformar_valor(valor):
    return str(valor).zfill(20)

# Aplica las funciones de transformación a las columnas correspondientes
df['ANIO'] = df['ANIO'].apply(transformar_anio)
df['CONCEPTO'] = df['CONCEPTO'].apply(transformar_concepto)
df['VALOR'] = df['VALOR'].apply(transformar_valor)

# Genera el archivo de texto con los datos transformados
with open('archivo_txt.txt', 'w') as f:
    for index, row in df.iterrows():
        f.write(f"{row['ANIO']}{row['CONCEPTO']}{row['VALOR']}\n")

