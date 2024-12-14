def me(lst):
  dic = {}
  for i in lst:
      if i in dic:
          dic[i] += 1
      else:
          dic[i] = 1
      
  return max(dic.keys() )
  

lst = [2, 2, 1, 1, 2, 2, 2]
result = me(lst)
print("Final Dictionary:", result)
