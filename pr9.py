#2-а
def m(a, b):
    return a if a < b else m(a - b, b)

a = int(input("a: "))
b = int(input("b: "))
print(m(a, b))

#2-б
def f():
    x = int(input())
    if x == 0:
        return (0,0)
    a, b = f()
    if x > a:
        return (x, a)
    if x < a and x > b:
        return (a, x)
    return (a, b)
r = f()
print(r[1])