l=[11,54,4,546,86,8,6,48,7]
e=int(0)
o=int(0)
for i in l:
    if (i%2==0):
      e+=1  
    else:    
      o+=1
print('even count:',e)

print('odd count:',o)