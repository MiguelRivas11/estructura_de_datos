class Lista:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, *elementos):
        for elemento in elementos:
            self.elementos.append(elemento)

    def eliminar_elemento(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
            print("Elemento eliminado correctamente.")
        else:
            print("El elemento no se encuentra en la lista.")

# Ejemplo de uso

lista = Lista()

   
lista.agregar_elemento(5, 10, 15)

   
lista.eliminar_elemento(10)

 
print(lista.elementos)
