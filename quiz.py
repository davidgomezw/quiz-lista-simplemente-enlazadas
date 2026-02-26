class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None


class ListaSE:
    def __init__(self):
        self.cabeza = None

    def insertarAlFinal(self, data):
        nuevo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminarObjeto(self, objeto):
        if self.cabeza is None:
            return

        if self.cabeza.data == objeto:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        while actual.siguiente and actual.siguiente.data != objeto:
            actual = actual.siguiente

        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

# Clase Huésped
class Huesped:
    def __init__(self, cedula, nombre, habitacion):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion

    def __str__(self):
        return f"Cédula: {self.cedula} | Nombre: {self.nombre} | Habitación: {self.habitacion}"


# Clase Habitación
class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.disponible = True
        self.huesped = None

    def __str__(self):
        if self.disponible:
            return f"Habitación {self.numero} - Disponible"
        else:
            return f"Habitación {self.numero} - Ocupada por {self.huesped.nombre}"


# Sistema del Hotel
class SistemaHotel:
    def __init__(self, num_habitaciones):
        self.habitaciones = ListaSE()
        self.entradas = ListaSE()
        self.salidas = ListaSE()

        for i in range(1, num_habitaciones + 1):
            self.habitaciones.insertarAlFinal(Habitacion(i))

    # Buscar habitación por número
    def buscar_habitacion(self, numero):
        actual = self.habitaciones.cabeza
        while actual:
            if actual.data.numero == numero:
                return actual.data
            actual = actual.siguiente
        return None

    # Registrar entrada
    def registrar_entrada(self, cedula, nombre, num_habitacion):
        habitacion = self.buscar_habitacion(num_habitacion)

        if habitacion and habitacion.disponible:
            huesped = Huesped(cedula, nombre, num_habitacion)
            habitacion.disponible = False
            habitacion.huesped = huesped
            self.entradas.insertarAlFinal(huesped)
            print("Entrada registrada correctamente")
        else:
            print("Habitación no disponible")

    # Registrar salida
    def registrar_salida(self, cedula):
        actual = self.entradas.cabeza

        while actual:
            if actual.data.cedula == cedula:
                huesped = actual.data
                habitacion = self.buscar_habitacion(huesped.habitacion)

                habitacion.disponible = True
                habitacion.huesped = None

                self.salidas.insertarAlFinal(huesped)
                self.entradas.eliminarObjeto(huesped)

                print("Salida registrada correctamente")
                return

            actual = actual.siguiente

        print("Huésped no encontrado")

    # Consulta individual
    def consulta_individual(self, cedula):
        actual = self.entradas.cabeza
        while actual:
            if actual.data.cedula == cedula:
                print(actual.data)
                return
            actual = actual.siguiente
        print("Huésped no encontrado")

    # Consulta total por orden de llegada
    def consulta_total_llegada(self):
        print("\nHuéspedes por orden de llegada:")
        actual = self.entradas.cabeza
        while actual:
            print(actual.data)
            actual = actual.siguiente

    # Consulta total por cédula (ordenado simple)
    def consulta_total_cedula(self):
        lista = []
        actual = self.entradas.cabeza
        while actual:
            lista.append(actual.data)
            actual = actual.siguiente

        lista.sort(key=lambda x: x.cedula)

        print("\nHuéspedes ordenados por cédula:")
        for h in lista:
            print(h)

    # Habitaciones disponibles
    def habitaciones_disponibles(self):
        print("\nHabitaciones disponibles:")
        actual = self.habitaciones.cabeza
        while actual:
            if actual.data.disponible:
                print(actual.data)
            actual = actual.siguiente

    # Habitaciones ocupadas
    def habitaciones_ocupadas(self):
        print("\nHabitaciones ocupadas:")
        actual = self.habitaciones.cabeza
        while actual:
            if not actual.data.disponible:
                print(actual.data)
            actual = actual.siguiente

# MENÚ PRINCIPAL
hotel = SistemaHotel(5)

while True:
    print("\n--- SISTEMA HOTEL ---")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Consulta huésped individual")
    print("4. Lista huéspedes por llegada")
    print("5. Lista huéspedes por cédula")
    print("6. Habitaciones disponibles")
    print("7. Habitaciones ocupadas")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cedula = input("Cédula: ")
        nombre = input("Nombre: ")
        habitacion = int(input("Número de habitación: "))
        hotel.registrar_entrada(cedula, nombre, habitacion)

    elif opcion == "2":
        cedula = input("Cédula del huésped: ")
        hotel.registrar_salida(cedula)

    elif opcion == "3":
        cedula = input("Cédula: ")
        hotel.consulta_individual(cedula)

    elif opcion == "4":
        hotel.consulta_total_llegada()

    elif opcion == "5":
        hotel.consulta_total_cedula()

    elif opcion == "6":
        hotel.habitaciones_disponibles()

    elif opcion == "7":
        hotel.habitaciones_ocupadas()

    elif opcion == "8":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")

