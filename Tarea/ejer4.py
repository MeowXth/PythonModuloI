import random
n= int(input("Ingrese Tamaño de Vector"))
A=[]
for i in range(0,n):
    A.append(random.randint(1,100))
    
print(A)
total=0
for i in A:
    if i%3==0:
        total=total+i

print("El total de los multiplos de 3 es; ",total)
