# res=[]
# def fact(n: int)->int:
#     if (n==1):
#         return n
#        


# print(fact(n))

#define la funcion fibonnaci que toma como parametro n para devolver un entero
def fibonacci(n:int)->int:
    
    if (n<=1 ):
        # analisa si el valor n es igual o menor que1 si es verdadero devuelve el valor de n
        return n
        
    else:
        #si es falsa llama otra vez a la funcion con dos valores diferentes  y suma los resultados 
        return fibonacci(n-1) + fibonacci(n-2)
    
 # se ingresamendiate consola un numero 
pp=[]    
ss=int(input())  
fibonacci(ss)
for i in range(ss):
    result=fibonacci(i)
    pp.append(result)
    # print(fibonacci(i))
    
print(pp)


