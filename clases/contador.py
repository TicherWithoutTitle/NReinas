class Contador:
    __nodosGenerados:int
    __nodosAnalizados:int
    __nodosPodados:int
    def __init__(self):
        self.__nodosGenerados = 0
        self.__nodosAnalizados = 0
        self.__nodosPodados = 0
    def __str__(self):
        return f"=== Estadísticas de la ejecución ===\nNodos generados: {self.__nodosGenerados}\nNodos analizados: {self.__nodosAnalizados}\nNodos podados: {self.__nodosPodados}\n============================="
    def getAnalizados(self):
        return self.__nodosAnalizados
    def getPodados(self):
        return self.__nodosPodados
    def getGenerados(self):
        return self.__nodosGenerados
    def setAnalizados(self,n):
        self.__nodosAnalizados+=n
    def setGenerados(self,n):
        self.__nodosGenerados+=n
    def setPodados(self,n):
        self.__nodosPodados+=n
