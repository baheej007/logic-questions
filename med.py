def m(lst):
  a=0
  b=0
  lsta=sorted(lst)
  if len(lsta)%2==0:
    a=lsta[len(lsta)//2]
    b=lsta[(len(lsta)//2)-1]
    return int((a+b)/2)
  else:
    return int(lsta[len(lsta)//2])
    
  
  












lst = [1, 3, 3, 6,7, 8, 9]
print(m(lst))
