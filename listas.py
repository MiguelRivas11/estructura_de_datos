# nomre_de_la_variable=[]
# metodo2 = (metodo2)
# print(metodo2)
# for i in 'cadena de caracteres':
#     print(i)
lista =range(100)
# print(list(lista))
    
for i in lista : # for i in range # n=5
    print(i)
x= list(range(1,11,2))
for i in range(len(x)):
    print(i,x[i])    


for i , elemento in enumerate(x):
    print(i, elemento)

import random
desordenada = [random.randint(1,100) for _ in range(100)]
print(desordenada)
desordenada.sort(reverse=True)
print (desordenada)
otralista =list('miguel rivas')
elemento=otralista[0]+otralista[1]+otralista[3]
elemento=otralista[:4]
elemento.reverse()
elemento=otralista[4:]
elemento=otralista[0::3]
for i in range(len(otralista)):
    holder= otralista[i]+holder
    print(holder)

# print(elemento)
# elemento= otralista[::-1]
# elemento_volteado=''.join(list(reversed(elemento)))
# print(elemento_volteado)
# lista= list(range(10))
# print(lista[len(lista)-1])
# print(lista)
# holder=lista.pop(0)
# print(holder)
# print(lista)
# listaVacia=[]
# for i in range(50):
#     listaVacia.append(i+1)
# print(listaVacia)    
x=[1,2,3,1,4,0]
x.insert(18,True)
print(x)
