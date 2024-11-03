history = [] #empty list to store completed calculations

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View Calculation History")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2 #addition
        elif choice == '2':
            result = num1 - num2 #subtraction
        elif choice == '3':
            result = num1 * num2 #multiplication
        else:
            if num2 == 0:
                print("Error: Division by zero")
                continue
            result = num1 / num2 #division

        print(f"{num1} {choice} {num2} = {result}")
        history.append(f"{num1} {choice} {num2} = {result}") #the calculation is now being stored in the history list

        with open("calculations.txt", "a") as file:
            file.write(f"{num1} {choice} {num2} = {result}\n") #the calculations are stored in a file named calculations.txt

    elif choice == '5':
        print("Calculation History:") 
        for h in history:
            print(h) #all the performed calculations are displayed
    else:
        print("Invalid input. Please try again.") #error message incase input is not 1,2,3,4 or 5

    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != 'yes':
        break
