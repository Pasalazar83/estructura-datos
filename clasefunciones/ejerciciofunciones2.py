num1=int(input('ingrese el primer numero'))
num2=int(input('ingrese el segundo numero'))
operador=(input('ingrese el operador entre + - * /'))

def operacionmatematica(num1, num2 ):
    resultado: int
    if operador == '+':
        print(num1+num2)

    elif operador=='-':
        print(num1-num2)

    elif operador=='*':
        print(num1*num2)

    elif operador =='/':
        print(num1/num2)
        
    else: 
        print( "es invalido")
print(operacionmatematica(num1,num2))

        


   
