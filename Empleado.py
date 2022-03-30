from Entidad import Entidad

class Empleado (Entidad):
    def __init__ (self,nombre):
        Entidad.__init__(self,nombre)