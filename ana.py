def a(n1,n2):
  if sorted(n1)==sorted(n2):
    return True
  else:
    return False

n1=input("enter 1st word: ")
n2=input("enter 2nd word: ")
print(a(n1,n2))
