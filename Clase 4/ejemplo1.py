
def sumaListas(a,b):
    listaFinal=list()
    n=0
    while n<len(a):
        listaFinal.append(a[n]+b[n])
        n+=1
        
    return listaFinal
    print(listaFinal)
def parImparLista(a):
    for i in a:
        if i% 2==0:
            print("par")
        else:
            print("impar")    






lista1=[1,2,3,45,6]
lista2=[10,20,30,40,50]

sumaListas(lista1,lista2)

parImparLista(sumaListas(lista1,lista2))