n = int(input())
for i in range (n):
    a,b = map(int,input().split())
    if (a>b or a == b):
        print(b)
    elif (a<b):
        print(a)    
    else:
        print(b)
        