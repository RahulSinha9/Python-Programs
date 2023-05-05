c = int(input())
for i in range (c):
    a=[]
    b = int(input())
    for i in range(b):
         a.append(input())
    if (a.count("cakewalk")>=1 and a.count("simple")>=1 and a.count("easy")>=1 and (a.count("easy-medium")>=1 or (a.count("medium")))>=1 and (a.count("medium-hard")>=1 or (a.count("hard")))>=1):
        print("Yes")
    else:
        print("No")
    
    