import numpy as np

n = 5
print(n, "Bienvenidos al juego")

coordenada = input("Introduce coordenada: ")
print(coordenada)

tablero = np.full((10,10), "~")
print(tablero)

#ejemplo de crar otro .py y llevar solo la parte que se precise
#import testeo
#from testeo import pide_coordenada
