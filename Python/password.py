import random
symbol = int(input("Enter symbol length\n"))
digit = int(input("Enter digit length\n"))
letter = int(input("Enter letter length\n"))

letters = ['a','b','c',"d",'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digits = [1,2,3,4,5,6,7,8,9,0]
symbols = ['@',"#",'!',"$","&","?","*"]

password_list = []
for i in range (0,symbol):
   password_list.append(random.choice(symbols))
for i in range (0,digit):
   password_list.append(random.choice(digits))   
for i in range (0,letter):
   password_list.append(random.choice(letters))  
print(password_list)  

random.shuffle(password_list) 

password = ''
for char in password_list:
    password = password+str(char)
print(password)    
     