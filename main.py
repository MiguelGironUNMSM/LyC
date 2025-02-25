from AnalizadorLexico import analizar_lexico
from AnalizadorSintactico import analizar_sintaxis

query = """
SELECCIONAR  nombre , apellido DESDE Usuarios
"""

resultado_lexico = analizar_lexico(query)
print("Resultado del analisis lexico:")
for token in resultado_lexico:
    print(token)

resultado_sintactico = analizar_sintaxis(query)
print("\nResultado del analisis sintactico:")
print(resultado_sintactico)

# Simulación de una base de datos
base_de_datos = {
    "usuarios": {
        "columnas": ["id", "nombre", "edad"]
    }
}

while True:
    try:
        entrada = input("SELECCIONAR nombre, apellido DESDE Usuarios")  
        if entrada.lower() in ["salir", "exit"]:
            break

        resultado = parser.parse(entrada)  # Ejecuta el análisis sintáctico
        if resultado:
            analizar(resultado, base_de_datos)  # Ejecuta el análisis semántico

    except Exception as e:
        print("Error:", e)
