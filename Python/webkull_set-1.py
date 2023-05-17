n=3

print('@'*(n+2))
x=1
for i in range((n+1)//2):
    print(' '*(((n+1)//2)-i)+'*'*x)
    x+=2
y=n-2
for i in range(((n+1)//2)-1):
    print(' '*(2+i)+'*'*y)
    y-=2
    
print((' '*((n+1)//2)+"@\n")*n)