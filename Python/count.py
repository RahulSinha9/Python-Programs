a= int(input())
for i in range (a):
    k = int(input())
    l = list(map(int,input().split()))
    count = 0
    b = len(l)
    for i in range(0,b):
        if(l[i]>=1000):
            count = count+1
    print(count)
            
        