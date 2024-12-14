def inter(l1,l2):
  lst=[]
  for i in l1:
    for j in l2:
      if i==j:
        lst.append(i)
        
  return lst
  
l1= [1, 2, 3, 4]
l2 = [3, 4, 5, 6]
print(inter(l1,l2))
