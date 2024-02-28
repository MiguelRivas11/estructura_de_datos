from listDinamic import ListaDinamica
from string import ascii_lowercase as defalph

class Caesar:
    def init(self, alphabet:str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self.alphabet = self.set_alphabet(alphabet)

    def encrypt(self, msg:str, key:int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
        pass  # Implementa la lógica de encriptación aquí

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