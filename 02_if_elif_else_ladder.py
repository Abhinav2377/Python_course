# if elif else ladder

n = int(input("Enter your age: "))

if (n>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(n<0):
    print("You are entering and invalid age")

elif(n==0):
    print("You are entering 0 which is not a valid age ")    

else:
    print("you are below the age of consent")    

print("End of program")    

