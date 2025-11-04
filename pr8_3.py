#1
import random
n = int(input('Введите размер матрицы: '))
m = []
for i in range(n):
    m1 = []
    for j in range(n):
        m1.append(random.randint(0, 9))
    m.append(m1)
s = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            s = False
for m1 in m:
    print(m1)
if s==True:
    print("симметрична")
else:
    print("не симметрична")

#2
import random
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
a = []
for i in range(n):
    r = []
    for j in range(m):
        number = round(random.uniform(1.0, 10.0), 1)
        r.append(number)
    a.append(r)
print("Исходная матрица:")
for i in a:
    print(i)
mx = a[0][0]
for i in range(n):
    for j in range(m):
        if mx < a[i][j]:
            mx = a[i][j]
mi, mj = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] == mx:
            mi, mj = i, j
if mi != 0:
    a[0], a[mi] = a[mi], a[0]
if mj != 0:
    for i in range(n):
        a[i][0], a[i][mj] = a[i][mj], a[i][0]
print("Результат:")
for i in a:
    print(i)