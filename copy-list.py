def copy(m):
    c=m
    return c   
 
m=list(map(int,input().split()))
c=copy(m)
print('original list is:',m)
print('copy list is:',c)
