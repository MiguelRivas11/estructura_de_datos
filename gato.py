from objetos import animal
 
class Gato(animal):
    def __init__(self, nombre):
        super().__init__(nombre)

    def maullar(self):
        print('miau')

if __name__=='__main__':
    perro=animal('firulais')

    gato=Gato('Michi')
    print(gato)
    gato.maullar

 
 