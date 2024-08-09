def calculator():
    while True:
        print("\nSimple Calculator")
        print("-------------------")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("\nEnter the number corresponding to the operation (1/2/3/4): ")

        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: Division by zero is not allowed.")
        else:
            print("\nInvalid choice. Please select a valid operation.")
        
        next_step = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_step != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
