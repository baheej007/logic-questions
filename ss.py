def ssc(t,ss):
  s=""
  lst=[]
  for i in t:
    if i !=" " and i!="," and i!="!":
      s=s+i
    else:
      lst.append(s)
      s=""
  print(lst)
  if ss in lst:
    return True 
  else:
    return False
      
      
t = "Hello, world!"
ss= "world"


print(ssc(t,ss))
