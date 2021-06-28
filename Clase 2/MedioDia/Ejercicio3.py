def suma(n1,n2):
    r=n1+n2
    return r
def respuesta (resulta):
    if resulta > 100:
        res=""
        res=str(resulta)+" Si es mayor"     #res=resulta," Si es mayor"
    else:
        res=str(resulta)+" No es mayor"     #res=resulta," No es mayor"
    return res

def imprimir(r):
    print(r)        



imprimir(respuesta(suma(20,100)))