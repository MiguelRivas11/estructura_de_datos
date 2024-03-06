from listDinamic import ListaDinamica
from string import ascii_lowercase as defalph

class Caesar:
    def init(self, alphabet:str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self.alphabet = self.set_alphabet(alphabet)

    def encrypt(self, msg:str, key:int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
          # Implementa la lógica de encriptación aquí
        contenedor=ListaDinamica(len(msg))
        for c in msg:
            if c== ' ':
                contenedor.append(c)
                continue
            if c.isupper():
                c=c.lower()
            if c not in self.alphabet:
                contenedor.append(c)
                continue
            desp=None
            if key<0:
                desp=self__alphabet.index()
            else:
                
                    



    def multiple_decrypt(self, msg:str) -> str:
        ''' Herramienta interactiva para múltiples desencriptaciones '''
        pass  # Implementa la lógica de desencriptación aquí

    def setalphabet(self, alphabet:str) -> ListaDinamica:
        ''' Definir alfabeto de la herramienta '''
        alphabetlist = ListaDinamica()
        alphabet = alphabet.lower()  # Convertir a minúsculas
        for char in alphabet:
            alphabet_list.append(char)
        return alphabet_list

if __name__ == '__main':
    ''' Incluye aquí tus casos de prueba '''