from Padre import Padre
class Palabra(Padre):
    
    def __init__(self,tipo,palabra,fila,columna):
        self.tipo=tipo
        self.palabra = palabra
        super().__init__(fila,columna)

    def funcionToken(self):
        return self.palabra
    
    def getFila(self):
        return super().getFila()
    
    def getColumna(self):
        return super().getColumna()
    
    def getPalabra(self):
        return self.palabra