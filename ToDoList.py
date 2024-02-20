def display_menu():
    print("\nCommand Menu:")
    print("  1. Add Task")
    print("  2. View Tasks")
    print("  3. Mark Task Complete")
    print("  4. Delete Task")
    print("  5. Quit")


def add_task(tasks):
    task_name = input("Enter task name: ")
    tasks[task_name] = False
    print(f"'{task_name}' added to the to-do list.")


def view_tasks(tasks):
    print("\nTo-Do List:")
    for index, (task, completed) in enumerate(tasks.items(), start=1):
        status = "Done" if completed else "Pending"
        print(f"{index}. [{status}] {task}")


def mark_task_complete(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to mark as complete: ")) - 1
    task_name = list(tasks.keys())[task_index]
    tasks[task_name] = True
    print(f"'{task_name}' marked as complete.")


def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter task number to delete: ")) - 1
    task_name = list(tasks.keys())[task_index]
    del tasks[task_name]
    print(f"'{task_name}' deleted from the to-do list.")


def main():
    tasks = {}

    while True:
        display_menu()
        choice = input("\nEnter command: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
