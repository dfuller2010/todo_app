# Python Software Development Project: To-Do List Application

import json
tasks = []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"'{task}' added to your list.")

def view_tasks():
    if len(tasks) == 0:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_number = input("\nEnter the task number to mark complete: ")
    index = int(task_number) - 1
    tasks[index] = tasks[index] + " ✓"
    print(f"Task marked complete.")

def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    task_number = input("\nEnter the task number to delete: ")
    index = int(task_number) - 1
    removed_task = tasks.pop(index)
    print(f"'{removed_task}' deleted.")

def main():
    load_tasks()
    while True:
        print("\nWhat would you like to do?")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Quit")

        choice = input("\nEnter your choice (1-5): ")

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

main()

