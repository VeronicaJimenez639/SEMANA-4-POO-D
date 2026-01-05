# Definimos la clase Mascota (representa una mascota real en la veterinaria)
class Mascota:
    # Constructor: se ejecuta cuando creamos un objeto Mascota()
    def __init__(self, nombre, especie, codigo):
        self.nombre = nombre          # Nombre de la mascota
        self.especie = especie        # Especie (perro, gato, etc.)
        self.codigo = codigo          # Código identificador de la mascota
        self.atendida = False         # Estado inicial: no ha sido atendida

    # Método para registrar atención médica
    def atender(self):
        if self.atendida:             # Se verifica si ya fue atendida las mascota
            return False              # Evita que se registre atención doble
        self.atendida = True          # Marcamos como atendida
        return True                   # Confirmamos la atención

    # Método para reiniciar el estado de atención
    def liberar(self):
        if not self.atendida:         # Si no estaba atendida...
            return False              # No se puede liberar
        self.atendida = False         # Se marca como disponible
        return True                   # Confirmamos la liberación

    # Método especial para mostrar la mascota como texto
    def __str__(self):
        estado = "Atendida" if self.atendida else "En espera"
        return f"Mascota({self.nombre}, {estado})"
    