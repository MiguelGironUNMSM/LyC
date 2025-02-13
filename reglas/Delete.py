def p_eliminar(t):
    """eliminar : ELIMINAR DESDE IDENTIFICADOR condicion_opt"""
    t[0] = ("eliminar", t[3], t[4])