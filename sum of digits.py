def sod(n):
  c=0
  k=str(n)
  
  for i in k:
    c+=int(i)
  return c
    
num = 12345
print(sod(num))

