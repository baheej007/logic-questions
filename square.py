def ps(num):
    if num<2:
        return True
    else:
        for i in range(2,num):
         for j in range(2,num):
             if i*j==num:
               return True
    return False          
             
num = 36
print(ps(num))
    