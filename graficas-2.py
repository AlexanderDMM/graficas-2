import pandas as pd
import matplotlib.pyplot as plt

# Crear el DataFrame con los datos proporcionados
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia',
                'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Sí', 'No', 'Sí', 'Sí']
}

df = pd.DataFrame(data)

# Gráfica 1: Boxplot de la distribución de notas
plt.figure(figsize=(8, 6))
plt.boxplot(df['nota'], vert=False)
plt.title('Distribución de Notas de Estudiantes')
plt.xlabel('Nota')
plt.show()

# Gráfica 2: Pie chart de la distribución de aprobados
aprobados_counts = df['aprobado'].value_counts()
labels = aprobados_counts.index
colors = ['green', 'red']

plt.figure(figsize=(8, 8))
plt.pie(aprobados_counts, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Proporción de Estudiantes Aprobados y No Aprobados')
plt.show()