#1
n=int(input('Введите длину массива: '))
d=[] 
for i in range(n):
    print("Введите",i,"элемент:")
    d.append(int(input()))
s=sum(d[1::2])
print("Массив: ", d)
print("Сумма нечетных индексов: ", s)

#2
d1=[]
print("Введите 8 элементов") 
for i in range(8):
    print("Введите", i, "элемент:")
    n = int(input())
    if n < 15:
        n = n * 2
    d1.append(n)

print("Преобразованный массив: ", d1)