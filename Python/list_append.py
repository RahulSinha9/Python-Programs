arr = []
print("Array Before=",arr)

count = 0

while(True):
    a = input("Enter any friends name \n")
    arr.append(a)
    if len(a)>=4:
        count = count+1
    choice = input("wish to add more ?(y/n) :")
    if (choice== "n"):
        break
print("Array- After =" ,arr)   
print("Long String count=0",count)
print("Small String count=0",len(arr)-count)
 