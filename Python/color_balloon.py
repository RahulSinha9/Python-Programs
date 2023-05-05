n = int(input())
for i in range(n):
    a = input().strip()
    print(min(a.count("a"),a.count("b")))
        