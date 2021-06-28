def buscarNombre(nombre,listaNom):
    res=False
    for nom in listaNom:
        if nom==nombre:
            res=True
        
    return res            




listaNombre=["Ana","Pedro","Ricardo","Maria","Sofia","Ernesto","Gonzalo","Felix","Roxana"]
nombre=input("Introduzca nombre ")
x=buscarNombre(nombre,listaNombre)
print(x)