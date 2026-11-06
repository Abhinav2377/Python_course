# 

n = int(input("Enter your age: "))

#if statement no:1
if(n%2==0):
    print("n is even")
# End of If statement no: 1 ,this if is independent


# If statement no:2
if (n>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(n<0):
    print("You are entering and invalid age")

elif(n==0):
    print("You are entering 0 which is not a valid age ")    

else:
    print("you are below the age of consent") 
#end of If statement no:2       

print("End of program")    

