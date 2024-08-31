def calculofactorial ( numero:int)->str|int:
    resultado: int =1 
    if numero < 0:
        return"no se puede valores negativos"
    elif numero == 0 :
        return 1
    for n in range (1,numero+1):
        resultado = resultado * n
    return resultado
    
