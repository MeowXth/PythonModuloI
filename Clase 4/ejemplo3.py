diccionario=dict()
diccionario_2=dict(nom='jose', ed=25)
diccionario={'nombre' :"Gonzalo",'edad':32,'estatura':1.75, 'Cursos':{'python','android','java','dart'}}
#print(type(diccionario))
#print(diccionario['edad'])
'''
for claves in diccionario:
    print(claves," :", diccionario[claves])

print(diccionario_2)
lista=[100,200,300,400,500]
claves="holas"
#diccionarioP=dict(zip('abcde',[10,20,30,40,50]))
diccionarioP=dict(zip(claves,lista))
print(diccionarioP)
'''
dic1={'a':10, 'b':20}
dic2={'c':100, 'd':200, 'e':300}
print(dic1)
dic1.update(dic2)
print(dic1)