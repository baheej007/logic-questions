
def avgsum(nums):
  sn=0
  sp=0
  n=[]
  p=[]
  
  for i in nums:
    if i<0:
      n.append(i)
      sn+=i 
    else:
      p.append(i)
      sp+=i

  navg=sn/len(n)
  pavg=sp/len(p)
  return sn,sp,navg,pavg 
  








numbers = []
for i in range(4):
    num = int(input(f"Enter integer {i+1}: "))
    numbers.append(num)
print(avgsum(numbers))


