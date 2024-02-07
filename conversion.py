from Nodo import Nodo

if __name__=='__main__':
    lista= list(range(1,6))
    head=Nodo()
    curr=head
    


e = [1, 2, 3, 4, 5]
head = Nodo()
carr = head
prev=None
i = 0
while i < len(e):
    carr.val = e[i]
    carr.prev=prev
    if i < len(e) - 1:
        carr.next = Nodo()
        prev=carr
        carr = carr.next
        
    i += 1

curr = head

while curr is not None:
    print( "el valor del nodo es",curr.val)
    print( "el valor previo del nodo es",curr.prev)
    print( "el valor siguiente del nodo es",curr.next,end="\n\n")
    curr = curr.next
   

curr = prev
while curr is not None:
    print("El valor del nodo es", curr.val)
    curr = curr.prev
# print("Aqui comiensa el forr")
# e = [1, 2, 3, 4, 5]
# head = Nodo()
# carr = head
# i = 0
# for i in range(len(e)):
#     carr.val = e[i]
#     if i < len(e) - 1:
#         carr.next = Nodo()
#         carr = carr.next

# carr = head  
# while carr is not None: 
#     print("el valor del nodo es :",carr.val)
#     carr = carr.next            