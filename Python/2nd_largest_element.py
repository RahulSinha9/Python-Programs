l = []
c = int(input("enter no. of element\n"))
for i in range (0,c):
    d = int(input())
    l.append(d)   
f = set(l)
g = list(f)
g.sort()
print ("2nd lagrest element is:",g[-2])

# n = int(input())
# for i in range(n):
#     n=int(input())
#     a=list(map(int,input().split()))