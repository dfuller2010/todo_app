# Python Software Development Project: To-Do List Application

import json

# Store the current list of tasks in memory for the session.
tasks = []

# Load any previously saved tasks from the JSON file when the app starts.
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

# Save the in-memory task list to disk so it can be restored later.
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
        
# Add a new task entered by the user to the task list.
def add_task():
    task = input("Enter your task: ") 
    tasks.append(task)
    print(f"'{task}' added to your list.")

# Display all current tasks or show a message when the list is empty.
def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

# Mark a selected task as complete by adding a checkmark to it.
def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_number = input("\nEnter the task number to mark complete: ")
    index = int(task_number) - 1
    tasks[index] = tasks[index] + " ✓"
    print("Task marked complete.")

# Remove a chosen task from the list after confirming the selection.
def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_number = input("\nEnter the task number to delete: ")
    index = int(task_number) - 1
    removed_task = tasks.pop(index)
    print(f"'{removed_task}' deleted.")

# Run the main interactive menu loop for the application.
def main():
    load_tasks()
    while True:
        # Show the available actions to the user.
        print("\nWhat would you like to do?")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

        # Handle the user-selected action.
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the program when the script is executed directly.
main()

