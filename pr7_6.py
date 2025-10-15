#1
def g(a, b):
    while b != 0:
        a, b = b, a % b
    return a  
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("НОД: ",g(a,b))
print("НОК: ",(a * b) // g(a,b))

#2
import math
def g(ab, bc, cd, ad, ac):
    p1 = (ab + bc + ac) / 2
    p2 = (ad + cd + ac) / 2
    s1 = math.sqrt(p1*(p1-ab)*(p1-bc)*(p1-ac))
    s2 = math.sqrt(p2*(p2-ad)*(p2-cd)*(p2-ac))
    s3 = s1+s2
    return s3
ab = int(input('Введите длину стороны AB '))
bc = int(input('Введите длину стороны BC '))
cd = int(input('Введите длину стороны CD '))
ad = int(input('Введите длину стороны AD '))
ac = int(input('Введите длину диагонали AC '))
a = g(ab, bc, cd, ad, ac) 
print(a)