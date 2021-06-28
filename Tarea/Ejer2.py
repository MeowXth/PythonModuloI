import random
n= int(input("Ingrese Tamaño del vector:"))
A=[]
for i in range(0,n):
    A.append(random.randint(1,100))

print(A)
men = A[0]
for i in A:
    if i<men:
        men=i

print("El menor es :",men)
