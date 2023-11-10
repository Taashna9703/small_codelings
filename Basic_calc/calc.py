def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
flag=1
while(flag==1):
    print("Your options are:")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit \n")

    choice=input("Enter your choice:")
    if choice=="A" or choice=="a":
        print("Addition")
        a=int(input("Enter number:" ))
        b= int(input("Enter number:" ))
        print("Your answer is: ",add(a,b),"\n")
    elif choice=="B" or choice=="b":
        print("Subtraction")
        a=int(input("Enter number:" ))
        b= int(input("Enter number:" ))
        print("Your answer is: ",sub(a,b))
    elif choice=="C" or choice=="c":
        print("Multiplication")
        a=int(input("Enter number:" ))
        b= int(input("Enter number:" ))
        print("Your answer is: ",mul(a,b))
    elif choice=="D" or choice=="d":
        print("Division")
        a=int(input("Enter number:" ))
        b= int(input("Enter number:" ))
        print("Your answer is: ",div(a,b))
    elif choice=="E" or choice=="e":
        print("Exit")
        flag=0
        quit()
    else:
        print("Invalid choice, choose a valid option")


