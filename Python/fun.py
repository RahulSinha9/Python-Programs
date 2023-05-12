# def sum(a,b):
#     return a+b
# a = int(input())
# b = int(input())
# print(sum(a,b))

n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    c= a+b
    d = c/2
    if(d%2==0):
        print(d)
    else:
        print("-1")    