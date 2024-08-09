import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.config(bg="#2E4053")  # Set the background color for the main window
        self.tasks = []

        self.setup_ui()
        self.load_tasks()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        # Task Entry
        self.task_entry = tk.Entry(self.root, width=40, bg="#F7DC6F", fg="#1F618D", font=("Helvetica", 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task Button
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task,
                                         bg="#28B463", fg="white", font=("Helvetica", 12))
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        # Tasks Listbox
        self.tasks_listbox = tk.Listbox(self.root, height=15, width=50, selectmode=tk.SINGLE,
                                        bg="#D5DBDB", fg="#212F3D", font=("Helvetica", 12))
        self.tasks_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Delete Task Button
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task,
                                            bg="#CB4335", fg="white", font=("Helvetica", 12))
        self.delete_task_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Mark Task Done Button
        self.mark_done_button = tk.Button(self.root, text="Mark Done", command=self.mark_task_done,
                                          bg="#3498DB", fg="white", font=("Helvetica", 12))
        self.mark_done_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
            self.tasks.pop(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def mark_task_done(self):
        try:
            selected_task_index = self.tasks_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            self.tasks[selected_task_index] = task + " [Done]"
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(selected_task_index, self.tasks[selected_task_index])
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as done.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for task in file:
                    self.tasks.append(task.strip())
                    self.tasks_listbox.insert(tk.END, task.strip())
        except FileNotFoundError:
            pass

    def on_closing(self):
        self.save_tasks()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

