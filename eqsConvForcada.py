def coefPelicula(nu: float, d: float, k: float) -> float:
    """
    Calcula o coeficiente de película um fluido (ou coeficiente de transferência de calor por convecção):
    Input:
        nu  ->  Número de Nusselt
        d   ->  Dimensão que domina o fenômeno da convecção
        k   ->  Condutividade térmica do fluido
    Output:
        Coeficiente de película um fluido
    """
    h = nu * k / d
    return h


def numNusselt(c: float, re: float, m: float, pr: float, n: float):
    """
    Calcula o número de Nusselt para escoamento externo: 
    Input:
        c   ->  Coeficiente da espressão
        re  ->  Número de Reynolds
        m   ->  Coeficiente para re
        pr  ->  Número de Prandt
        n   ->  Coeficiente para pr
    Output:
        Numero de Nusselt
    """
    nu = c * pow(re, m) * pow(pr, n)
    return nu


def numReynolds(d: float, v: float, rho: float, v_: float):
    """
    Calcula o número de Reynolds: 
    Input:
        d   ->  Dimensão que domina o fenômeno da convecção
        v   ->  Velocidade do fluido
        rho ->  Densidade do fluido
        v_  ->  Viscosidade dinâmica do fluido
    Output:
        Numero de Reynolds
    """
    re = d * v * rho / v_
    return re


def numPrandt(c: float, v_: float, k: float):
    """
    Calcula o número de Prandt: 
    Input:
        c   ->  Calor específico do fluido
        v_  ->  Viscosidade dinâmica do fluido
        k   ->  Condutividade térmica do fluido
    Output:
        Numero de Reynolds
    """
    pr = c * v_ / k 
    return pr