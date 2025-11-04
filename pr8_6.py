#1
import random
n = int(input('Введите размер матрицы: '))
m = []
for i in range(n):
    m1 = []
    for j in range(n):
        m1.append(random.randint(0,9))
    m.append(m1)
for m1 in m:
    print(m1)
r = []
for i in range(n):
    mx = m[i][0]
    for j in range(n):
        if m[i][j] > mx:
            mx = m[i][j]
    r.append(mx)
c = []
for j in range(n):
    mn = m[0][j]
    for i in range(n):
        if m[i][j] < mn:
            mn = m[i][j]
    c.append(mn)
for x in r:
    print(x, end=' ')
print()
for y in c:
    print(y, end=' ')
print()

#2
import random
n = int(input("Введите нечетный размер матрицы: "))
a = []
for i in range(n):
    r = []
    for j in range(n):
        number = round(random.uniform(1.0, 10.0), 1)
        r.append(number)
    a.append(r)
print("Исходная матрица:")
for i in a:
    print(i)
mx = a[0][0]
mi, mj = 0, 0
for i in range(n):
    if a[i][i] > mx:
        mx = a[i][i]
        mi = i
        mj = i
    j = n - 1 - i
    if a[i][j] > mx:
        mx = a[i][j]
        mi = i
        mj = j
c = n // 2
a[mi][mj], a[c][c] = a[c][c], a[mi][mj]
print("Результат:")
for i in a:
    print(i)