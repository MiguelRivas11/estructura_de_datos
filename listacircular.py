from Nodes import Nodes

class CircularLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter: int = 0
        self.head: Node or None = None
        self.tail: Node or None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_node = Nodes(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.counter += 1

    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Nodes(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.counter += 1

    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        if self.head is None:
            raise ValueError('La lista está vacía')
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            self.counter -= 1

    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        if self.head is None:
            raise ValueError('La lista está vacía')
        else:
            current = self.head
            while current.next != self.head:
                print(current.val, end=" -> ")
                current = current.next
            print(current.val)  # Imprime el último elemento

if __name__ == '__main__':
    lista_circular = CircularLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    for item in lista_tradicional:
        lista_circular.tailInsert(item)

    # Impresión de la lista
    print("Lista circular:")
    lista_circular.traverse()

    # Adición de un nuevo elemento al final
    n = False
    lista_circular.tailInsert(n)
    print("Lista circular después de agregar al final:")
    lista_circular.traverse()

    # Adición de un nuevo elemento al inicio
    n = 'Estructuras'
    lista_circular.headInsert(n)
    print("Lista circular después de agregar al inicio:")
    lista_circular.traverse()

    # Eliminación del primer elemento e impresión
    lista_circular.headRemove()
    print("Lista circular después de eliminar el primer elemento:")
    lista_circular.traverse()