number = int(input())
temp= number
rev= 0
while(number>0):
    digit = number%10
    rev = rev*10 + digit
    number = number//10
if(temp==rev):
        print("palindrome")
else:
        print("Not a palindrome")    
    