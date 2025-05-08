# To-Do List Manager - CLI Version
# Author: [Your Name]
# Description: Simple command-line task manager with add/view/remove functionality.

from typing import List

def display_menu() -> None:
    """Displays the main menu options."""
    print("\n========== TO-DO LIST ==========")
    print("1️⃣  Add Task")
    print("2️⃣  View Tasks")
    print("3️⃣  Remove Task")
    print("4️⃣  Exit")
    print("================================")

def add_task(tasks: List[str]) -> None:
    """Adds a new task to the list."""
    task = input("➕ Enter the task to add: ").strip()
    if task:
        tasks.append(task)
        print("✅ Task added successfully.")
    else:
        print("⚠️  Task cannot be empty.")

def view_tasks(tasks: List[str]) -> None:
    """Displays all current tasks."""
    if not tasks:
        print("📭 Your to-do list is empty.")
    else:
        print("\n📝 Current Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(tasks: List[str]) -> None:
    """Removes a task by number or name."""
    if not tasks:
        print("❌ No tasks to remove.")
        return

    view_tasks(tasks)
    user_input = input("🗑️  Enter task number or exact name to remove: ").strip()

    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️  Task removed: {removed}")
        else:
            print("⚠️  Invalid task number.")
    else:
        if user_input in tasks:
            tasks.remove(user_input)
            print(f"🗑️  Task removed: {user_input}")
        else:
            print("⚠️  Task not found.")

def main() -> None:
    """Main application loop."""
    tasks: List[str] = []

    while True:
        display_menu()
        choice = input("👉 Select an option (1-4): ").strip()

        match choice:
            case '1':
                add_task(tasks)
            case '2':
                view_tasks(tasks)
            case '3':
                remove_task(tasks)
            case '4':
                print("👋 Exiting. See you soon!")
                break
            case _:
                print("❓ Invalid option. Please choose from 1 to 4.")

if __name__ == "__main__":
    main()