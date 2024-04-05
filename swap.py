
n=[15,5,28,7,7,95,2,34,3,98]
p=int(input('enter index:'))
o=int(input('enter index:'))
a=n[p]
n[p]=n[o] 
n[o]=a
print(n)