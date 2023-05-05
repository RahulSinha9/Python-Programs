print("Your chaiwala")
print("---------Menu---------")
print("Tea,Coffee,")
print("Tea Price = 10","Coffee Price = 20")
a = input("Enter choice from menu\n")
if(a=="Tea"):
    bill = 10
elif(a=="Coffee"):
    bill = 20       
sugar = input("Do you need extra suger")
if(sugar=="Yes"):
    bill  +=2
rusk = input("Do you want rusk")
if (rusk=="Yes"):
    bill +=5 
print("Total cost is", bill)     
       
 
           
    
    
    
    

 