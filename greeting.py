name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    print(f"Hello mr. {name} your age is {age} and you are a great human being")
except Exception as e:
    print("Please enter a valid age!!!!")