from Entidad import Entidad

class Ciudad (Entidad):
    def __init__ (self,nombre):
        Entidad.__init__(self,nombre)
        self.edificios= []
    def destruccion (self):
        Entidad.destruccion(self)
        for edificio in self.edificios:
            edificio.destruccion()