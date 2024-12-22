def search(lst,t):
    for p,val in enumerate(lst):
        if val==t:
            return p
            
            
lst = [1, 3, 5, 7, 9]
t = 5
print('searched no at ',search(lst,t))

