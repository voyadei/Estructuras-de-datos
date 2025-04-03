class Node:
    """Node in a linked list, stores data and reference to the next node."""
    
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
    
    def get_next(self):
        return self.next
    
    def set_next(self, next_node):
        self.next = next_node

nodo1=Node(10)
print(nodo1)



class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del objeto
        self.edad = edad      # Atributo del objeto

    def mostrar_info(self):
        """Muestra el nombre y la edad de la persona."""
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Crear objetos de la clase Persona
persona1 = Persona("Ana", 25)
persona2 = Persona("Carlos", 30)

# Acceder a los atributos
print(persona1.nombre)  # Salida: Ana
print(persona2.edad)    # Salida: 30

# Usar el método para mostrar información
persona1.mostrar_info()  # Salida: Nombre: Ana, Edad: 25
persona2.mostrar_info()  # Salida: Nombre: Carlos, Edad: 30
