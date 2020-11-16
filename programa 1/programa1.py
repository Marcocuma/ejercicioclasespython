import math



class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Forma:
    def __init__(self,color,coord,nombre):
        self.color = color
        self.coordCenFor = coord
        self.nombre = nombre
    def imprimir(self):
        print(self.nombre)
        print(self.color)
        print(self.coordCenFor.x)
        print(self.coordCenFor.y)
    def obtenerColor(self):
        return self.color
    def cambiarColor(self,color):
        self.color = color
    def moverForma(self,coord):
        self.coordCenFor = coord

class Rectangulo(Forma):
    def __init__(self,color,coord,nombre,ladMenor,ladMayor):
        Forma.__init__(self,color,coord,nombre)
        self.ladMenor = ladMenor
        self.ladMayor = ladMayor
    def imprimir(self):
        Forma.imprimir(self)
        print(self.ladMenor)
        print(self.ladMayor)
    def calcularArea(self):
        return self.ladMenor*self.ladMayor
    def calcularPerimetro(self):
        return 2*self.ladMayor+2*self.ladMenor
    def cambiarTamanio(self,factEscala):
        self.ladMenor = self.ladMenor*factEscala
        self.ladMayor = self.ladMayor*factEscala

'''Probando las clases'''
forma = Forma("rojo",Punto(1,3),"Punto1")
print("Valores de la forma")
forma.imprimir()
print("Obteniendo y cambiando el color")
print(forma.obtenerColor())
forma.cambiarColor("azul")
print(forma.obtenerColor())
forma.moverForma(Punto(2,3))
print("Valores actualizados")
forma.imprimir()
print("----------Rectangulo-------------")
rectangulo = Rectangulo("rojo",Punto(1,3),"Rectangulo1",5,7)
rectangulo.imprimir()
print(rectangulo.calcularArea())
print(rectangulo.calcularPerimetro())
rectangulo.cambiarTamanio(2)
print(rectangulo.calcularArea())



class Elipse(Forma):
    def __init__(self,color,coord,nombre,radMayor,radMenor):
        Forma.__init__(self,color,coord,nombre)
        self.radMayor = radMayor
        self.radMenor = radMenor
    def imprimir(self):
        Forma.imprimir(self)
        print(self.radMayor)
        print(self.radMenor)
    def calcularArea(self):
        return math.pi*(self.radMenor*self.radMayor)

class Cuadrado(Rectangulo):
    def __init__(self,color,coord,nombre,ladMayor,ladMenor):
        Rectangulo.__init__(self,color,coord,nombre,ladMayor,ladMenor)
    def imprimir(self):
        Forma.imprimir(self)
class Circulo(Elipse):
    def __init__(self,color,coord,nombre,radMayor,radMenor):
        Elipse.__init__(self,color,coord,nombre,radMayor,radMenor)
    def imprimir(self):
        Forma.imprimir(self)

'''Programa 1'''
forma = Forma("rojo",Punto(1,3),"Forma1")
rectangulo = Rectangulo("rojo",Punto(4,2),"Rectangulo1",6,1)
elipse = Elipse("rojo",Punto(6,4),"Rectangulo1",6,8)
cuadrado = Cuadrado("rojo",Punto(2,3),"Cuadrado1",3,5)
circulo = Circulo("rojo",Punto(7,2),"Rectangulo1",1,4)
lista = [forma,rectangulo,cuadrado,circulo]

'''Muevo los puntos y pongo las formas del mismo color'''
x = 1
y = 3
for forma in lista:
    forma.moverForma(Punto(x,y))
    forma.cambiarColor("Verde")
    x += 1
    y += 1
'''Muestro sus valores'''
for forma in lista:
    print('----Valores----')
    forma.imprimir()