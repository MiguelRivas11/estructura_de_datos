from Node import Node  

class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.counter += 1

    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        if self.head is None:
            raise ValueError('La lista está vacía')
        else:
            self.head = self.head.next
            self.counter -= 1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

if __name__ == '__main__':
    lista_ligada = LinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    for item in lista_tradicional:
        lista_ligada.tailInsert(item)

    # Impresión de la lista
    print("Lista ligada:")
    lista_ligada.traverse()

    # Adición de un nuevo elemento al final
    n = False
    lista_ligada.tailInsert(n)

    # Adición de un nuevo elemento al inicio
    n = 'Estructuras'
    lista_ligada.headInsert(n)

    # Eliminación del primer elemento e impresión
    lista_ligada.headRemove()
    print("Lista después de eliminar el primer elemento:")
    lista_ligada.traverse()

    # Eliminación del último elemento (o explica por qué no es posible en un comentario multilínea)
    ''' No se ha implementado la función para eliminar el último elemento'''

    ''' Manejo de errores '''
   
    try:
        lista_ligada.headRemove()
    except ValueError as e:
        print(e)

    try:
        print(1/0)
    except (ZeroDivisionError, ValueError) as identificador:
        print(f'Intentaste dividir entre 0 o hubo un error de valor ({identificador})')
    except Exception as e:
        print('Error inesperado')
    finally:
        print('Saliendo...')
