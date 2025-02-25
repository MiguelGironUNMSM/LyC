from clases.Soltar import Soltar

def p_soltar(t):
    """soltar : SOLTAR TABLA IDENTIFICADOR
              | SOLTAR TABLA IDENTIFICADOR condicional """
    if len(t) == 4:
        t[0] = Soltar(tabla= t[3])
    else:
        t[0] = Soltar(tabla= t[3],condicional = t[4])

def p_condicional(t):
    """condicional : SI EXISTE """
    t[0] = f"{t[1]} {t[2]}"
