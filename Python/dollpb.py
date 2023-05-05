a =int(input())
for i in range (a):
    b=[]
    c=int(input())
    for j in range(c):
        d=int(input())
        if d not in b:
            b.append(d)
        else:
            b.remove(d)
    for i in b:
        print(i)            
        