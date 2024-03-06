
from ListaDinamica import ListaDinamica

class EmptyStack(Exception):
    ''' Error personalizado para stack vacío '''

class Stack:
    ''' Clase implementadora de stack '''

    def __init__(self) -> None:
        self.__S = ListaDinamica()
    
    def __len__(self) -> int:
        ''' Regresa el número de elementos dentro del stack '''
        return len(self.__S)

    def is_empty(self) -> bool:
        ''' Indica si el stack está vacío '''
        return len(self) == 0
    
    def push(self, e) -> None:
        ''' Agregar un elemento al stack '''
        self.__S.append(e)

    def top(self) -> object:
        ''' Regresa el elemento hasta el tope del stack sin eliminarlo '''
        if self.is_empty():
            raise EmptyStack("el estack esta vacio")
        return self.__S[-1]

        

    def pop(self) -> object:
        ''' Elimina el elemento hasta el tope del stack y lo regresa '''
        if self.is_empty():
            raise EmptyStack("el estack esta vacio")
        return self.__S.pop()

    def __str__(self) -> str:
        return str(self.__S) 
     


if __name__ == '__main__':
    ''' Pruebas de la implementación '''
    s= Stack()
    scuencia =[1,2,3,'A','B',False,True]
    for elen in scuencia:
        s.push(elen)

    print(f'Stack resultante -> {s}')
    print(f'¿El stack esta vacio -> {"si" if s.is_empty() else "No"}')
    print(f'El elemento hacta arriva ->{s.top()}')
    print(f'Longitud original -> {len(s)}')
    print(f'Eliminacion del elemento hasta arriva -> {s.pop}')
    print(f'Nueva longitud -> {len(s)}')
    print(f'Nueva representacion -> {s}\n')

    s_empty=Stack()
    print(f'Stack resultante -> {s_empty}')
    print(f'Longitud del segundo stack ->{len(s_empty)}')
    try:
        print(f'Elemento hasta arriva -> {s_empty.pop()}')
    except EmptyStack as e:
        print(f'El stack esta vacio ->({e} ({e} ({e} (Creo que estack esta vacio))))')
    except:
        print(f'Un error inesperado ')        


     
