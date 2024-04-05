n=list(map(str,input().split()))

print(n)
p=int(input('enter index:'))
o=int(input('enter index:'))
a=n[p]
n[p]=n[o] 
n[o]=a
print(n)
