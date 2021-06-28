def sumaListas(l1, l2):
    listaFinal=[]
    n=0
    while n<10:
        listaFinal.append(l1[n]+l2[n])
        n+=1
    return listaFinal    

listaNum_1=[10,20,30,40,50,60,70,80,90,100]
listaNum_2=[100,200,300,400,500,600,700,800,900,1000]

li=sumaListas(listaNum_1,listaNum_2)
print(li)