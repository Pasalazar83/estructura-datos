num1=int(input('ingrese el primer numero'))
num2=int(input('ingrese el segundo numero'))
operador=(input('ingrese el operador entre + - * /'))

if operador == '+':
    print(num1+num2)
elif operador=='-':
    print(num1-num2)

elif operador=='*':
    print(num1*num2)

elif operador =='/':
    print(num1/num2)

else :
    print('operador no valido')