# DELETE FROM 'nombreTabla'
def p_eliminar(t):
    """eliminar : ELIMINAR DESDE IDENTIFICADOR opt_condiciones"""
    t[0] = ("eliminar", t[3], t[4])
