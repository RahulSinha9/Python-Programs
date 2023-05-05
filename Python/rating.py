n = int(input())
for i in range (n):
  x,y = map(int,input().split())
  if (x<=y and x+200>=y):
      print("YES")
  else:
      print("NO")
  