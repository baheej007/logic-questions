def fsa(a):
    sa = []
    sas=[]
    
    for i in range(len(a)):
        for j in range(i, len(a)):
            
                sa.append(a[i:j+1] ) 
       
    for i in sa:
        if sum(i)==0:
            sas.append(i)
    s=0  
    ls=[]
    for i in sas:
        if len(i)>s:
            s=len(i)
            ls=i
    return   ls     
            

n = int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
  l.append(int(input(f"Element {i+1}: ")))

print(fsa(l))
