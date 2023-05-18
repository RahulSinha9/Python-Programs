n=9
if n%2!=0:
    print(" "*(n-1)+"@"+'*'*(n+2)+'@')
    for i in range(2,n+1):
        print(' '*(n-i)+'@'*i+' '*((n+2)//2)+'*'+' '*((n+2)//2)+'@'*i)
        
else:
    print('Invalid input')
        
    