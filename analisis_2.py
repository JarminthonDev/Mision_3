import pandas as pd
import matplotlib.pyplot as plt

# Crear un dataframe con los datos proporcionados
data = {
    'Fecha': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05', '2023-10-06', '2023-10-07', '2023-10-08', 
              '2023-10-09', '2023-10-10', '2023-10-11', '2023-10-12', '2023-10-13', '2023-10-14', '2023-10-15', '2023-10-16', 
              '2023-10-17', '2023-10-18', '2023-10-19', '2023-10-20', '2023-10-21', '2023-10-22', '2023-10-23', '2023-10-24', 
              '2023-10-25', '2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29', '2023-10-30', '2023-10-31', '2023-11-01', 
              '2023-11-02', '2023-11-03', '2023-11-04', '2023-11-05', '2023-11-06', '2023-11-07', '2023-11-08', '2023-11-09', 
              '2023-11-10', '2023-11-11', '2023-11-12', '2023-11-13', '2023-11-14', '2023-11-15'],
    'Casos Confirmados': [12000, 12100, 12250, 12400, 12550, 12700, 12850, 13000, 13200, 13350, 13500, 13600, 13800, 14000, 
                           14150, 14300, 14450, 14600, 14750, 14900, 15050, 15200, 15350, 15500, 15650, 15800, 15950, 16100, 
                           16250, 16400, 16550, 16700, 16800, 16950, 17100, 17250, 17400, 17550, 17700, 17850, 18000, 18150, 
                           18300, 18450, 18600, 18750],
    'Recuperados': [10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 
                    11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 
                    13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 
                    14700, 14800, 14900, 15000],
    'Fallecidos': [700, 710, 715, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 
                   890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 
                   1080, 1090, 1100, 1110, 1120, 1130, 1140],
}

df = pd.DataFrame(data)
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Gráfico de líneas
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Casos Confirmados'], label='Casos Confirmados', color='blue', marker='o')
plt.plot(df['Fecha'], df['Recuperados'], label='Recuperados', color='green', marker='o')
plt.plot(df['Fecha'], df['Fallecidos'], label='Fallecidos', color='red', marker='o')

plt.title('Evolución de Casos Confirmados, Recuperados y Fallecidos')
plt.xlabel('Fecha')
plt.ylabel('Cantidad')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

#-------------------------------------------------------------------------------
# Guardar la imagen
plt.savefig('evolucion_casos.png', bbox_inches='tight')
plt.show()


# Gráfico de líneas para la tasa de mortalidad
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Tasa de Mortalidad (%)'], color='purple', marker='o')

plt.title('Tasa de Mortalidad a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Tasa de Mortalidad (%)')
plt.grid(True)
plt.xticks(rotation=45)

#-------------------------------------------------------------------------------
# Guardar la imagen
plt.savefig('tasa_mortalidad.png', bbox_inches='tight')
plt.show()

# Gráfico de líneas para los casos por millón
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Casos por Millón'], color='orange', marker='o')

plt.title('Casos por Millón de Habitantes')
plt.xlabel('Fecha')
plt.ylabel('Casos por Millón')
plt.grid(True)
plt.xticks(rotation=45)

# Guardar la imagen
plt.savefig('casos_por_millon.png', bbox_inches='tight')
plt.show()



#-------------------------------------------------------------
# Gráfico de líneas para los casos activos
plt.figure(figsize=(12, 6))
plt.plot(df['Fecha'], df['Activos'], color='brown', marker='o')

plt.title('Casos Activos a lo largo del tiempo')
plt.xlabel('Fecha')
plt.ylabel('Casos Activos')
plt.grid(True)
plt.xticks(rotation=45)

# Guardar la imagen
plt.savefig('casos_activos.png', bbox_inches='tight')
plt.show()


#---------------------------
# Proporción de casos recuperados y fallecidos
recuperados_totales = df['Recuperados'].iloc[-1]
fallecidos_totales = df['Fallecidos'].iloc[-1]
proporciones = [recuperados_totales, fallecidos_totales]
labels = ['Recuperados', 'Fallecidos']

plt.figure(figsize=(8, 8))
plt.pie(proporciones, labels=labels, autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'red'])
plt.title('Proporción de Recuperados vs Fallecidos')

# Guardar la imagen
plt.savefig('proporcion_recuperados_fallecidos.png', bbox_inches='tight')
plt.show()

