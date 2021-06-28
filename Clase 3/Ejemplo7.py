vec=[10,8,6,4,2]
matriz=[]
matriz.append(vec)
zz=list(reversed(vec))
matriz.append(zz)
matriz.append(vec)
matriz.append(zz)
matriz.append(vec)
matriz.append(zz)


print(vec)
for i in matriz:
    for j in i:
        print("[", end = str(j)+"]")
    print()    