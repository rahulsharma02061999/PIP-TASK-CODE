tasks = []

def addTask():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"task is added successfully.")

def viewTask():
    if not tasks:
        print(" there are no tasks.")
    else:
        print("Tasks are as below.")
        for index, task in enumerate(tasks):
            print(f"Task {index+1}. {task}")

def deleteTask():
    viewTask()
    try:
        choice = int(input("enter your choice: "))
        choice = choice-1
        if choice>= 0 and choice < len(tasks):
            tasks.pop(choice)
            print(f"{choice+1} has been delete successfully.")
        else:
            print(f"{choice+1} not found.")

    except:
        print("Invalid choice made.")

if __name__ == "__main__": 
    print("Welcome to the TO-DO-LIST")
while (True):
    print("What do you want to do with your TO-DO-LIST:")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. DELETE TASK")
    print("4. EXIT")
    
    choice = input("Enter your choice: ")
    if(choice == "1"):
        addTask()
    elif(choice == "2"):
        viewTask()
    elif(choice == "3"):
        deleteTask()
    elif(choice == "4"):
        break
    else:
        print("You have made an invalid choice, try it again")
print("GoodBye")        