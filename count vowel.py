def cv(str):
  c=0
  for i in str:
    if i in 'aeiou':
      c+=1

  return c
  











str = "Hello World!"
print(cv(str))
