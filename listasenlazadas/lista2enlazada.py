class Animal:
    def __init__ (self, especie:str, edad:int):
        self.especie=especie
        self.edad=edad
    
    def  __str__ (self):
        return f" {self.especie}- Edad:{self.edad}"

    
class Nodo:
    def __init__ (self, animal:str):
        self.animal= animal
        self.siguiente= None

class listaenlazada:
    def __init__ (self):
        self.head=None
    
    def agregar_animal(self, nuevo_animal):
        if not self.head:
            self.head= Nodo(nuevo_animal)
            return 
        
        actual= self.head
        while actual:
            if actual.animal.especie== nuevo_animal.especie and actual.animal.edad== nuevo_animal.edad:
                print("el animal se encuentra en la lista")
                return
            if  actual.siguiente==None:
                break
            actual= actual.siguiente

        actual.siguiente= Nodo(nuevo_animal)

    def mostrar__animales__lista(self, nodo):
        if self==None:
            return
        print(nodo.animal) 
        self.mostrar__animales__lista(nodo.siguiente)   
    
    def  mostrar__animales__lista2(self):
        actual= self.head
        while actual:
            print(actual.animal)
            actual=actual.siguiente
           
    zoo= listaenlazada()
    zoo.agregar_animal(Animal( "cocodrilo","reptiles", 7))
    zoo.agregar_animal(Animal( "aguila", "aves", 30))
    zoo.agregar_animal(Animal( "orangutan","primates", 18))
    
    print("animales en el zoologico(lista):")
    zoo.mostrar__animales__lista(zoo.head) 

    print("Animales en el zoo(lista2):")
    zoo.mostrar__animales__lista2()

    
   
        

    

        


