#lista=['jose','maria']
numero=input('coloca un numero ')


try:
    numero = int(numero)
    print(numero," Es un numero")
    try:
        pass
    except:
        pass
except :
     print("E1" ,numero," No es un numero")

finally:
    print("Si o SI ")     