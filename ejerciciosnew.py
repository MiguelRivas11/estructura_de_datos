# Initialize variables and array
I = 1
J = 2
A = [0] * 10

# Assign values to array A
A[I] = J
A[J] = I
A[J + I] = I + J
I = A[I] + A[J]

# Assign value 5 to A[3]
A[3] = 5

# Calculate and assign new value to J
J = A[I] - A[J]

# Print values of I and J after execution
print("Valor de I después de las instrucciones:", I)
print("Valor de J después de las instrucciones:", J)
#----------------------------------------------------------------------------------------------------------------------

# Calcular los cuadrados de los primeros 100 números enteros
cuadrados = [i ** 2 for i in range(1, 101)]

# Imprimir la tabla de cuadrados
print("Número\tCuadrado")
print("-----------------")
for i, cuadrado in enumerate(cuadrados, start=1):
    print(f"{i}\t{cuadrado}")
#------------------------------------------------------------------------------------------------------------
# Crear un vector de dimensión 100 (por ejemplo, lleno de unos)
vector = [1] * 100

# Calcular la suma de todos los elementos del vector
suma = sum(vector)

# Calcular la media aritmética
media = suma / len(vector)

# Imprimir resultados
print("Suma de todos los elementos del vector:", suma)
print("Media aritmética de los elementos del vector:", media)
#------------------------------------------------------------------------------------------------------
def encontrar_mayor(lista):
    # Verificar si la lista está vacía
    if len(lista) == 0:
        return None  # Si la lista está vacía, no hay mayor valor
    else:
        return max(lista)

# Ejemplo de uso
L = [10, 5, 8, 20, 15]  # Lista de ejemplo
mayor_valor = encontrar_mayor(L)
print("El mayor valor en la lista es:", mayor_valor)
#---------------------------------------------------------------------------------------------------------------------

N = 100
temperatura = []
suma = 0
media = 0
C = 0

print("Ingrese las temperaturas (Ingrese 'fin' para terminar):")
while len(temperatura) < N:
    entrada = input("Ingrese la temperatura {}: ".format(len(temperatura) + 1))
    if entrada.lower() == 'fin':
        break
    temperatura.append(float(entrada))
    suma += temperatura[-1]

if not temperatura:
    print("No se ingresaron temperaturas.")
    exit()

N = len(temperatura)
media = suma / N

print("Temperaturas mayores o iguales a la media:")
for temp in temperatura:
    if temp >= media:
        C += 1
        print(temp)

print("La media es:", media)
print("Cantidad de temperaturas mayores o iguales a la media (", media, ") es:", C)


