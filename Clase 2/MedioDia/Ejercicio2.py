def buscar(n1,n2,n3):
    for dato in n1:
        if dato=="Gonzalo":
            print("Existe")
    #pass


listaNom1=["Ale","Ana","Pedro","Gonzalo","Raul","Marta"]
listaNom2=["Mar","Diego","Pedro","Raul","Marta"]
listaNom3=["Juan","Ana","Pedro","Raul","Marta"]
for dato in listaNom3:
    if dato=="Gonzalo":
        print("Existe")
    else:
        print("No")

buscar(listaNom1,listaNom2,listaNom3)