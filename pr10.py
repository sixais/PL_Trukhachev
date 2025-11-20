#1
with open('ТрухачевАндрейДмитриевич_УБ51_vvod1.txt', 'r') as f:
    m = []
    for l in f:
        r = []
        for x in l.split():
            r.append(int(x))
        m.append(r)
n = len(m)
s = True
for i in range(n):
    for j in range(n):
        if m[i][j] != m[j][i]:
            s = False
with open('ТрухачевАндрейДмитриевич_УБ51_vivod1.txt', 'w') as f:
    for r in m:
        for n in r:
            f.write(str(n) + ' ')
        f.write('\n')
    if s:
        f.write("симметрична")
    else:
        f.write("не симметрична")

#2
with open('ТрухачевАндрейДмитриевич_УБ51_vvod2.txt', 'r') as f:
    a = []
    for l in f:
        r = []
        for x in l.split():
            r.append(float(x))
        a.append(r)
n = len(a)
m = len(a[0])
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
with open('ТрухачевАндрейДмитриевич_УБ51_vivod2.txt', 'w') as f:
    for r in a:
        for n in r:
            f.write(str(n) + ' ')
        f.write('\n')