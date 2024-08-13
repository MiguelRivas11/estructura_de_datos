from ListaDinamica import ListaDinamica

class emtyStack(Exception):
    '''error personalizado'''

    class stack:
       
        def __init__(self)->None:
            self.__s = ListaDinamica()

        def __len(self)->int:
            return len(self.__s)

        def is_emty(self)->bool:
            return len(self.__s)==0

        def push(self, e) -> None:
            self.__s.append(e)
        
            


    
   
   
