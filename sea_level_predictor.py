import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Cargar los datos
df = pd.read_csv('epa-sea-level.csv')

# Crear el diagrama de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Línea de mejor ajuste para todos los datos
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series([i for i in range(1880, 2051)])
plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Best Fit Line 1880-2050')

# Línea de mejor ajuste desde el año 2000
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(years_extended, intercept_recent + slope_recent * years_extended, 'g', label='Best Fit Line 2000-2050')

# Configurar etiquetas y título
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Guardar la figura
plt.savefig('sea_level_plot.png')
plt.show()
