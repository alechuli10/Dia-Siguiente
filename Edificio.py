from Entidad import Entidad

class Edificio (Entidad):
    def __init__ (self,nombre,ubicacion):
        Entidad.__init__(self,nombre)
        ubicacion.edificios.append(self)