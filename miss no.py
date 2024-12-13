def fm(nums):
  l=[]
  for i in range(min(nums),max(nums)-1):
    if i not in nums:
      l.append(i)
  

  return l




nums = [1, 2, 4, 6, 3, 7, 8]
print(fm(nums))
