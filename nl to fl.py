def fl(nl):
  ls=[]
  for i in nl:
    if isinstance(i, list):
      ls.extend(fl(i))
    else:
      ls.append(i)
      
  return ls
  
nl= [1, [2, [3, 4]], 5]
print(fl(nl))
