tls=[]
def find_is(lst):
  
  
  ls=[]
  
  k=0
  m=0
  
  for p,val in enumerate(lst):
      if val>k:
        k=k+val
        ls.append(val)
        
      else:
        tls.append(ls)
        ls=[]
        
        find_is(lst[p:])
        
        break
        
        
  
        
        

    
  return (tls)
lst = [10, 22, 9, 33, 21, 50, 41, 60]
mi=min(lst)

print("Subsets:", find_is(lst+[mi-1]))
