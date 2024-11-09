import numpy as np
from clases.nodo import Nodo
from clases.arbol import ArbolGeneral
from clases.pila import Pila
N = 4

def mostrarTablero(nodo:Nodo,tablero:np.ndarray,solucion:bool=False,lista:Pila=Pila(N)):
    if nodo.getHijos()!=[]:
        for hijo in nodo.getHijos():
            lista.apilar(hijo.getvalor())
            mostrarTablero(hijo,tablero,True,lista)
            lista.desapilar()
    elif solucion:
        for i in range(N):
            tablero[i][lista.retornaNum(i)]="|R|"
        print("==============================")
        for i in range(N):
            for j in range(N):
                print(tablero[i][j],sep=" ",end="")
            print()
        tablero.fill("|.|")
# Funcion que revisa si un vector es K-prometedor
def esFactible(pila:Pila, fila, columna):
    for i in range(fila):
        if pila.retornaNum(i) == columna or abs(pila.retornaNum(i) - columna) == abs(i - fila):
            return False  # No es K-prometedor
    return True
# Función principal que implementa la solución del problema de las N reinas
def NReinasPila(pila:Pila, nodo, fila):
    if fila == N:
        print(f"Solución encontrada: {pila}")
        return True
    else:
        solucion=False
        for columna in range(N):
            if esFactible(pila, fila, columna):
                nuevo_nodo=Nodo(columna)
                nodo.agregar_hijo(nuevo_nodo)
                pila.apilar(columna)
                if NReinasPila(pila,nuevo_nodo,fila+1):
                    solucion =True
                else:
                    nodo.eliminarHijo(columna,N)
                pila.desapilar()
        return solucion


if __name__=='__main__':
    arbol = ArbolGeneral(-1,N)  # Crear un árbol con la raíz inicial -1 (valor de inicio)
    raiz = arbol.obtener_raiz()  # Obtener la raíz del árbol
    pila=Pila(N)  # Vector solución de tipo Pila, donde no hay valores, retorna -1
    NReinasPila(pila, raiz,0)  # Llamada a la función principal
    arbol.mostrar_arbol()  # Mostrar el árbol una vez que todas las soluciones se han agregado
    tablero=np.full((N,N),"|.|")  # Tablero para mostrar por pantalla
    mostrarTablero(raiz,tablero)
