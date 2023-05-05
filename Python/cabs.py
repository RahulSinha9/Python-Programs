n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        print('FIRST')
    elif a > b:
        print('SECOND')
    else:
        print('ANY')
    