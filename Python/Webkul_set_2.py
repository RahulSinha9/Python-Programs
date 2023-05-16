n=9
m=(n+1)//2
print((' '*m+'@\n')*n,end="")
a=m
x=1
for i in range(1,m+1):
    print(" "*a+'*'*x)
    a-=1;x+=2
# print(a)
x=n-2
b=2
for i in range(1,(n-m)+1):
    print(" "*b+'*'*x)
    b+=1;x-=2

print(' '+'@'*n)