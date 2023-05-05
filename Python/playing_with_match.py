n = int(input())
for i in range (n):
    a,b = map(int,input().split())
    c = a+b
    d = str(c)
    sum = 0
    for i in d:
        if (i == '0' or i == '6' or i == '9'):
            sum = sum+6
        elif(i == '2'or i=='3' or i == '5'):
            sum = sum+5
        elif(i == '1'):
            sum = sum+2
        elif( i == '4'):
            sum = sum+4
        elif(i == '7'):
            sum = sum+3
        elif(i == '8'):
            sum = sum+7
    print(sum)        