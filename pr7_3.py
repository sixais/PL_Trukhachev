#1
def g(x, y):
    return x**2+y**2
a1, b1 = map(float, input("Катеты первого треугольника a1, b1 = ").split())
a2, b2 = map(float, input("Катеты второго треугольника a2, b2 = ").split())
c1 = g(a1, b1) 
c2 = g(a2, b2)
if c1 == c2:
    print("Гипотенузы равны")
elif c1 > c2:
    print("Гипотенуза первого треугольника больше")
else:
    print("Гипотенуза второго треугольника больше")

#2
def g1(a):
    w = a.split()
    b = ""
    for w in w:
        b1 = ''.join(sorted(w))
        b += b1 + " "
    return b
c = input("Введите строку: ")
r = g1(c)
print("Результат:", r)