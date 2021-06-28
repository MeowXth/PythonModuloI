from collections import deque
class metodos():
    def listF(a):
        lista1 =[]
        lista2 =[]
        for i in a:
            if 50>i:
                lista1.append(i)
            else:
                lista2.append(i)    
        print(lista1)
        print(lista2)
        
    def listaM(d,f):
        listaMezclada=list()
        c=len(f)-1
        for i in d:
            listaMezclada.append(i)
            listaMezclada.append(f[c])
            c=c-1
        return print(listaMezclada)

    def proce (f):
        matriz =[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
        n=0
        while n < len (matriz):
            m=0
            while m<5: 
                cdf=f.popleft()
                matriz[n][m] = cdf
                f.append(cdf)
                m+=1
            df=f.popleft()
            f.append(df)
            n+=1
        n=0
        while n < len (matriz):
            m=0
            while m<5: 
                print("[", end = str(matriz[n][m])+"]")
                m+=1
            print("")
            n+=1
            print()
