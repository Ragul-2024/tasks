def swap(n):
    s=len(n)
    a=n[0]
    n[0]=n[s-1]
    n[s-1]=a
    return n
n=[12,5,48,65,79,5,28,34]
print(swap(n))
