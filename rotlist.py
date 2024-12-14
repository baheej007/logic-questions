def rl(lst,k):
  
  l=len(lst)
  s=[]
  for i in range(0,l):
    s.append(0)
  for p,val in enumerate(lst):
    print(p)
    if p+k<l:
      s[p+k]=val
    else:
      s[p+k-l]=val
  


  return s








lst = [1, 2, 3, 4, 5]
k = 2
print(rl(lst,k))
