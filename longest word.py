def lw(s):
  l=[]
  st=""
  for i in s:
    if i!=" ":
      st+=i
    else:
      l.append(st)
      st=" "
  k=0
  j=""
  for i in l:
    if len(i)>k:
      k=len(i)
      j=i
  return j  
s = "Python programming is amazing"
print(lw(s))
 
