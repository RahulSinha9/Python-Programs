n = int(input())
for i in range (n):
    a,b,c,d,e,f = map(int,input().split())
    l1=[]
    l2=[]
    l1.append(c)
    l1.append(d)
    l2.append(e)
    l2.append(f)
    if(a in l1 and b in l1):
        print("1")
    elif(a in l2 and b in l2):
        print("2")
    else:
        print("0")