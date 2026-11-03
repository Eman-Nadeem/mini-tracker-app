
import json

tasks = []
not_exit = True


# Load saved tasks
def load_task():
    global tasks

    try:
        with open('tasks.json', 'r') as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


# Save tasks
def save_task():
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f, indent=4)


# Add a new task
def add_task():
    title = input("Enter task title: ").strip()

    if not title:
        print("Task name cannot be empty!")
        return

    tasks.append({"title": title, "done": False})
    save_task()

    print("Task added successfully!")


# View all tasks
def view_task():
    if not tasks:
        print("No tasks available!")
        return

    print("\n--- YOUR TASKS ---")

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f'{index}. {task["title"]} [{status}]')


# Complete a task
def complete_task():
    view_task()

    if not tasks:
        return

    try:
        task_number = int(input(
            "\nEnter the task number to mark as completed: "
        ))

        if 1 <= task_number <= len(tasks):
            index = task_number - 1

            if not tasks[index]["done"]:
                tasks[index]["done"] = True
                save_task()
                print("Task completed successfully!")
            else:
                print("This task is already completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Delete a task
def delete_task():
    view_task()

    if not tasks:
        return

    try:
        task_number = int(input(
            "\nEnter the task number to delete: "
        ))

        if 1 <= task_number <= len(tasks):
            index = task_number - 1

            del tasks[index]
            save_task()

            print("Task deleted successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Exit program
def exit_menu():
    global not_exit
    not_exit = False
    print("Exiting the program. Goodbye!")


# Load tasks when program starts
load_task()


# Main menu
while not_exit:
    print("\n--- TASK TRACKER ---")
    print("1. Add")
    print("2. View")
    print("3. Complete")
    print("4. Delete")
    print("5. Exit")

    choice = input("\nChoice: ").strip()

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        exit_menu()
    else:
        print("Invalid choice! Please select 1-5.")
