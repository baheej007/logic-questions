def tsum(t,lst):
  l=[]
  for i in lst:
    for j in lst:
      if t==i+j:

        l.append((i,j))



  return l
lst=[1, 2, 3, 4, 5]
t=6
print(tsum(t,lst))
