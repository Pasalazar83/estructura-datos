class Zoo:
    def __init__ (self,especie:str, animal:str, edad:int):
        self.especie=especie
        self.animal=animal
        self.edad=edad
    def  __str__ (self):
        return f"Zoo: {self.especie}, Animal: {self.animal}, Edad:{self.edad}"
    especie= ave("flamenco", "aguila","condor")
class clase(Zoo):
    def __init__ (self,especie:str, animal:str, edad:int):
        super().__init__ 
    


