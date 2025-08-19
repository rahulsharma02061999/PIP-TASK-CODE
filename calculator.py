try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("What kind of operation you want to do.\n press + for addition \n press - for subtraction \n press * for multiplication \n press / for division")
    choice = input("Enter your choice: ")
    match choice:
        case "+":
            print(f"The sum of {a} and {b} is: {a+b}")
        case "-":
            print(f"fThe difference of {a} and {b} is: {a-b}")
        case "*":
            print(f"The multiplication of {a} and {b} is {a*b}")
        case "/":
            print(f"The division of {a} and {b} is {a/b}")
        case default:
           print("There was and error")
except Exception as e:
    print("Enter a valid Value")