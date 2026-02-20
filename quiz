# Clase Nodo
class Nodo:
    def __init__(self, data):
        self.data = data
        self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
    def __init__(self):
        self.cabeza = None

# Lista Vacia
    def vacio(self):
        if self.cabeza == None:
            print("Está vacia")
        else:
            print("Lista no vacia")

    # Agregar al inicio
    def agregarInicio(self, data):
        nuevo_nodo = Nodo(data)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

#insertar al final
    def insertarAlFinal(self, data):
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente

            actual.siguiente = nuevo_nodo
        
# agregar un elemento antes de x
    def agregarAntesDeX(self, data, x):
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            print("La lista está vacía. No se puede agregar antes de", x)
            return

        if self.cabeza.data == x:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            return
    
        actual = self.cabeza
    
        while actual.siguiente is not None and actual.siguiente.data != x:
            actual = actual.siguiente
        
        if actual.siguiente is None:
            print("El elemento", x, "no se encontró en la lista.")
        else:
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    #agregar un elemento despues de x
    def agregarDespuesDeX(self, data, x):
        nuevo_nodo = Nodo(data)

        if self.cabeza is None:
            print("La lista está vacía. No se puede agregar después de", x)
            return

        actual = self.cabeza

        while actual is not None and actual.data != x:
            actual = actual.siguiente

        if actual is None:
            print("El elemento", x, "no se encontró en la lista.")
        else:
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

# eliminar x
    def eliminarX(self, x):
        if self.cabeza is None:
            print("La lista está vacía. No se puede eliminar", x)
            return

        if self.cabeza.data == x:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza

        while actual.siguiente is not None and actual.siguiente.data != x:
            actual = actual.siguiente

        if actual.siguiente is None:
            print("El elemento", x, "no se encontró en la lista.")
        else:
            actual.siguiente = actual.siguiente.siguiente

# mostrar la lista
    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.data, end=" -> ")
            actual = actual.siguiente
        print("None")        

#eliminar el primer elemento
    def eliminarPrimerElemento(self):
        if self.cabeza is None:
            print("La lista está vacía. No se puede eliminar el primer elemento.")
            return

        self.cabeza = self.cabeza.siguiente

#eliminar el ultimo elemento
    def eliminarUltimoElemento(self):    
        if self.cabeza is None:
            print("La lista está vacía. No se puede eliminar el último elemento.")
            return

        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        actual = self.cabeza
        while actual.siguiente.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = None

#buscar elemento
    def buscar(self, x):
        actual = self.cabeza
        while actual is not None:
            if actual.data == x:
                return True
            actual = actual.siguiente
        return False

#contar elementos
    def contarElementos(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

# Clase para Huésped
class Huesped:
    def __init__(self, cedula, nombre, habitacion):
        self.cedula = cedula
        self.nombre = nombre
        self.habitacion = habitacion

    def __str__(self):
        return f"Cédula: {self.cedula}, Nombre: {self.nombre}, Habitación: {self.habitacion}"

# Clase para Habitación
class Habitacion:
    def __init__(self, numero):
        self.numero = numero
        self.disponible = True
        self.huesped = None

    def ocupar(self, huesped):
        if self.disponible:
            self.disponible = False
            self.huesped = huesped
            return True
        return False

    def liberar(self):
        if not self.disponible:
            self.disponible = True
            huesped = self.huesped
            self.huesped = None
            return huesped
        return None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Ocupada por {self.huesped.nombre if self.huesped else 'N/A'}"
        return f"Habitación {self.numero}: {estado}"

# Sistema de Hotel
class SistemaHotel:
    def __init__(self, num_habitaciones):
        self.habitaciones = ListaSE()
        for i in range(1, num_habitaciones + 1):
            self.habitaciones.insertarAlFinal(Habitacion(i))
        self.entradas = ListaSE()  # Lista de huéspedes actuales
        self.salidas = ListaSE()   # Lista de huéspedes que se retiraron


    def consulta_huesped_individual(self, cedula):
        actual = self.entradas.cabeza
        while actual is not None:
            if actual.data.cedula == cedula:
                print(actual.data)
                return
            actual = actual.siguiente
        print("Huésped no encontrado")

    def consulta_huesped_total_por_cedula(self):
        print("Huéspedes actuales por cédula:")
        actual = self.entradas.cabeza
        while actual is not None:
            print(actual.data)
            actual = actual.siguiente

    def consulta_huesped_total_por_orden_llegada(self):
        print("Huéspedes actuales por orden de llegada:")
        actual = self.entradas.cabeza
        while actual is not None:
            print(actual.data)
            actual = actual.siguiente

    def habitaciones_disponibles(self):
        print("Habitaciones disponibles:")
        actual = self.habitaciones.cabeza
        while actual is not None:
            if actual.data.disponible:
                print(actual.data)
            actual = actual.siguiente

    def habitaciones_ocupadas(self):
        print("Habitaciones ocupadas:")
        actual = self.habitaciones.cabeza
        while actual is not None:
            if not actual.data.disponible:
                print(actual.data)
            actual = actual.siguiente

