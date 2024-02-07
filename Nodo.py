'''Modulo contenedor de clase Nodo para listas ligadas'''
class Nodo:
    '''clase de Nodo'''
    def __init__(self,val:int=None):
        '''Inicializador de clase'''
        self.val=val
        self.next=None
        self.prev=None

    def __str__(self) -> str:
        if self.val:
            return f'valor del nodo={self.val}'
        
        return f'el nodo no tiene valor'
    
   
        
        

      