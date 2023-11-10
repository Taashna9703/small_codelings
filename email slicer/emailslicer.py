def ex():
    print("Email slicer is here for you! \n")

    email=input("Enter your email address:")
    (user, domain)=email.split("@")
    (domain, extension)=domain.split(".")

    print(f"Your username is: {user} \nand your domain is :{domain} \nand your extension is :{extension}")
    
ex()