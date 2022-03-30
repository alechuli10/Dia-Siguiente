from Entidad import Entidad

class Empresa (Entidad):
    def __init__ (self,nombre,edificios,empleados):
        Entidad.__init__(self,nombre)
        self.edificios= edificios
        self.empleados= empleados