from modelos.mascota import Mascota        # Importamos la clase Mascota
from modelos.propietario import Propietario # Importamos la clase Propietario
from servicios.veterinaria import Veterinaria  # Importamos la clase Veterinaria

# Definimos la función principal del programa
def main():
    veterinaria = Veterinaria()   # Creamos el objeto Veterinaria

    # Crear mascota y propietario
    mascota1 = Mascota("Firulais", "Perro", "001")   # Creamos una mascota
    propietario1 = Propietario("Verónica", "2100662044")  # Creamos un propietario

    veterinaria.agregar_mascota(mascota1)  # Registramos la mascota

    print(veterinaria.atender("001", propietario1))   # Atendemos la mascota
    print(veterinaria.atender("001", propietario1))   # Intentamos atender otra vez
    print(veterinaria.liberar("001"))                 # Liberamos la mascota
    print(veterinaria.atender("001", propietario1))   # La atendemos nuevamente
    print(veterinaria.atender("999", propietario1))   # Código NO existe

# Ejecutamos el programa
if __name__ == "__main__":
    main()
