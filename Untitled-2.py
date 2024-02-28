"Lista dinamica"
import ctypes

class ListaDinamica:
    def __init__(self):
        ''' Inicializar un arreglo vacío '''
        self.capacidad = 10  # Capacidad inicial por defecto
        self.arreglo = self.__init_arr(self.capacidad)  # Arreglo contenedor
        self.elementos = 0  # Elementos actuales (lista contenedora)

    def __len__(self):
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.elementos

    def __getitem__(self, k):
        ''' Regresa un elemento en una posición k -> arreglo[k]; k = -1 -> arreglo[ultima_posición_valida] '''
        if k < 0:
            k = self.elementos + k
        if k >= self.elementos or k < 0:
            raise IndexError("Índice fuera de rango")
        return self.arreglo[k]

    def append(self, obj):
        ''' Añade un elemento al final de la lista '''
        if self.elementos == self.capacidad:
            self.__resize(self.capacidad * 2)
        self.arreglo[self.elementos] = obj
        self.elementos += 1

    def __resize(self, c):
        ''' Modifica el tamaño de la lista interna '''
        nuevo_arreglo = self.__init_arr(c)
        for i in range(self.elementos):
            nuevo_arreglo[i] = self.arreglo[i]
        self.arreglo = nuevo_arreglo
        self.capacidad = c

    def __init_arr(self, capacidad):
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()

if __name__ == '__main__':
    '''
        Pruebas de la clase:
        El siguiente código no debe ser modificada
        y debe correr sin errores
    '''
    # 1. Instanciación
    ld = ListaDinamica()

    # 2. Inserción de al menos 5 elementos
    ld.append(10)
    ld.append(20)
    ld.append(False)
    ld.append(-0.53)
    ld.append('String')

    # 3. Impresión de los elementos usando for
    for i in range(len(ld)):
        print(ld[i])