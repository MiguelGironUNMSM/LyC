from clases.Soltar import Soltar
from clases.Soltar import soltar_condicional

def p_soltar(t):
    """soltar : SOLTAR TABLA IDENTIFICADOR
              | SOLTAR TABLA condicional_soltar IDENTIFICADOR """
    if len(t) == 4:
        t[0] = Soltar(tabla= t[3])
    else:
        t[0] = soltar_condicional(tabla= t[4])

def p_condicional(t):
    """condicional_soltar : SI EXISTE """
    t[0] = f"{t[1]} {t[2]}"
