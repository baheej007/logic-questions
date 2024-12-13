def arm(num):
   l=len(str(num))
   sum=0
   for i in str(num):
     sum=sum+int(i)**l
   if sum==num:
     return True 
   else:
     raise False 
     


  







num = 372
print(arm(num))
