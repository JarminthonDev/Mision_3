
# import csv

# with open('BD_mision_3.csv', mode='r', newline='', encoding='utf-8') as file:
#     csv_reader = csv.reader(file)
        
    # for row in csv_reader:
    #     print(row)

import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV, asegurándose de usar una codificación adecuada
df = pd.read_csv('BD_mision_3.csv', encoding='utf-8-sig')

# Limpiar los nombres de las columnas (quitar espacios y caracteres extraños)
df.columns = df.columns.str.strip()

# Verificar los nombres de las columnas
print(df.columns)

# Ahora puedes usar la columna 'FECHA' correctamente (mayúsculas)
plt.plot(df['FECHA'], df['INGRESO_SIN_RESTRICCI�N'], label='Ingresos sin restricción', color='b', marker='o')

# Etiquetas y título
plt.xlabel('Fecha')
plt.ylabel('Ingresos sin restricción')
plt.title('Ventas a lo largo del tiempo')

# Mostrar el gráfico
plt.legend()
plt.xticks(rotation=45)
plt.show()
