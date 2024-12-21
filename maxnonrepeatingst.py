def sc(t):
  l=[]
  s=""
  j=0
  for i in t:
     if i not in s:
       s=s+i
     else:
       l.append(s)
       s=i
  for i in l:
    if len(i)>j:
      j=len(i)
    
  return j 











t= "ababaabcdefhcu"
print(sc(t))
