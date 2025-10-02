#1
a=[]
print("Введите 10 элементов") 
for i in range(10):
    print("Введите",i,"элемент:")
    a.append(int(input()))
m=max(a)
print('Максимальный элемент массива:',m)
b=0
n=0
for i in a:
    if i>m:
        b+=1
    elif i<m:
        n+=1
print("Кол-во больших максимального: ",b)
print("Кол-во меньших максимального: ",n)

#2
a1=[]
print("Введите 10 элементов") 
for i in range(10):
    print("Введите",i,"элемент:")
    a1.append(int(input()))
s = 0
for i in a1:
    if i > 5:
        s += i
print("Сумма чисел больше 5 = ", s)