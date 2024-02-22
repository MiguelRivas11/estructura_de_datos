import ctypes

class ListaDinamica:
    def __init__(self) -> None:
        ''' Inicializar un arreglo vacío '''
        self.__n=0
        self.__c=1
        self.__a=self.__init_arr(self.__c)# Elementos actuales (lista contenedora)
        # Capacidad inicial por defecto
        # Arreglo contenedor

    def __len__(self) -> int:
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.__n

    def __getitem__(self, k) -> object:
        ''' Regresa un elemento en una posición k -> arreglo[k]; k = -1 -> arreglo[ultima_posición_valida] '''
        if k < 0:
            if abs(k) >  self.__n:
                raise IndexError(f'indice invalido ({k})')
            k= self.__n + k
        elif k < 0 >= self.__n:
            raise IndexError(f'indice invalido ({k})')
        return self.__a[k]
    
    def append(self, obj) -> None:
        ''' Añade un elemento al final de la lista '''
        if self.__n == self.__c:
            self.__resize(2*self.__c)
            
        self.__a[self.__n]=obj
        self.__n+=1

    def __resize(self, c) -> None:
        ''' Modifica el tamaño de la lista interna '''
        B=self.__init_arr(c )
        for i in range(self.__n):
            B[i]=self.__a[i]

        self.__a=B
        self.__c=c   

    def __init_arr(self, capacidad): # No tocar; Ya implementada
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()     # Magia

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
    ''' Descomentar el siguiente for si se hizo la implementación de índices negativos
    for i in range(1, len(ld)+1):
        print(ld[-i]) '''

    ''' Usar el siguiente for en caso contrario '''
    for i in range(len(ld)):
        print(ld[i])