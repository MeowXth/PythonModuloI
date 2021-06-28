from metodos import metodos as met
from collections import deque


print("***************************************")
print("************   Menu     ***************")
print("*                                     *")
print("*                                     *")
print("* 1.-Ejercicio 1                      *")
print("* 2.-Ejercicio 2                      *")
print("* 3.-Ejercicio 3                      *")
print("* 4.-Salir                            *")
while True:
    md=int(input("digite alguna opcion: "))
    if md == 1:
        listaprinc=[51,45,21,78,15 ,98,66,45,15,21]
        met.listF(listaprinc)

    if md == 2:
        x=[10,11,12,13,14]
        y=[20,30,40,50,60]
        met.listaM(x,y)
        
        
    if md ==3:
        cola = deque([])
        for i in range(0,5):
            num=int(input("Digite Num: "))
            cola.append(num)
        print(met.proce(cola))    
        
    if md >=4 or md == 0:
        break