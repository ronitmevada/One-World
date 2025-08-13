import os

FILE_NAME = "tasks.txt"

# --- Helper Functions ---
def load_tasks():
    tasks = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# --- Main Menu Functions ---
def show_tasks(tasks):
    if not tasks:
        print("\n📭 No tasks found!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("\nEnter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("\nEnter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f"❌ Deleted: {removed}")
        else:
            print("⚠ Invalid task number!")
    except ValueError:
        print("⚠ Please enter a valid number!")

# --- Main Program ---
def main():
    tasks = load_tasks()
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
