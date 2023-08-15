"""
Task-2: Managing a ToDo List
1. Create a Python class named Task.
2. Define the following methods within the Task class:
	set_task_detail(self, task_name, priority)
	mark_as_complete(self)
	display_task_info(self)
3. Create an object of the Task class.
4. Use the set_task_details method to set the task_name, and task’s priority.
5. Use the mark_as_complete method to mark the task as completed.
6. Finally, use the display_task_info method to print the toDo List.
"""

class Task:
    completed = False
    def set_task_detail(self, task_name, priority):
        self.task_name = task_name
        self.priority = priority
    def mark_as_complete(self):
        self.completed = True
    def display_task_info(self):
        print("Task Name:", self.task_name)
        print("Priority:", self.priority)
        print("Completed:", self.completed)

task1 = Task()
task_name = input("Enter Task Name: ")
priority = input("Enter Priority (Low/Medium/High): ")
priority = priority.lower()
while priority != "low" and priority != "medium" and priority !="high":
    print("Invalid Input")
    priority = input("Enter Priority (Low/Medium/High): ")
    priority = priority.lower()
else:
    task1.set_task_detail(task_name, priority)

    choise = input("Do you want to mark this task as completed? (y/n): ")
    choise = choise.lower()
    while choise != "n" and choise != "y":
        print("Invalid Input")
        choise = input("Do you want to mark this task as completed? (y/n): ")
        choise = choise.lower()

    if choise == "y":
        task1.mark_as_complete()

    print()
    task1.display_task_info()