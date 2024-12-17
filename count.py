def c(lst):
    dic={}
    for i in lst:
        if i in dic:
           dic[i]+=1
        else:
            dic[i]=1
    return dic   
lst = [1, 2, 2, 3, 3, 3]
print(c(lst))
