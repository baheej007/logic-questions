def pw(l):
  nl = []
  
  for i in range(len(l)):
    p = 1
    for j in range(len(l)):
          
          if i != j:
              p *= l[j]
    nl.append(p)
  return nl

n = int(input("Enter the number of elements in the list: "))
l = []
for i in range(n):
  l.append(int(input(f"Element {i+1}: ")))

print(pw(l))
