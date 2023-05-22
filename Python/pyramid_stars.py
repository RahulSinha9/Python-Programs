print("Enter the no. of rows ")
rows =int(input())
for i in range (rows):
    for j in range (i+1):
        print( "*", end  = "")
    print ("\n")    