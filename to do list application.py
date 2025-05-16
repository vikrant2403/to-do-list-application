# to-do-list-application
#to-do list application
#1. view tasks
#2. add a task
#2.1 personal
#2.2 work
#3. remove a task
#4. completed task
#5. show completed tasks
#4.exit
tasks = []
show_completed_tasks = []
personal =[]
work = []
while True:
    print("Welcome to the To Do list application made by Vikrant Sheokand\n--------------------------------\n")
    print("1. view tasks\n2. add a task\n3. remove a task\n4. task completed\n5.exit")
    user_choice = int(input("enter your choice(1-4): "))
    if user_choice == 2:
        new_task = input("enter a task you want to add: ")
        tasks.append(new_task)
        ask_userspecifications =input("is this personal or work related(P or W): ").upper()
        if ask_userspecifications == "P":
            personal.append(ask_userspecifications)
        elif ask_userspecifications == "W":
            work.append(ask_userspecifications)
        print("task successfully added.\n thank you")
        continue

    if user_choice == 1:
        task_choice = input("Which task you want to fetch(all,personal,work,completed): ").lower()
        if task_choice=="all":
           print(f"your tasks to do are :\n{tasks}")
        elif task_choice == "work":
            print(f"your work tasks are :\n{work}")
        elif task_choice == "personal":
            print(f"your personal tasks are :\n{personal}")
        elif task_choice == "completed":
            print(f"your completed tasks are :\n{completed}")



    if user_choice == 3:
        remove_task = input("enter your task to remove: ")
        tasks.remove(remove_task)
        print(f"your task removed successfully")
        print(f"your pending tasks to do are:\n{tasks}")

    if user_choice == 4:
        completed_task = input("enter the task which you have completed: ")
        tasks.remove(completed_task)
        show_completed_tasks.append(completed_task)
        ask_user = input("do you want to see your completed tasks(yes/no): ")
        if ask_user == "yes":
            print(f"here your completed tasks are:{show_completed_tasks}")

    if user_choice == 5:
        break


