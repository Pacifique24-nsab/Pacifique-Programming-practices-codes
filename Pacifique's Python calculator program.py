print("Welcome to the simple calculator program made by Pacifique!")
while True:
    name = input("What's your name? ")
    # Check if the user has entered a valid name with composed by alphabets only!!
    if not name.isalpha():
        print("Invalid name! Please enter a valid name with alphabets in it. This is a simple advice for your friend Pacifique !!!.")
        continue
    else:
        print("Hello " + name + ", we are excited to help and assist you during your calculations!!!")
        break

while True:
    print("What calculation would you like to perform", name , "?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. exit the program")
    choice = input("Enter your choice (1/2/3/4/5): ")

    # Check if choice is a valid integer from 1 to 4
    while choice not in ['1', '2', '3', '4','5']:
        print("Invalid choice! Please enter a valid choice from 1 to 5.")
        choice = input("Enter your choice (1/2/3/4/5): ")

    num1 =input("Enter first number: ")

    # Check if num1 is a valid integer
    while not num1.isdigit():
        print("Invalid input! Please enter a valid integer for the first number.")
        num1 =input("Enter first number: ")
      
    num2 =input("Enter second number: ")

    # Check if num2 is a valid integer
    while not num2.isdigit():
        print("Invalid input! Please enter a valid integer for the second number.")
        num2 =input("Enter second number: ")

    if choice == '1':
        print(" you selected addition")
        result =int(num1)  + int(num2)
        print("The result of your addition is:", result)
    elif choice == '2':
        print("you selected substraction")
        result = int(num1) - int(num2)
        print("The result of your subtraction is:", result)
    elif choice == '3':
        result = int(num1) * int(num2)
        print("The result of your multiplication is:", result)
    elif choice == '4':
        if num2 == 0:
            print("Error: You cannot divide by zero " + name + ", I am sorry for that!!" )
        else:
            result = int(num1) / int(num2)
            print("The result of division is:", result,"number")
    else:
        print("Invalid choice!")

    
    while True: 
        continue_choice = input("Would you like to continue to do your calculations (yes/no)? ")
        if continue_choice == "yes":
            break
        elif continue_choice == "no":
            print("Thanks for using the pacifique calculator program ", name, "! Goodbye, enjoy your day dude!!")
        else:
            print("Error: you made an invalid input, please enter 'yes'or 'no'!!")
    print("Thanks for using the pacifique calculator program ", name, "! Goodbye, enjoy your day dude!!")
