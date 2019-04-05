from libgenerarPagoMes import *
from libsalario import DeterminarSalub
from libdevengados import DeterminarDevengado

if(__name__=='__main__'):
    Cedula=(input("Porfavor digite el numero de su cedula =>"))
    NombreC=(input("Porfavor Digite su nombre completo =>"))
    SalarioB=int(input("Digite su salario =>"))
    HExDiur=int(input("Digite las horas extras diurnas trabajadas =>"))
    HExNoct=int(input("Digite las horas extras nocturnas trabajadas =>"))
    HExDomini=int(input("Digite las horas extras dominicales trabajadas =>"))
    DTra=int(input("Dias trabajados =>"))
    DeterminarPago(Cedula,NombreC,SalarioB,HExDiur,HExNoct,HExDomini,DTra)
    DeterminarDevengado(SalarioB,HExDiur,HExNoct,HExDomini)
    DeterminarSalub(SalarioB)