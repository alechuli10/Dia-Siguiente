class Entidad:
    def __init__ (self,nombre):
        self.nombre= nombre
    def destruccion (self):
        print(self.nombre, " destruido")