'''
lista = [10,20,30,40,50,60,70,80,90,100]
tupla = (10,20,30,40,50,60,70,80,90,100)
print(type(lista))
print(lista)
print(type(tupla))
print(tupla)
'''
nombres1=tuple()
nombres2=("jose",)
nombre3=("ana",10,10.5,False,[1,2,3,4,[111,22]])
tupla = (10,20,30,40,50,60,70,80,90,100)
print(type(nombres2))
for dato in nombre3:
    print(dato)
x=nombre3[4][4][1] 
print(x)   