def DeterminarDevengado(SalarioB,HExDiur,HExNoct,HExDomini):
    ValorExD=(SalarioB/30)/(8*1.25)
    ValorExN=(SalarioB/30)/(8*1.5)
    ValorDyF=(SalarioB/30)/(8*1.25)

    HorasExtrD=ValorExD*HExDiur
    HorasExtrN=ValorExN*HExNoct
    HorasDominiLu=ValorDyF*HExDomini

    TDevengados=SalarioB+HorasExtrD+HorasExtrN+HorasDominiLu
    print(f"Devengado {TDevengados} ")