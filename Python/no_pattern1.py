n = int(input())
# for i in range(n):
#     for j in range(n):
#         if(i>=j):
#          print("1", end=" ")
#         else:
#            print(" ", end=" ")
#     print() 
                 #or
# for i in range(n):
#       for j in range(i+1):               
#       print("1", end="")
#   print()   
           #or
s = "1"           
for i in range(n):
    print(s)
    s=s+"1"           