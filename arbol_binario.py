class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)

    def imprimir_inorden(self, nodo_actual):
        if nodo_actual:
            self.imprimir_inorden(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self.imprimir_inorden(nodo_actual.derecha)

    def imprimir_arbol(self):
        if self.raiz is None:
            print("El árbol está vacío")
        else:
            print("Árbol binario:")
            self.imprimir_inorden(self.raiz)

# Crear el árbol y agregar los datos
datos = [9, 2, 1, 16, 6, 11, 8, 4]
arbol = ArbolBinario()
for dato in datos:
    arbol.insertar(dato)

# Imprimir el árbol
arbol.imprimir_arbol()
