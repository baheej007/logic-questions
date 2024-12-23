def find_ss(lst):
  ss = [[]]  
  ls=[]
  k=1
  for num in lst:
    
      new_ss = [subset + [num] for subset in ss]
      ss.extend(new_ss)
  for i in ss:
    for j in i:
      k=k*j
      
    ls.append(k)
    k=1
  return max(ls)
lst = [-10, -10, 1, 3, 2]
print("Subsets:", find_ss(lst))
