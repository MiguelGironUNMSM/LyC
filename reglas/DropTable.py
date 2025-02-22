def p_soltar(t):
    """soltar : SOLTAR TABLA IDENTIFICADOR"""
    t[0] = ("soltar", t[3])
