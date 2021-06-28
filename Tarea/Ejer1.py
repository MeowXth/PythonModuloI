n = int(input("Ingrese Tamaño de Vector: "))
A = []
for i in range(0,n):
    num=int(input("Digite Num: "))
    A.append(num)

print(A)
may=0
for i in A:
    
    if i> may:
        may=i

print("El mayor es :",may)        





