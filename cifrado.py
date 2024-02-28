from ListaDinamica import ListaDinamica
from string import ascii_lowercase as def_alph

class Caesar:
    def __init__(self, alphabet: str) -> None:
        ''' Inicializa herramienta criptográfica '''
        self.alphabet = alphabet

    def encrypt(self, msg: str, key: int, inverse=False) -> str:
        ''' Des/encriptar un mensaje '''
        result = ListaDinamica()
        for char in msg:
            if char == ' ':
                result.append(char)
                continue

            temp = char
            if char.isupper():
                temp = char.lower()

            if temp not in self.alphabet:
                result.append(temp)
                continue

            shift = key
            if inverse:
                shift = -key

            index = (self.alphabet.index(temp) + shift) % len(self.alphabet)
            new_char = self.alphabet[index]
            if char.isupper():
                new_char = new_char.upper()

            result.append(new_char)

        return ''.join(str(i) for i in result)
    
    def multiple_decrypt(self, msg: str) -> None:
        ''' Herramienta interactiva para múltiples desencriptaciones '''
        num_pasos = 0
        i = 1
        while True:
            decrypted_msg = self.encrypt(msg, i, True)
            print(f"Paso: {i}, Decrypted Message: {decrypted_msg}")
            user_input = input("Presiona Enter para ver la siguiente desencriptación o escribe 'q' para salir: ")
            num_pasos += 1
            if user_input.lower() == 'q':
                break
            i += 1
        print(f"Número total de pasos: {num_pasos}")
        print(f"Última palabra desencriptada: {decrypted_msg}")

if __name__ == '__main__':
    palabra = input("Ingresa la palabra a encriptar: ")
    desplazamiento = int(input("Ingresa el desplazamiento: "))

    ''' Inicializar el cifrador Caesar '''
    caesar = Caesar(def_alph)

    palabra_encriptada = caesar.encrypt(palabra, desplazamiento)
    print("Palabra encriptada:", palabra_encriptada)

    caesar.multiple_decrypt(palabra_encriptada)
