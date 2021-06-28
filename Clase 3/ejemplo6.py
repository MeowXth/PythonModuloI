matriz =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
n=0



a=99
while n < len (matriz):
    m=0
    while m<5:
        #print("[", end = str(matriz[n][m])+"]")

        matriz[n][m] = a
        a=a-1
        m+=1
    #print("")
    n+=1
n=0
while n<len(matriz):
    print(matriz[n])
    n+=1            