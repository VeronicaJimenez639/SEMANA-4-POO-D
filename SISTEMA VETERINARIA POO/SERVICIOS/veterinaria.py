# Definimos la clase Veterinaria (administra mascotas y atenciones)
class Veterinaria:
    # Constructor: se ejecuta cuando creamos Veterinaria()
    def __init__(self):
        self.mascotas = []            # Lista para guardar las mascotas registradas

    # Método para registrar una mascota en la veterinaria
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)  # Añadimos la mascota a la lista

    # Método para atender una mascota según su código
    def atender(self, codigo, propietario):
        for mascota in self.mascotas:        # Recorremos las mascotas
            if mascota.codigo == codigo:     # Buscamos por código
                if mascota.atender():        # Intentamos atenderla
                    return f"Mascota atendida para {propietario.nombre}"
                return "La mascota ya fue atendida"
        return "Mascota no encontrada"

    # Método para liberar una mascota
    def liberar(self, codigo):
        for mascota in self.mascotas:        # Recorremos las mascotas
            if mascota.codigo == codigo:
                if mascota.liberar():        # Intentamos liberar
                    return "Mascota liberada correctamente"
                return "La mascota ya estaba en espera"
        return "Mascota no encontrada"
