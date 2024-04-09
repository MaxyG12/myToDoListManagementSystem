print("TODO List Management System")
print()

# Initialize a list of dictionaries to store tasks
todoList = []

def printList():
    print("\n{:<20} {:<15} {:<10}".format("Task", "Deadline", "Priority"))
    print("-" * 45)
    for item in todoList:
        print("{:<20} {:<15} {:<10}".format(item["task"], item["deadline"], item["priority"]))
    print()

while True:
    menu = input("Do you want to view, add, edit, or remove an item from your to-do list? ")
    if menu == "add":
        item = input("What do you want to add? ")
        dueDate = input("When is it due? ")
        priority = input("What is the priority? (High/Medium/Low): ")

        # Create a dictionary for the task
        task_dict = {"task": item, "deadline": dueDate, "priority": priority}
        todoList.append(task_dict)

    elif menu == "view":
        allOrPriority = input("Do you want to view all or view by priority? ")
        if allOrPriority.strip().lower()[0] == "a":
            printList()
        elif allOrPriority.strip().lower()[0] == "p":
            priority = input("What priority? (High/Medium/Low): ")
            for task in todoList:
                if task["priority"].lower() == priority.lower():
                    print(f"{task['task']}'s priority is {task['priority']}")

    elif menu == "edit":
        item = input("What task do you want to change? ")
        new_task = input("What do you want to change it to? ")
        for task in todoList:
            if task["task"] == item:
                task["task"] = new_task

    elif menu == "remove":
        item = input("What task do you want to remove? ")
        check = input(f"Are you sure you want to remove '{item}'? (y/n): ")
        if check.strip().lower() == "y":
            todoList = [task for task in todoList if task["task"] != item]
        else:
            print(f"{item} was not removed.")

    elif menu == "exit":
        break
    else:
        print("Invalid option. Please choose 'add', 'view', 'edit', 'remove', or 'exit'.")

  