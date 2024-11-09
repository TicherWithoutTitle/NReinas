from clases.nodo import Nodo
class ArbolGeneral:
    __raiz:Nodo
    __N:int
    def __init__(self, valor_raiz,N):
        self.__raiz = Nodo(valor_raiz)
        self.__N=N
    def obtener_raiz(self):
        return self.__raiz

    def mostrar_arbol(self):
        if self.__raiz:
            self.__raiz.mostrar()
        else:
            print("el arbol esta vacio.")

    def suprimir(self, valor):
        if self.__raiz.getvalor() == valor:
            print("no se puede suprimir la raíz del arbol.")
            return

        if not self.__raiz.eliminarHijo(valor,self.__N):
            print(f"el nodo con valor {valor} no fue encontrado en el arbol.")
