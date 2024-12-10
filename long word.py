def lw(s):
  st,rs="",""
  k=0
  for i in s:
    if i!=" ":
      st+=i
    else:
      if len(st)>k:
        k=len(st)
        rs=st
        st=""
  return rs

s = "Python programming is amazing"
print(lw(s))
 
