from Nodo import Nodo

if __name__=='__main__':
    lista= list(range(1,6))
    head=Nodo()
    curr=head
    



   


# print("Aqui comiensa el forr")

e = [1, 2, 3, 4, 5]
head = Nodo()
carr = head
for i in range(len(e)):
    carr.val = e[i]
   
    if i < len(e) - 1:
        carr.next = Nodo()
       
        carr = carr.next
carr.next = head
carr = head
while True:
    print("El valor del nodo es", carr.val)
    carr = carr.next
    if carr == head:
        break  
print("El nodo inicial es", carr.val)