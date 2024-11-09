import numpy as np
class Pila:
    __lista:np.ndarray
    __dimension:int
    __tope:int
    __cantidad:int
    def __init__(self,dim) -> None:
        self.__dimension=dim
        self.__tope=-1
        self.__cantidad=0
        self.__lista = np.full(self.__dimension,-1, dtype=int)
    def estaVacia(self):
        return self.__tope==-1
    def estaLlena(self):
        return self.__cantidad==self.__dimension
    def recorrer(self):
        i=0
        while i<=self.__tope:
            print(self.__lista[self.__tope-i])
            i+=1
    def apilar(self,num):
        if not self.estaLlena():
            self.__tope+=1
            self.__lista[self.__tope]=num
            self.__cantidad+=1
    def desapilar(self)->int:
        if not self.estaVacia():
            x = self.__lista[self.__tope]
            # self.__lista[self.__tope]=-1
            self.__tope-=1
            self.__cantidad-=1
            return x
        else:
            print("LISTA VACIA")
            return 0
    def retornaNum(self,index:int):
        return self.__lista[index]
    def getLista(self):
        return self.__lista
    def __str__(self) -> str:
        return self.__lista.__str__()
