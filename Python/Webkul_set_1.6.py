n=4

for i in range(n):
    print('@')

print('@',end=" ")
print('*'*n)
x=n+1
for i in range(n-1):
    if i<(n-2):
        print(" "*x+'*'*n)
        x+=n-1
    else:
        print(' '*x+'*'*n,'@')
        
for i in range(n):
    print(' '*((n*(n-1))+4)+'@')