import random

# Generador de Datos de Prueba
def generador_datos_prueba(cantidad):
    datos_generados = []
    for _ in range(cantidad):
        registro = {
            'id': random.randint(1, 1000),
            'valor': random.random() *100
        }
        datos_generados.append(registro)
    return datos_generados

print (generador_datos_prueba(10))

