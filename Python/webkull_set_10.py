n=5
x=n
for i in range((n+1)//2):
    print(' '*(((n-1)//2)+i)+'@'*x)
    x-=2
    
print('*'*n)
print(('*'+' '*(n-2)+'*\n')*(n-1))