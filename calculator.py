while True: 
    choice = int(input("\nEnter Operation\n"
                       "1. Addition (+)\n"
                       "2. Subtraction (-)\n"
                       "3. Multiply (*)\n"
                       "4. Division (/)\n"
                       "5. Exit\n: "))

    if choice == 1:
        num1 = int(input("Enter First Value : "))
        num2 = int(input("Enter Second Value : "))
        print("Result =", num1 + num2)

    elif choice == 2:
        num1 = int(input("Enter First Value : "))
        num2 = int(input("Enter Second Value : "))
        print("Result =", num1 - num2)

    elif choice == 3:
        num1 = int(input("Enter First Value : "))
        num2 = int(input("Enter Second Value : "))
        print("Result =", num1 * num2)

    elif choice == 4:
        num1 = int(input("Enter First Value : "))
        num2 = int(input("Enter Second Value : "))
        if num2 == 0:
            print("Error: Division by zero is not allowed")
        else:
            print("Result =", num1 / num2)

    elif choice == 5:
        print("Exit !")
        break

    else:
        print("No Operator Found")


