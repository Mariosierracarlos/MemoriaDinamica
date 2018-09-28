from Memoria_Dinamica import Memoria_Dinamica

__author__ = 'mario sierra carlos'


from Memoria_Dinamica import *


promedio = 9.67
otralista = []
supermercado = ['comida','jugo', 'pepsi', 'tostada', 'cottel']
precios = [14, 44, 55, 67]
porcentajes = [.44, .55, .67, 1.2]

listas = Memoria_Dinamica(supermercado)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('tepache')
listas.imprimirLista()

lista2 = Memoria_Dinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(89)
lista2.imprimirLista()
