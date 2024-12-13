def rs(s):
  st=""
  ls=[]
  for i in s:
    if i!=" ":
      st=st+i
    else:
      ls.append(st)
      st=""
  ls.append(st)
  k=ls[::-1]
  for i in k:
    print(i,end=" ")

  return "."
      
      
    
    
    









s="Python is fun "
print(rs(s))
