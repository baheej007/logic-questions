def f(l):
  if l<=1:
    return 0
  fl=[0,1]
  if l>1:
    for i in range(2,l):
       fl.append(fl[i-1]+fl[i-2])
      
  return fl
  
  
l=int(input("length : "))
print(f(l))
