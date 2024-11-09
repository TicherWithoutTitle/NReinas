import numpy as np
class ColaSecuencial:
    __lista:np.ndarray
    __maximo:int
    __ultimo:int
    __primero:int
    __cantidad:int
    def __init__(self,max) -> None:
        from clases.nodo import Nodo
        self.__lista=np.ndarray(max,dtype=Nodo)
        self.__maximo=max
        self.__ultimo=0
        self.__primero=0
        self.__cantidad=0
    def estaVacia(self):
        return self.__cantidad==0
    def insertar(self,elem):
        if(self.__cantidad<self.__maximo):
            self.__lista[self.__ultimo]=elem
            self.__ultimo=(self.__ultimo+1)%self.__maximo
            self.__cantidad+=1
        else:
            print("LISTA VACIA")
    def suprimir(self):
        if self.estaVacia():
            print("LISTA VACIA")
            return None
        else:
            x=self.__lista[self.__primero]
            self.__primero=(self.__primero+1)%self.__maximo
            self.__cantidad-=1
            return x
    def getLista(self):
        return self.__lista
    def retornaNum(self, index: int) -> int:
        if index < 0 or index >= self.__cantidad:
            raise IndexError("Índice fuera de rango")
        pos = (self.__primero + index) % self.__maximo
        return self.__lista[pos]
