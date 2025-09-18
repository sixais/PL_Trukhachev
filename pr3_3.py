a=int(input("От "))
b=int(input("До "))
for i in range(a,b-1,-1):
    if i%2!=0:
        print(i)