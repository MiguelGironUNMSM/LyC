def p_transaccion(t):
    """transaccion : INICIAR_TRANSACCION
    | CONFIRMAR
    | REVERTIR"""
    t[0] = t[1]