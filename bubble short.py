l=[2,1,3,4,5,3,9]
# for i in range(len(l)-1):
#   if (l[i]>l[i+1]):
#     l[i],l[i+1]=l[i+1],l[i]



for i in range(len(l)):
    for j in range(len(l)-i-1):
        if(l[j]>l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]
            print(l)
    
            



            