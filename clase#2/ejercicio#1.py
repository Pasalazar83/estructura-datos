num1=input('digite el primer numero')
num2=input('digite el segundo numero')
num3=input('digitee el tercer numero')

if numero_uno > numero_dos and numero_uno > numero_tres:
    if numero_dos > numero_tres:
        print('el numero mayor es:','1',numero_uno, '2',numero_dos, "3",numero_tres)
    else:
        print(numero_uno, numero_tres, numero_dos)
elif numero_dos > numero_uno and numero_dos > numero_tres:
    if numero_uno > numero_tres:
        print('el numero mayor es:','1',numero_dos,'3', numero_uno, '4',numero_tres)
    else:
        print('el numero mayor es:','1',numero_dos, '2',numero_tres, '3',numero_uno)
else:
    if numero_uno > numero_dos:
        print('1',numero_tres,'2', numero_uno,'3', numero_dos)
    else:
        print('1',numero_tres, '2',numero_dos,'3', numero_uno)
        