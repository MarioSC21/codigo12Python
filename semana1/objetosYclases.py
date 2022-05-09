
class Automovil:
    #crear atributos o popiedades
    def __init__(self,aa,pl,col,mar):
        self.ano = aa
        self.placa = pl
        self.color = col
        self.marca = mar
    
    def encender (self):
        print('encender '+ self.marca)
    
    def acelerar (self):
        print('acelerar'+ self.marca)
    
    def frenar (self):
        print('frenar'+ self.marca)        

#?Creacion de objetos
vw = Automovil(1970, 232131, "rojo", "vw")
#accediendo a los atributos

print("ano: " + str(vw.ano))

#?utilizando el objeto
vw.encender()