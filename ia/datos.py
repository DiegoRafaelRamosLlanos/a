from faker import Faker

fake = Faker()

def generar_conversacion(num_mensajes):
    conversacion = []
    for _ in range(num_mensajes):
        mensaje = fake.text()
        conversacion.append(mensaje)
    return "\n".join(conversacion)

# Ejemplo de generación de una conversación
conversacion_sintetica = generar_conversacion(10)
print(conversacion_sintetica)
