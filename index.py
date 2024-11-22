# import pandas as pd
# import matplotlib.pyplot as plt
# import mpld3


# # Cargar el archivo CSV
# df = pd.read_csv('covid_data.csv')

# # Convertir la columna 'Fecha' a tipo datetime
# df['Fecha'] = pd.to_datetime(df['Fecha'])

# # Graficar los casos confirmados, recuperados y fallecidos
# plt.figure(figsize=(10, 6))
# plt.plot(df['Fecha'], df['Casos Confirmados'], label='Casos Confirmados', marker='o')
# plt.plot(df['Fecha'], df['Recuperados'], label='Recuperados', marker='s')
# plt.plot(df['Fecha'], df['Fallecidos'], label='Fallecidos', marker='^')
# plt.plot(df['Fecha'], df['Activos'], label='Casos Activos', marker='x')

# # Etiquetas y título
# plt.title('Análisis de COVID-19')
# plt.xlabel('Fecha')
# plt.ylabel('Número de Personas')
# plt.legend()
# plt.grid(True)

# # Mostrar la gráfica
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('covid_data.csv')

# Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Graficar los casos confirmados, recuperados, fallecidos y activos
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Casos Confirmados'], label='Casos Confirmados', marker='o')
plt.plot(df['Fecha'], df['Recuperados'], label='Recuperados', marker='s')
plt.plot(df['Fecha'], df['Fallecidos'], label='Fallecidos', marker='^')
plt.plot(df['Fecha'], df['Activos'], label='Casos Activos', marker='x')

# Etiquetas y título
plt.title('Tendencias del COVID-19')
plt.xlabel('Fecha')
plt.ylabel('Número de Personas')
plt.legend()
plt.grid(True)

# Guardar el gráfico como imagen PNG
plt.savefig('grafico_covid.webp')

print("Gráfico guardado como 'grafico_covid.webp'")


