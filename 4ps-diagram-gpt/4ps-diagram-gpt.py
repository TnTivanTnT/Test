import matplotlib.pyplot as plt

# Definir las 4 Ps y sus respectivos valores
ps = ['Producto', 'Precio', 'Plaza', 'Promoción']
valores = [4, 3, 2, 5]  # Puedes cambiar estos valores según lo necesites

# Crear el gráfico de barras
plt.bar(ps, valores, color=['blue', 'green', 'red', 'purple'])

# Agregar título y etiquetas
plt.title('Las 4 Ps del Marketing Mix')
plt.xlabel('P')
plt.ylabel('Valor')

# Mostrar el gráfico
plt.show()
