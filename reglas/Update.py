def p_actualizar(t):
    """actualizar : ACTUALIZAR IDENTIFICADOR COLOCAR lista_asignaciones opt_condiciones"""
    t[0] = ("actualizar", t[2], t[4], t[5])


def p_lista_asignaciones(t):
    """lista_asignaciones : IDENTIFICADOR IGUALDAD valor
                          | lista_asignaciones COMA IDENTIFICADOR IGUALDAD valor"""
    if len(t) == 4:
        t[0] = [(t[1], t[2], t[3])]
    else:
        t[0] = t[1] + [(t[3], t[4], t[5])]
