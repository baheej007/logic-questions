def du(l):
  c={}
  for i in l:
    c[i]=0
  for i in l:
    c[i]+=1

  for i in c:
    if c[i]==1:
       return i
  
  
  


n=int(input("enter no of elements in the list: "))
l=[]
for i in range(0,n):
  l.append(int(input(f"{i+1}element: ")))
  
print(du(l))
