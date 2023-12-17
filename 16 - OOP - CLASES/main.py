#OBJETCT ORIENTED PROGRAMING

#Define a class (mold to create more objects from this type with the similar characteristics)

class coche:
    #Atributes and properties (in previous excercises "variables")
    color = "rojo"
    marca = "Ferrari"
    modelo = "360"
    velocidad = 300
    caballos = 500
    plazas = 2

    #Methods. They are actions that objects do (in previous excercises "functions")

    def acelerar(self): #Reserved word for having access to atributes or properties
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad
    
#Create a object coche

coche = coche()

print (coche.marca, coche.modelo, coche.color)
print ("Velocidad inicial", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print ("Velocidad nueva1", coche.velocidad)

coche.frenar()

print ("Velocidad nueva1", coche.velocidad)

