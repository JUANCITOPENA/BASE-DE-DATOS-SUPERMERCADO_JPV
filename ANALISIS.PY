import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ruta del archivo de Excel
excel_file = r'C:\Users\TU_USUARIO\Desktop\TU_CARPETA\BASE DE DATOS SUPERMERCADO JPV CONVERSION\BASE DE DATOS DE SUPERMERCADO_JPV.xlsx'

# Cargar el archivo de Excel en un DataFrame de Pandas
df = pd.read_excel(excel_file)

# Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])

# Extraer el año de la fecha
df['Año'] = df['Fecha'].dt.year

# KPIs más relevantes
total_ventas = df['Precio Ventas'].sum()
ventas_por_producto = df.groupby('Nombre_Producto')['Cantidad'].sum().nlargest(5)
ventas_por_vendedor = df.groupby('Nombre_Vendedor')['Cantidad'].sum().nlargest(5)
promedio_precio_ventas = df['Precio Ventas'].mean()

# Crear gráficos de impacto
plt.figure(figsize=(18, 14))

# Gráfico 1: Ventas Totales Mensuales
ventas_mensuales = df.resample('M', on='Fecha')['Precio Ventas'].sum()
plt.subplot(3, 3, 1)
plt.plot(ventas_mensuales.index, ventas_mensuales.values, marker='o', linestyle='-', color='skyblue')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales ($)')
plt.title('Ventas Totales Mensuales')
plt.xticks(rotation=45)
plt.grid(True)

# Gráfico 2: Ventas por Producto (Top 5)
plt.subplot(3, 3, 2)
ventas_por_producto.plot(kind='bar', color='lightgreen')
plt.xlabel('Producto')
plt.ylabel('Cantidad Vendida')
plt.title('Ventas por Producto (Top 5)')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico 3: Ventas por Vendedor (Top 5)
plt.subplot(3, 3, 3)
ventas_por_vendedor.plot(kind='bar', color='lightcoral')
plt.xlabel('Nombre del Vendedor')
plt.ylabel('Cantidad Vendida')
plt.title('Ventas por Vendedor (Top 5)')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico 4: Distribución de Precios de Ventas
plt.subplot(3, 3, 4)
sns.histplot(df['Precio Ventas'], bins=20, kde=True, color='salmon')
plt.xlabel('Precio de Ventas ($)')
plt.ylabel('Frecuencia')
plt.title('Distribución de Precios de Ventas')

# Gráfico 5: Promedio de Precio de Ventas por Mes
ventas_promedio_mes = df.resample('M', on='Fecha')['Precio Ventas'].mean()
plt.subplot(3, 3, 5)
plt.plot(ventas_promedio_mes.index, ventas_promedio_mes.values, marker='o', linestyle='-', color='orange')
plt.xlabel('Fecha')
plt.ylabel('Precio Promedio de Ventas ($)')
plt.title('Promedio de Precio de Ventas por Mes')
plt.xticks(rotation=45)
plt.grid(True)

# Gráfico 6: Cantidad de Productos Vendidos por Categoría
plt.subplot(3, 3, 6)
categorias_productos = df.groupby('Nombre_Producto')['Cantidad'].sum().sort_values(ascending=False).index[:10]
df_categorias = df[df['Nombre_Producto'].isin(categorias_productos)]
sns.countplot(y='Nombre_Producto', data=df_categorias, palette='viridis', order=categorias_productos)
plt.xlabel('Cantidad Vendida')
plt.ylabel('Producto')
plt.title('Cantidad de Productos Vendidos por Categoría')

# Gráfico 7: Ventas por Nombre de Cliente (Top 10)
plt.subplot(3, 3, 7)
ventas_por_cliente = df.groupby('Nombre_Cliente')['Cantidad'].sum().nlargest(10)
ventas_por_cliente.plot(kind='bar', color='skyblue')
plt.xlabel('Nombre del Cliente')
plt.ylabel('Cantidad Vendida')
plt.title('Ventas por Nombre de Cliente (Top 10)')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico 8: Ventas por Región del Vendedor
plt.subplot(3, 3, 8)
ventas_por_region = df.groupby('Region_Vendedor')['Cantidad'].sum().sort_values(ascending=False)
ventas_por_region.plot(kind='bar', color='lightgreen')
plt.xlabel('Región del Vendedor')
plt.ylabel('Cantidad Vendida')
plt.title('Ventas por Región del Vendedor')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Gráfico 9: Ventas Totales por Año
ventas_por_año = df.groupby('Año')['Precio Ventas'].sum()
plt.subplot(3, 3, 9)
plt.bar(ventas_por_año.index, ventas_por_año.values, color='gold')
plt.xlabel('Año')
plt.ylabel('Ventas Totales ($)')
plt.title('Ventas Totales por Año')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Ajustar diseño para evitar solapamiento
plt.tight_layout()
plt.show()

# Tarjetas con KPIs relevantes
print(f"Total de Ventas: ${total_ventas:.2f}")
print("\nVentas por Producto (Top 5):")
print(ventas_por_producto)
print("\nVentas por Vendedor (Top 5):")
print(ventas_por_vendedor)
print(f"\nPromedio de Precio de Ventas: ${promedio_precio_ventas:.2f}")
