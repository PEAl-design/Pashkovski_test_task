import numpy as np
import pandas as pd

# Запрашиваем начальные данные
number_of_vectors = int(input("Введите количестов векторов (500 < N <= 1000):"))
number_of_dimension = int(input("Введите мерность веткора (10 < m <= 50):"))

# Создаем DataFrame
vectors = pd.DataFrame(np.random.randint(-1, 1, size=(number_of_vectors, number_of_dimension)))

# Сохраняем данные в файл vectors.csv
vectors.to_csv('vectors.csv', index=False)
