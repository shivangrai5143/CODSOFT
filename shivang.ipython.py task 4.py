# TO DO LIST APPLICATION

class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_menu(self):
        print("\nTo-Do List Menu:")
        print("1. Show all tasks")
        print("2. Add a task")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Quit")

    def show_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def add_task(self):
        task = input("Enter a task: ")
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def update_task(self):
        self.show_tasks()
        task_number = int(input("Enter the task number to update: "))
        task = input("Enter the updated task: ")
        self.tasks[task_number - 1] = task
        print(f"Task {task_number} updated!")

    def delete_task(self):
        self.show_tasks()
        task_number = int(input("Enter the task number to delete: "))
        del self.tasks[task_number - 1]
        print(f"Task {task_number} deleted!")

def main():
    todo_list = ToDoList()

    while True:
        todo_list.show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.show_tasks()
        elif choice == "2":
            todo_list.add_task()
        elif choice == "3":
            todo_list.update_task()
        elif choice == "4":
            todo_list.delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()