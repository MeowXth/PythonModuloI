from typing import List

#matriz =[[2,2,2,2,2],[3,3,0,3,3],[4,4,4,4,4],[5,5,5,5,5],[6,6,6,6,6]]
matriz =[[1,1,1,0,1],[2,2,2,2,2],[3,3,0,3,3],[4,4,4,4,4],[5,5,5,5,0]]
n=0
while n < len (matriz):
    m=0
    while m<5:
        #print("[", end = str(matriz[n][m])+"]")
        if matriz [n][m] == 0:
            matriz[n][m] = 11
        m+=1
    #print("")
    n+=1
n=0
while n<len(matriz):
    print(matriz[n])
    n+=1            
'''

for n in matriz:
    print(n)

'''



















'''
a=[]
#li1=[2,8,9,10,45,6,45,4,9,3]
li1=[2,2.5,"100",True,[1,2,3],(10,20)]
print(li1)
n=0

while n<len(li1):
    print(type(li1[n]),"    ----->",li1[n])
    n+=1
'''


'''
while n<len(li1):
    print(li1[n])
    n=n+1

for  n in li1
    print(n)    
'''    