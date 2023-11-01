print("********************** Welcome *************************")

myList = []

while(True):
    print("\nOptions: ")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Remove Task")
    print("4. View Task")
    print("5. Exit")
    print("Enter your choice (1-5): ")


    choice = int(input())


    match choice:
        case 1:
            print("Enter the Task to add into your list: ")
            task = input()
            myList.append(task)
            print("Task Added")
        case 2:
            completeTask = int(input("Enter the Task index to mark as Completed: ")) - 1
            if 0 <= completeTask < len(myList):
                task = myList[completeTask]
                if task.startswith("[Completed] "):
                    print("Task already marked as completed: ", task)
                else:
                    myList[completeTask] = "[Completed]" + task
                    print("Task marked as Completed: ", myList[completeTask])
            else:
                print("Invalid Task Index!")
        case 3:
            print("Enter the task index to remove from the List: ")
            index = int(input())
            if 1 <= index <= len(myList):
                removeTask = myList.pop(index - 1)
                print("Task removed: ", removeTask)
            else:
                print("Invalid Task Index!")
        case 4:
            print("Your Task List: \n")
            for i, item in enumerate(myList, start=1):
                print(f'{i}.{item}') 
        case 5:
            print("Exit the program. \nThank You for using To Do List.")
            break
        case _:
            print("Invalid Choice!!!")