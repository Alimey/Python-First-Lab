# -*- coding: utf-8 -*-
"""Копия блокнота "lab_1_np_pandas_matplotlib"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11TJd2cR2DdlX2OyD6W9N0cRh_p54-E4C
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random as rand

"""# 1. Разминка (4 балла)

## 1.1 Создание матриц (0.25 балла)

Создайте 4 матрицы
- A - "шахматную" из нулей и единиц, размера 6 на 3, левое верхнее значение (A[0][0]) равно 1,
- В - из чисел от 1 до 24, записанных в виде змейки, размера 6 на 4,
- C - из случайных целых чисел от 2 до 10 (обе границы включительно), размера 4 на 3
- D - из нулей с единичками на главной диагонали, размера 4 на 4.

**Создайте из этих матриц "лоскутную" матрицу S**

A В

С D

используя **только стандартные** операции numpy. Comprehensions использовать нельзя.

После этого допишите к полученной матрице S матрицу F размера 10 на 2 из нулей, чтобы получилась матрица G:

S F

P.S. Когда мы говорим, что матрица имеет размер x на y, x - количество строк, y - количество столбцов.
"""

A = np.zeros((6, 3), dtype = int);
A[::2, ::2] = 1
A[1::2, 1::2] = 1
print(A)

B = np.zeros((6, 4), dtype = int)
for i in range(6):
  for j in range(4):
    B[i][j] = i * 6 + j + 1
print(B)

C = np.zeros((4, 3), dtype = int)
for i in range(4):
  for j in range(3):
    C[i][j] = rand.randint(2, 10)
print(C)

D = np.zeros((4, 4), dtype = int)
for i in range(4):
  D[i][i] = 1
print(D)

S = np.block([[A, B], [C, D]])
print(S)

F = np.zeros((10, 2), dtype = int)
print(F)

G = np.block([S, F])
print(G)

# YOUR CODE HERE

"""## 1.2 Поиск ближайшего соседа (0.25 балла)

Реализуйте функцию, принимающую на вход матрицу X и некоторое число a и возвращающую ближайший к числу элемент матрицы.
Например, для X = np.arange(0,10).reshape((2, 5)) и a = 3.6 ответом будет 4. Можно пользоваться только базовыми функциями numpy, циклами пользоваться **нельзя**.
"""

def find_nearest_neighbour(X, a):
    index = np.abs(X - a).argmin()
    multi_index = np.unravel_index(index, X.shape)
    return X[multi_index]
find_nearest_neighbour(np.arange(0,10).reshape((2, 5)), 3.6)

"""## 1.3 Очень странная нейросеть (0.25 балла)

Реализуйте одну очень странную нейросеть. Нейросеть должна:

- Возводить матрицу A (матрицу весов) размера N x N в квадрат
- В качестве первого преобразования умножать вектор X длины N (вектор признаков) на матрицу весов A**2 (на выходе получается новый вектор);
- В качестве второго преобразования умножать вектор, полученный на прошлом шаге, на вектор b (вектор весов) размера N (на выходе получается скалярное число).

Считаем, что все числа (элементы матриц и векторов) - числа с плавающей точкой.
"""

# Придумайте свои данные для примера, N >= 4
A = np.random.uniform(low=1, high=10, size=(5, 5))
b = np.random.uniform(low=1, high=10, size=(5, 1))
X = np.random.uniform(low=1, high=10, size=(1, 5))

print(A)
print(b)
print(X)


def very_strange_neural_network(A, b, X):
    A = np.dot(A, A)
    X = np.dot(X, A)
    ANS = np.dot(X, b)
    return ANS[0][0]


print(very_strange_neural_network(A, b, X))

"""## 1.4 Джунгли зовут! (0.25 балла)

Перед вами матрица M - карта местности тяжелопроходимых джунглей, составленная Ларой Крофт. На карте каждая ячейка - целое число, обозначающее высоту над уровнем моря (если число больше нуля) в метрах или глубину моря (если число меньше нуля) в метрах в данной ячейке карты размером метр на метр. Если число 0, то это часть суши - берег.


Вам необходимо посчитать:
- Общую площадь клеточек моря, в которых его глубина больше 5 (в м^2)
- Общий объём всей воды на карте (в м^3)
- Максимальную высоту над уровнем моря, которая есть на этой карте (в м)
"""

def find_deep_sea_area(M):
    return np.sum(M < -5)
def find_water_volume(M):
    return -np.sum(M[M < 0])

def find_max_height(M):
    return np.max(M[M >= 0])

# Можно подставить свой пример
M = np.array([
    [-7, -3, -1, 0],
    [-4, -3, 1, 19],
    [-2, 0, 4, 25],
    [-1, 3, 6, 9]
])

# простая проверка для примера выше
assert np.isclose(find_deep_sea_area(M), 1)
assert np.isclose(find_water_volume(M), 21)
assert np.isclose(find_max_height(M), 25)

print("Общая площадь моря на карте -", find_deep_sea_area(M), "м^2")
print("Общий объем воды на карте -", find_water_volume(M), "м^3")
print("Максимальный уровень над уровнем моря на карте -", find_max_height(M), "м")

"""## 1.5 Острова сокровищ (0.25 балла)


На вход функции подаётся массив a из нулей и единиц. Необходимо посчитать, сколько в массиве есть блоков из идущих подряд единиц (островков). Можно пользоваться только базовыми функциями numpy, циклами пользоваться **нельзя**.

Подсказка: посмотрите, что такое `np.diff`
"""

def count_all_islands(a):
    differences = np.diff(a)
    starts = np.where(differences == 1)[0]
    if a[0] == 1:
        starts = np.insert(starts, 0, -1)
    return len(starts)

# можно подставить свой пример

a = np.array([0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1])

# простая проверка для примера выше
assert count_all_islands(a) == 4
print(count_all_islands(a))

"""## 1.6 Маскарад (0.25 балла)

На вход идёт 2-мерная матрица X, заполненная числами с плавающей точкой, и дробное число a. Нужно заменить все ячейки в матрице, которые больше, чем а, на среднее значение среди элементов матрицы Х.

**Нужно** пользоваться базовыми функциями numpy, **нельзя** пользоваться циклами.
"""

def swap_mask_for_average(X, a):
  mean = np.mean(X)
  X[X > a] = mean
  return X

# Можно подставить свой пример
M = np.array([
    [-7, -3, -1, 0],
    [-4, -3, 1, 19],
    [-2, 0, 4, 25],
    [-1, 3, 6, 9]
])
a = 5

# простая проверка для примера выше
assert np.allclose(swap_mask_for_average(M, a),
                   np.array([
                       [-7, -3, -1, 0],
                       [-4, -3, 1, 2],
                       [-2, 0, 4, 2],
                       [-1, 3, 2, 2]
                   ]))

swap_mask_for_average(M, a)

"""## 1.7 По горячим трейсам (0.25 балла)

На вход приходит квадратная матрица М, надо посчитать разницу между суммой по главной и побочной диагоналями матрицы.


Можно пользоваться только базовыми функциями numpy, циклами пользоваться **нельзя**.

Подсказка: посмотрите, что такое `np.trace`
"""

def count_trace_diff(M):
    main = np.trace(M)
    rest = np.trace(np.fliplr(M))
    return main - rest

# Можно подставить свой пример
M = np.array([
    [-7, -3, -1, 0],
    [-4, -3, 1, 19],
    [-2, 0, 4, 25],
    [-1, 3, 6, 9]
])

# простая проверка для примера выше
assert np.allclose(count_trace_diff(M), 3)

count_trace_diff(M)

"""## 1.8 Царь горы (0.25 балла)

На вход приходит вектор a размера N. Необходимо при помощи сложения, конкатенации, бродкастинга получить симметричную матрицу размера 2N x 2N, у которой в середине максимальное значение, а к краям оно убывает.

Пример: a = (0, 1, 2)

Результат:

0 1 2 2 1 0 \\
1 2 3 3 2 1 \\
2 3 4 4 3 2 \\
2 3 4 4 3 2 \\
1 2 3 3 2 1 \\
0 1 2 2 1 0 \\
"""

def create_mountain(a):
    N = len(a)
    first = a[:, None] + a[None, :]
    second = np.concatenate([first, first[::-1, :]], axis=0)
    ans = np.concatenate([second, second[:, ::-1]], axis=1)
    return ans

# Можно подставить свой пример
a = np.array([0, 1, 2])

create_mountain(a)

"""## 1.9 Монохромная фотография 9 на 12 (0.5 балла)

На вход приходит двухмерная матрица P размера N на M, заполненная числами от 0 до 255, соответствующая некой черно-белой фотографии и натуральное число C. Необходимо из неё получить матрицу размера (N-C + 1) x (M-C+1), где каждая ячейка - среднее значение соответствующей подматрицы размера C x C. Таким образом, по сути, мы сделаем примитивное размытие изображения (и немного потеряем в его размере)
"""

def custom_blur(P, C):
    rows, cols = P.shape
    smoothed = np.zeros((rows - C + 1, cols - C + 1))
    for i in range(rows - C + 1):
        for j in range(cols - C + 1):
            smoothed[i, j] = np.mean(P[i:i + C, j:j + C])
    return smoothed

# можно подставить свой пример
P = np.arange(0, 12).reshape((3, 4))
kernel = 2

# простая проверка для примера выше
assert np.allclose(custom_blur(P, kernel),
                   np.array([[2.5, 3.5, 4.5], [6.5, 7.5, 8.5]]))
custom_blur(P, 2 )

"""## 1.10 Функция проверки (0.75 балла)

На вход функции поступает произвольное (>2) кортежей размеров (shape) различных матриц. Необходимо вернуть True если можно последовательно сложить эти матрицы (возможно, с помощью broadcasting), и False если нет.
"""

def check_successful_broadcast(*matrices):
    pass

assert check_successful_broadcast((5, 6, 7), (6, 7), (1, 7))
# можно ещё потестировать на своих примерах

"""## 1.11 Попарные расстояния (0.75 балла)

На вход подаются матрицы A размера m x k и матрица B размера n x k. Нужно получить матрицу размера m x n, содержащую попарные евклидовы расстояния.

Можно пользоваться только базовыми функциями, нельзя пользоваться циклами, сторонними библиотеками; скорее всего, пригодится broadcasting. Авторское решение записывается **в одну строчку** в соответствии со всеми правилами кодстайла.
"""

def pairwise_distances(A, B):
  return np.sqrt(((A[:, np.newaxis] - B)**2).sum(axis=2))

m = 10
k = 5
n = 8

A = np.random.uniform(low=1, high=5, size=(m,k))
B = np.random.uniform(low=1, high=5, size=(n, k))

pairwise_distances(A, B)

"""Объясни принцип работы этой одной строчки. Что именно происходит в ней?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Сначала добавляется новая ось в A, матрица будто разворачивается таким образом, чтобы высоты k из обеих матриц стояли рядом
Потом A[...] - B использует broadcasting и "расширяет" матрицу вправо. получается куб m x n x k. Считаются разности м/д элементами.
Потом эти разницы возводятся в квадрат (**2 - поэлементное возведение), суммируются сверху вниз, т.е. получаются суммы разностей квадратов в количестве k штук. Потом из них извлекается корень и записывается в новую матрицу. Победа.

# 2. Обработка данных эксперимента (3 балла)

А сейчас, дамы и господа, мы научимся использовать библиотеки для анализа данных в реальности!

**Причина появления этого раздела проста**: многие студенты ПМФ даже во втором и третьем семестрах продолжают использовать Excel, калькулятор или лист бумаги. Хочется открыть глаза на ещё один способ выполнения лабораторных с намного меньшим порогом вхождения, чем тот же Excel. Авторы надеются, что кого-то это замотивирует присмотреться к удобным библиотекам.

*Спонсор данных для раздела - blacksamorez. Без него пять счастливых семестров лаб были бы совсем не счастливыми...*
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""##  2.1. Постановка задачи и данные

Предположим, у нас есть гироскоп с прицепленным к его оси грузом на рычаге (см. рисунок для быстрого понимания, а подробности можно узнать в [лабораторном практикуме](https://lib.mipt.ru/book/267519/), том 1, стр.160). Из-за наличия груза гироскоп начинает медленно [прецессировать](https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%B5%D1%86%D0%B5%D1%81%D1%81%D0%B8%D1%8F), т.е. вращаться вокруг вертикальной оси с какой-то более-менее постоянной частотой.

Мы с вами разберём часть этой лабораторной, в основном касающуюся обработки данных и построения графиков.

<center><img src='https://drive.google.com/uc?export=view&id=1KfYQ0hKYRDhi5uk7C8lNffZBNy8NF7nu' width=600>

Изображение гироскопа с подвешенным грузом Г и рычагом С</center>

Для начала посмотрим на данные, которые любезно кто-то для нас собрал. Создайте датафрейм из [файла](https://drive.google.com/file/d/1SbLR6R16obqLewUTnX1CAAjQTrVXh2Vq/view?usp=sharing)
"""

import os
os.system("curl https://raw.githubusercontent.com/aRTIKa-afk/mipt-py-data/refs/heads/main/data_numpy_lab.csv -o data_numpy_lab.csv")
data = pd.read_csv('./data_numpy_lab.csv')
data.head()

"""## 2.2 Работа с данными

Колонки в датафрейме следующие:

N - количество полных оборотов гироскопа в эксперименте;

t, в секундах - время эксперимента;

$\sigma_t$ - погрешность измерения времени;

mass - масса груза, подвешенного к рычагу на гироскопе;

length - длина плеча вышеупомянутого рычага;

phi - угол в радианах, на который опустился рычаг за время эксперимента. Понадобится, чтобы оценить влияние силы трения в гироскопе на прецессию.

Так как физики любят оперировать величинами адекватной размерности, нужно перевести колонки с массой в килограммы, а с длиной - в метры. Затем переименуйте все колонки так, чтобы в них не осталось упоминаний о размерности - только названия физических величин.
"""

data['mass, gramm'] /= 1000
data['length, cm'] /= 100
data.rename(columns={'Unnamed: 0' : 'Unnamed', 't, sec' : 't', 'sigma_t, sec' : 'sigma_t', 'mass, gramm' : 'mass', 'length, cm' : 'length', 'phi, rad' : 'phi'}, inplace=True)

assert data.mass.mean() < 0.3
assert np.allclose(data.length.mean(), 1.155)
assert all(' ' not in column for column in data.columns)

data.head()

"""Добавьте в датафрейм колонки с соответствующими именами и значениями, вычисленными по формулам:

`omega`: $\Omega = 2 \pi \cdot \frac{N}{t}$

`sigma_omega`: $\sigma_{\Omega} = \Omega / t \cdot \sigma_t$

`omega_down`: $\Omega_{down} = \varphi / t$

`sigma_down`: $\Omega_{down} \cdot \sigma_t / t$

`momentum`: $M = m \cdot g \cdot l$ (`g = 9.8 м/с^2`)

`momentum_down`: $M_{down} = m \cdot \frac{\varphi}{t^2} \cdot l^2$

`sigma_momentum`: $\sigma_{M} = M_{down} \cdot 2 \cdot \frac{\sigma_t}{t}$

"""

import math

data['omega'] = math.pi * 2 * data['N'] / data['t']
data['sigma_omega'] = data['omega'] / data['t'] * data['sigma_t']
data['omega_down'] = data['phi'] / data['t']
data['sigma_down'] = data['omega_down'] * data['sigma_t'] / data['t']
data['momentum'] = data['mass'] * 9.8 * data['length']
data['momentum_down'] = data['mass'] * data['phi'] / data['t'] / data['t'] * data['length'] * data['length']
data['sigma_momentum'] = data['momentum_down'] * 2 * data['sigma_t'] / data['t']

assert np.allclose(data.momentum_down.iloc[0], 5.892e-07)
assert np.allclose(data.sigma_omega[0:5], 3.5e-04, atol=3e-5)
assert np.allclose(data.sigma_momentum[0:5], 4.4e-09, atol=1e-9)

data.head()

"""Возможно, вы уже задались вопросом, для чего так много раз повторяются эксперименты с одной и той же массой. Чтобы получить более стабильные результаты, конечно же! Посчитайте теперь средние значения колонок `omega`, `sigma_omega`, `momentum` и`momentum_down` для каждой уникальной массы.

**Подсказка:** функция groupby вам поможет. Никаких циклов!
"""

grouped_data = data.groupby('mass').mean()

assert 0.273 in grouped_data.index
assert np.allclose(grouped_data.omega[0.273], 0.1433)

grouped_data

"""## 2.3 Простые графики и МНК

Теперь время для повторного знакомства с методом наименьших квадратов. Конечно же, мы не заставим вас писать МНК самостоятельно! <s>Мы же не звери</s>


В numpy функция [np.polyfit](https://numpy.org/devdocs/reference/generated/numpy.polyfit.html) по `x`, `y` и степени `p` вычисляет многочлен заданной степени, являющийся МНК-оценкой зависимости `y(x)`.

Функция [np.polyval](https://numpy.org/devdocs/reference/generated/numpy.polyval.html), в свою очередь, вычисляет многочлен `P(x)` по заданным коэффициентам.

Ваша задача - построить график зависимости $\Omega (M)$ угловой скорости от момента инерции. На графике должны присутствовать экспериментальные точки, а также прямая, построенная по методу наименьших квадратов. В легенду вынесите полином с записанными коэффициентами. Не забудьте подписать оси (14 шрифт), задать сетку и сделать правильный заголовок (18 шрифт)!

<center><img src='https://drive.google.com/uc?export=view&id=1xumON0195iA4HGSqvpS0FAhPGxuCdKH8' width=600>

Пример получившегося графика</center>
"""

omega_np = np.array(grouped_data.omega)
momentum_np = np.array(grouped_data.momentum)

coefs = np.polyfit(momentum_np, omega_np, 1)

x_lsq = np.linspace(momentum_np.min() * 0.5, momentum_np.max() * 1.1, 100)

y_lsq = np.polyval(coefs, x_lsq)

fig = plt.figure(figsize=(12, 8))

plt.plot(x_lsq, y_lsq, label=f'y = {coefs[0]} x + {coefs[1]}')
plt.scatter(momentum_np, omega_np, color='red')

plt.grid(True)

plt.ylabel('omega', fontsize=14)
plt.xlabel('momentum', fontsize=14)

plt.title('Graphic Omega(Mass)', fontsize=18)

plt.legend()

plt.show()

"""`np.polyfit` также умеет оценивать погрешности! Если точнее, он возвращает матрицу ковариаций для метода наименьших квадратов. Не будем углубляться в математику, главное знать, что на диагонали у неё стоят дисперсии полученных коэффициентов. Для получения собственно погрешности $\sigma$ необходимо взять корень из этих дисперсий.

Также стоит упомянуть про параметр `W`, задающий веса точек для оценки. Если известны ошибки $y_{error}$, можно задать веса как $W = 1 / y_{error}$, и прямая получится ещё более точной. Чтобы учесть ещё и ошибки по $x$, нужны, к сожалению, уже другие методы (но скорее всего, вам не понадобятся даже ошибки по $y$).

Представим, что произошла неприятность, и погрешности возросли в 10 раз!
"""

grouped_data['sigma_down'] *= 10
grouped_data['sigma_momentum'] *= 10

"""Теперь вам нужно нарисовать график зависимости $\Omega_{down} (M_{down})$ <b>(не $\Omega(M)$!)</b> для точек с крестами погрешностей, а также построить не только прямую по оценке наименьших квадратов, а ещё и учесть погрешности оценок коэффициентов! Т.е. нужно построить три прямых: $k \cdot x + b$, которую выдал МНК, $(k - \sigma_k) \cdot x + (b - \sigma_b)$, $(k + \sigma_k) \cdot x + (b + \sigma_b)$, и закрасить промежуток между этими прямыми (в этом вам поможет функция plt.fill_between). Остальное оформление оставьте таким же, как в предыдущем задании.

_Примечание: часто в МНК не смотрят на погрешность $b$, оставляя только $\sigma_k$._

<center><img src='https://drive.google.com/uc?export=view&id=1SriaMzJah7F610ocIK_O1-HqqtMQgxlg' width=600>

Пример получившегося графика</center>
"""

omega_down_np = np.array(grouped_data.omega_down)
momentum_down_np = np.array(grouped_data.momentum_down)

# Снова polyfit, но с дополнительным параметром и возвращающий ковариацию!
coefs, cov = np.polyfit(momentum_down_np, omega_down_np, 1, cov=True)

# Чтобы прямая построилась снова красиво
x_lsq = np.linspace(momentum_down_np.min() * 0.3, momentum_down_np.max() * 1.1, 100)

# Посчитайте корень диагональных элементов, должен получиться массив размером (2,)
lsq_stds = np.sqrt(np.diag(cov))

# Знакомый polyfit, но три раза
y_lsq = coefs[0] * x_lsq + coefs[1]
y_lsq_lower = (coefs[0] - lsq_stds[0]) * x_lsq + (coefs[1] - lsq_stds[1])
y_lsq_upper = (coefs[0] + lsq_stds[0]) * x_lsq + (coefs[1] + lsq_stds[1])

fig = plt.figure(figsize=(12, 8))

# YOUR CODE HERE
fig = plt.figure(figsize=(12, 8))

plt.plot(x_lsq, y_lsq, color='red', label=f'y = {coefs[0]} x + {coefs[1]}')
plt.plot(x_lsq, y_lsq_lower, color='red')
plt.plot(x_lsq, y_lsq_upper, color='red')

plt.fill_between(x_lsq, y_lsq_lower, y_lsq_upper, color='red', alpha=0.1)

plt.scatter(momentum_down_np, omega_down_np, color='blue')
plt.errorbar(momentum_down_np, omega_down_np, xerr=grouped_data.sigma_momentum, yerr=grouped_data.sigma_down, fmt='o', color='blue')

plt.ylabel('omega', fontsize=14)
plt.xlabel('momentum', fontsize=14)

plt.title('Graphic Omega(Mass)', fontsize=18)

plt.legend()

plt.grid(True)

plt.show()

"""# 3. Работа с датасетом (3 балла)

Датасет ирисов использовался в статье Р.А. Фишера 1936 года «Использование множественных измерений в таксономических задачах», а в наши дни часто используется начинающими аналитиками данных.

В наборе данных включены три вида ирисов по 50 образцов каждый, а также некоторые свойства каждого цветка. Один вид цветка линейно отделим от двух других, но два других не отделимы линейно друг от друга.

Столбцы в этом датасете:

Идентификатор (Id) \\
Длина чашелистика, см (SepalLengthCm) \\
Ширина чашелистика, см (SepalWidthCm) \\
Длина лепестка, см (PetalLengthCm) \\
Ширина лепестка, см (PetalWidthCm) \\
Вид (Species) \\

<font color='red'>ВНИМАНИЕ!</font> Все графики в этой части должны быть подписаны, а на осях должны быть подписи на русском языке.
"""

sns.set_style("darkgrid")

# Считайте csv в DataFrame pandas при помощи pd.read_csv
import os
os.system("curl https://huggingface.co/datasets/scikit-learn/iris/raw/main/Iris.csv -o iris.csv")
iris = pd.read_csv('./iris.csv')
iris.head()

# Понятно, что колонка Id нам не очень нужна
# Поэтому давайте её удалим - HINT: используйте метод drop

iris.drop(columns='Id', inplace=True)
iris.head()

"""Давайте проверим, сколько у нас разных видов ирисов в итоге - должно быть 3 по 50 штук каждый. Воспользуйтесь `value_counts` , чтобы посмотреть, какие есть возможные значения у колонки species."""

iris['Species'].value_counts()

"""## 3.1 Графики длины и ширины лепестка ириса

Давайте попробуем сравнить, связаны ли ширина и длина лепестков - воспользуйтесь `sns.scatterplot`, чтобы отобразить на оси OXY значения. Не забудьте подписать график и оси!
"""

graph = sns.scatterplot(x=iris.SepalLengthCm, y=iris.SepalWidthCm, hue=iris.Species)
graph.set(xlabel="Длинна лепестков, см", ylabel="Ширина лепестков, см")
plt.xlim(0, iris["SepalLengthCm"].max() * 1.1)
plt.ylim(0, iris["SepalWidthCm"].max() * 1.1)
plt.title("Зависимость ширины лепестков от длины")
plt.show()

"""Напишите, какие выводы можно сделать из графика. Чего графику не хватает, чтобы он был информативным?

<font color='red'>ВАШ ОТВЕТ ЗДЕСЬ</font>

Графику не хватает аппроксимирующих линий. Никаких точных выводов сделать нельзя, но с первого взгляда естественным образом возникает гипотеза, что длина и ширина линейно связаны друг с другом.

Давайте попробуем другие графики для тех же целей из библиотеки seaborn - `sns.jointplot`; кроме того, попробуйте выделить цветом точки на графике в зависимости от вида ириса - воспользуйтесь `sns.facetgrid`. В следующих ячейках выведите эти два графика и проанализируйте.
"""

graph = sns.jointplot(x=iris.SepalLengthCm, y=iris.SepalWidthCm, hue=iris.Species)
plt.xlabel("Длина лепестков, см")
plt.ylabel("Ширина лепестков, см")
plt.xlim(0, iris["SepalLengthCm"].max() * 1.1)
plt.ylim(0, iris["SepalWidthCm"].max() * 1.1)
plt.show()

graph = sns.FacetGrid(iris, col="Species", hue="Species", palette="bright")
graph.map(sns.scatterplot, "SepalLengthCm", "SepalWidthCm")
graph.set_axis_labels('Длина лепестков, см', 'Ширина лепестков, см')
plt.xlim(0, iris["SepalLengthCm"].max() * 1.1)
plt.ylim(0, iris["SepalWidthCm"].max() * 1.1)
plt.show()

"""Какие выводы можно сделать из этих графиков? Какой из 3 методов - scatterplot, jointplot, facetgrid вам кажется лучше?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Из графиков можно предполагать линейную зависимость, но тут нет никаких расчетов и недостаточно данных. Мне кажется, наиболее полезен scatterplot, так как все собрано в одном месте и нет лишней информации. В jointpoint не слишком полезное распределение плотности точек.

## 3.2 Графики распределений значений длины лепестка

Постройте график "ящика с усами" - `sns.boxplot` и его аналог - `sns.violinplot`. По оси Ox должны находиться возможные виды ирисов, по оси Oy.
"""

sns.boxplot(data=iris, x="Species", y="PetalLengthCm", hue="Species", palette="bright")
plt.xlabel('Виды')
plt.ylabel('Длина лепестков, см')

sns.violinplot(data=iris, x="Species", y="PetalLengthCm", hue="Species", palette="bright")
plt.xlabel('Виды')
plt.ylabel('Длина лепестков, см')

"""Сравните два вида графиков. Какой более информативный, а какой - более красивый визуально по вашему мнению? Какую информацию мы можем получить из этих графиков?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Более красивый визуально, конечно, второй. А вот что касается информативности, то первый проще анализировать. Из этих графиков мы можем получить максимальную, минимальную и среднюю длины лепестков, в каком диапазоне лежит большая часть значений.

Однако, возможно, из-за того, что второй строит параллельно еще и график распределения плотности точек, то в тех случаях, когда он нужен, сторой график будет полезнее.

## 3.3 Попарные графики взаимосвязи признаков


Давайте попробуем построить большую табличку из графиковв размера 4 на 4, где у нас находятся все возможные пары признаков (длина/ширина лепестка, длина/ширина чашелистика). Для этого воспользуйтесь `sns.pairplot` и не забудьте указать параметр `hue`.
"""

graph = sns.pairplot(
    data=iris,
    vars=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm',	'SepalWidthCm'],
    hue="Species",
    palette="bright"
)
translations = {
    "PetalLengthCm": "Длина лепестка, см",
    "PetalWidthCm": "Ширина лепестка, см",
    "SepalLengthCm": "Длина чашелистика, см",
    "SepalWidthCm": "Ширина чашелистика, см"
}
for ax in graph.axes.flatten():
    if ax.get_xlabel() in translations:
        ax.set_xlabel(translations[ax.get_xlabel()])
    if ax.get_ylabel() in translations:
        ax.set_ylabel(translations[ax.get_ylabel()])

"""Какую информацию о взаимосвязи признаков вы можете почерпнуть из полученного графика?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Ну, попробую предположить, что все зависит линейно от всего, хотя для iris-setosa это кажется сомнительным из-за наличия вертикальных / горизонтальных линий.

Какие графики находятся на диагонали этой таблицы?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Графики плотности распределения точек. diag_kind = kde

Попробуй заменить графики на диагонали таблицы на другие, возможно, более информативные (подсказка: в документации у `sns.pairplot` для этого есть специальный параметр). Выведи полученный график.
"""

graph = sns.pairplot(
    data=iris,
    vars=['PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm',	'SepalWidthCm'],
    hue="Species",
    palette="bright",
    diag_kind="hist"
)
translations = {
    "PetalLengthCm": "Длина лепестка, см",
    "PetalWidthCm": "Ширина лепестка, см",
    "SepalLengthCm": "Длина чашелистика, см",
    "SepalWidthCm": "Ширина чашелистика, см"
}
for ax in graph.axes.flatten():
    if ax.get_xlabel() in translations:
        ax.set_xlabel(translations[ax.get_xlabel()])
    if ax.get_ylabel() in translations:
        ax.set_ylabel(translations[ax.get_ylabel()])

"""Какие графики теперь находятся на диагонали таблицы? Получилось ли более информативно?

<font color='red'> ВАШ ОТВЕТ ЗДЕСЬ </font>

Теперь гистограммы. kde хороши тем, что дают более точные результаты, гистограммы - более обобщенные и легкие к восприятию. В зависимости от целей, одно лучше другого. А тут не знаю, зачем эти графики плотности вообще нужны.
"""