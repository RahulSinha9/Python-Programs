n = int(input())
for i in range(0,n+1):
    x = i+1
    for j in range(i+1):
        print(x,end="")
        x+=1
    print()    