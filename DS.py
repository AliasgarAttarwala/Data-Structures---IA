import tkinter as tk
#first
class Task:
    def __init__(self, day, month, year, hour, description):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour
        self.description = description
        self.next = None

class TaskList:
    def __init__(self):
        self.head = None

    def add_task(self, day, month, year, hour, description):
        new_task = Task(day, month, year, hour, description)
        new_task.next = self.head
        self.head = new_task

    def display_tasks(self):
        tasks = []
        current_task = self.head
        while current_task:
            tasks.append((current_task.hour, current_task.description))
            current_task = current_task.next
        return tasks

def get_month_name(month):
    return {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }.get(month, "Invalid Month")

def days_in_month(month):
    return {
        4: 30,
        6: 30,
        9: 30,
        11: 30,
        2: 28,
    }.get(month, 31)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.task_list = TaskList()
        self.day = 1
        self.month = 1
        self.year = 2023
        self.num_tasks = 0
        self.create_widgets()

    def create_widgets(self):
        self.num_tasks_label = tk.Label(self.master, text="How many tasks do you have?")
        self.num_tasks_label.pack()
        self.num_tasks_entry = tk.Entry(self.master)
        self.num_tasks_entry.pack()
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
        self.quit_button.pack()

    def add_task(self):
        self.num_tasks = int(self.num_tasks_entry.get())
        self.num_tasks_label.destroy()
        self.num_tasks_entry.destroy()
        self.add_task_button.destroy()

        if self.num_tasks == 0:
            return

        self.day_label = tk.Label(self.master, text="Enter task day and month (e.g., 20th October): ")
        self.day_label.pack()
        self.day_entry = tk.Entry(self.master)
        self.day_entry.pack()
        self.description_label = tk.Label(self.master, text="Enter task description: ")
        self.description_label.pack()
        self.description_entry = tk.Entry(self.master)
        self.description_entry.pack()
        self.hour_label = tk.Label(self.master, text="Enter task hour (e.g., 8): ")
        self.hour_label.pack()
        self.hour_entry = tk.Entry(self.master)
        self.hour_entry.pack()
        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_task)
        self.submit_button.pack()

    def submit_task(self):
        day, month_str = self.day_entry.get().split()
        self.day = int(day[:-2])
        self.month = {
            "jan": 1,
            "feb": 2,
            "mar": 3,
            "apr": 4,
            "may": 5,
            "jun": 6,
            "jul": 7,
            "aug": 8,
            "sep": 9,
            "oct": 10,
            "nov": 11,
            "dec": 12
        }.get(month_str.lower(), 1)
        description = self.description_entry.get()
        hour = int(self.hour_entry.get())
        self.task_list.add_task(self.day, self.month, self.year, hour, description)

        self.day_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.hour_entry.delete(0, tk.END)

        self.num_tasks -= 1
        if self.num_tasks == 0:
            self.day_label.destroy()
            self.day_entry.destroy()
            self.description_label.destroy()
            self.description_entry.destroy()
            self.hour_label.destroy()
            self.hour_entry.destroy()
            self.submit_button.destroy()
            self.display_tasks()

    def display_tasks(self):
        tasks = self.task_list.display_tasks()
        tasks_str = "\n".join([f"{hour}\t{description}" for hour, description in tasks])
        tasks_label = tk.Label(self.master, text=f"All Tasks:\nHour\tTask\n{tasks_str}")
        tasks_label.pack()

        continue_input = tk.messagebox.askyesno("Continue?", "Do you want to continue entering tasks?")
        if continue_input:
            self.add_task()
        else:
            self.quit_button.pack_forget()
            self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)
            self.quit_button.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()