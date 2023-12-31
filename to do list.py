class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f'Task "{task}" added to the to-do list.'

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f'Task "{task}" removed from the to-do list.'
        else:
            return f'Task "{task}" not found in the to-do list.'

    def view_tasks(self):
        if not self.tasks:
            return "No tasks in the to-do list."
        else:
            task_list = "\n".join(self.tasks)
            return f'To-Do List:\n{task_list}'

def main():
    to_do_list = ToDoList()

    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task to add: ")
            print(to_do_list.add_task(task))
        elif choice == "2":
            task = input("Enter the task to remove: ")
            print(to_do_list.remove_task(task))
        elif choice == "3":
            print(to_do_list.view_tasks())
        elif choice == "4":
            print("Exiting the To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
