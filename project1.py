# Function to display the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

# define an empty list to store tasks
tasks = []

# function to add a task
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# function to remove a task
def remove_task():
    view_tasks()
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1) #to remove the task we use pop() function
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")

#Main Program Loop(main section of the program)
if __name__== "__main__" :
    print("Welcome to the To Do List app")
    print("----------------------------------------")
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
