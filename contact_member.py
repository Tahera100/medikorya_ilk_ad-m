# Hi everyone! 
# Here we are with a new mini but important code together, 
# that at least once or towice in a day we use it in our cell phons.
# _____----- that is: contact member -----______

contact={}    # we need to define an empty variable to save our information inside it.and

while True:

    print("Choice from the operation in the below :")
    print("Add a new member = write done 1. ")
    print("Remove a member = write done 2. ")
    print("Show a member = write done 3. ")
    print("log out = write done 4. ")

    user_choice= input("Please write done the operation you want to do as 1,2,3 or 4. ")

    if user_choice=="1":
        name= input("Enter the name: ")
        phone_number=input("Enter the phone number: ")
        contact[name]=phone_number
        print(f"{name} added successfully")

    elif user_choice=="2":
        name= input("Enter the name, you want to remove : ")
        if name in contact:
            del contact[name]
            print(f"The {name} username is deleted successfully! ")
        else:
            print(f"The {name} is not in your conatact! ")
    elif  user_choice=="3":
            for name, phone_number in contact.items():
                print(f"{name} = {phone_number}")
    elif  user_choice=="4":
       #yes=input("do you want to log out?  ")
        #if yes=="yes":
            print("You logged out!")
        #else:
           # print("Enter the correct option among 1,2,3 and 4 ")

    break


    
