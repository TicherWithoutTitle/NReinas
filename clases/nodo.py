from clases.cola import ColaSecuencial
class Nodo:
    __valor:int
    __hijos:list
    def __init__(self, valor):
        self.__valor=valor
        self.__hijos=[]

    def agregar_hijo(self, hijo):
        self.__hijos.append(hijo)

    def cant_hijos(self):
        return len(self.__hijos)

    def getvalor(self):
        return self.__valor
    def getHijos(self):
        return self.__hijos
    # Eliminar un hijo del nodo
    def eliminarHijo(self,valor,N):
        queue=ColaSecuencial(N)
        queue.insertar(self)
        while not queue.estaVacia():
            nodoActual=queue.suprimir()
            for i,hijo in enumerate(nodoActual.getHijos()):
                if hijo.getvalor()==valor:
                    nodoActual.getHijos().pop(i)
                    return True
                else:
                    queue.insertar(hijo)
    def mostrar(self, nivel=0):
        # print(" "*nivel*4+"|"+"_" *nivel + str(self.__valor))
        print(" " *nivel *4+ str(self.__valor))
        for hijo in self.__hijos:
            hijo.mostrar(nivel + 1)
