import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Функция для создания гистограммы
def draw_histogram(array, array_x):
    plt.bar(array_x, array)
    plt.show()


# Функция для определления максимально возможного расстояния
def calcul_max_lim_of_distance(dimension):
    return np.sqrt(dimension * 4)


# Функция проверки является ли данная пара векторов максимально удаленными
def check_max(distance, current_line, another_line, max_distance):
    if distance > max_distance['distance']:
        max_distance['distance'] = distance
        max_distance['first_vector'] = current_line
        max_distance['second_vector'] = another_line
    return max_distance


# Функция проверки является ли данная пара векторов минимально удаленными
def check_min(distance, current_line, another_line, min_distance):
    if distance < min_distance['distance']:
        min_distance['distance'] = distance
        min_distance['first_vector'] = current_line
        min_distance['second_vector'] = another_line
    return min_distance


# Функция для создания массива подсчёта расстояний
def create_array_of_distance(number_of_dimension):
    max_position = int(calcul_max_lim_of_distance(number_of_dimension) / 0.1)
    array_of_distance = np.zeros_like(np.empty(max_position, int))
    return array_of_distance


# Функция записи в массив подсчёта расстояний
def update_position_in_array(distance, array_of_distance):
    position_of_distance = int(round(distance, 1) * 10)
    array_of_distance[position_of_distance] += 1
    return array_of_distance

# Открываем файл и переводим его из DataFrame в массив NumPy
vectors = pd.read_csv('vectors.csv').to_numpy()

# Определяем размер массива
number_of_vectors = vectors.shape[0]
number_of_dimension = vectors.shape[1]

# Создаем массив подсчёта расстояний
array_of_distance = create_array_of_distance(number_of_dimension)

# Создаем словари записи максимальных и минимальных расстояний
max_distance = {
    'distance': 0.0,
    'first_vector': 0,
    'second_vector': 0
    }
min_distance = {
    'distance': calcul_max_lim_of_distance(number_of_dimension),
    'first_vector': 0,
    'second_vector': 0
    }

# Проводим рассчёт расстояний для всех пар векторов
for current_line in range(0, number_of_vectors):
    another_line = current_line + 1
    while another_line < number_of_vectors:
        distance = np.linalg.norm(vectors[current_line] - vectors[another_line])
        another_line += 1
        max_distance = check_max(distance, current_line, another_line, max_distance)
        min_distance = check_min(distance, current_line, another_line, min_distance)
        array_of_distance = update_position_in_array(distance, array_of_distance)

# Создаем маасив даных для отображения на оси х
array_for_axis_x = np.arange(0, int(calcul_max_lim_of_distance(number_of_dimension)) + 0.1, 0.1)

# Выводим результат
print('Расстояние между векторами {} и {} равно {} и оно максимально'.format(
    max_distance['first_vector'],
    max_distance['second_vector'],
    round(max_distance['distance'], 2)
))
print('Расстояние между векторами {} и {} равно {} и оно минимально'.format(
    min_distance['first_vector'],
    min_distance['second_vector'],
    round(min_distance['distance'], 2)
))
draw_histogram(array_of_distance, array_for_axis_x)
