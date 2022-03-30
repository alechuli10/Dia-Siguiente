from Empleado import Empleado
from Ciudad import Ciudad
from Edificio import Edificio
from Empresa import Empresa

def simulacion ():
  martin= Empleado("Sr. Martin")
  salim= Empleado("Sr. Salim")
  xing= Empleado("Sra. Xing")
  newYork= Ciudad("New York")
  losAngeles= Ciudad("Los Ángeles")
  a= Edificio("A",newYork)
  b= Edificio("B",newYork)
  c= Edificio("C",losAngeles)
  yoohoo= Empresa("Yoohoo",[a,b,c],[martin,salim,xing])
  
  newYork.destruccion()
  print ("--------")