from AnalizadorSintactico import analizar_consulta

resultado = analizar_consulta("""
 CREAR TABLA empleados (
    id_empleado ENTERO CLAVE_PRIMARIA,
    nombre CADENA(50) NO_NULO,
    edad ENTERO
)
""")


print("Resultado de la consulta:")
print(resultado)

