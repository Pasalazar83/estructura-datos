celsius= int(input("ingrese temperatura  en celsius: "))
farenheith= int(input("ingrese temperatura  en farenheith: "))

def gradostemperatura(celsius, farenheith):
    resultado: int 
    if celsius:
        resultado = (farenheith - 32) * 5/9
        print (resultado)
    
        resultado2 = (celsius * 9/5) + 32
        print(resultado2) 
print(gradostemperatura(celsius, farenheith))