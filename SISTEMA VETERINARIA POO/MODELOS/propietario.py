# Definimos la clase Propietario (representa al responsable de la mascota)
class Propietario:
    # Constructor: se ejecuta cuando creamos un objeto Propietario()
    def __init__(self, nombre, cedula):
        self.nombre = nombre          # Nombre del propietario
        self.cedula = cedula          # Cédula del propietario

    # Método especial para mostrar el propietario como texto
    def __str__(self):
        return f"Propietario({self.nombre})"
    