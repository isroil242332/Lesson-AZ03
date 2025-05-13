import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных из 5 чисел
x = np.random.rand(5)
y = np.random.rand(5)

# Печать сгенерированных массивов
print("X:", x)
print("Y:", y)

# Создание диаграммы рассеяния
plt.scatter(x, y)

# Добавление заголовков и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение графика
plt.show()