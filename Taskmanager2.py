from datetime import datetime
from datetime import date
lines_count = 0
def reg_new_user():
        new_password = input("please enter new user and password (user, password): ")
        new_split = new_password.split(", ")
        with open('user.txt', 'r+') as user_file:
            for line in user_file.readlines():
                line = line.strip()
                login_credentials = line.split(", ")

        if new_split[0] == login_credentials[0] and new_split[1] == login_credentials[1]:
            print("Error: user and password already exsists")
            exit()

        elif new_split[0] != login_credentials[0] and new_split[1] != login_credentials[1]:
                with open('user.txt', 'a') as f:
                    f.write('\n' + new_password)  # writes new user and password
                    print("New user and password has been added to 'user.txt'.")

def add_task():
    new_task = input("enter the username, the title of the task, the description, and the due date of the task: \n")
    new_task = new_task.split(", ")
    n_assigned_to = (new_task[0])
    n_task = (new_task[1])
    n_task_description = (new_task[2])
    n_due_date = (new_task[3])
    n_date_assigned = str(date.today())
    n_completion = "no" #adds new task

    with open('tasks.txt', 'a') as f2:
        f2.write(f"\n{n_assigned_to}, {n_task}, {n_task_description}, {n_date_assigned}, {n_due_date}, {n_completion}")
    print("New task has been added to 'tasks.txt'.")

def view_all():
    source = open('tasks.txt', 'r+')
    for line in source.readlines():
        line = line.split(", ")
        print("Task:\t\t\t\t" + (line[1]))
        print("Assigned to:\t\t" + (line[0]))
        print("Date assigned:\t\t" + (line[3]))
        print("Due date:\t\t\t" + (line[4]))
        print("Task complete?:\t\t" + (line[5]))
        print("Task_description: \n" + (line[2]))
        print("\n")
    source.close()

def menu():
    if access == True:
        current_user = username
        print(f"welcome {username}")
        print("Please select one of the following options: ")
        if username == "admin":  # set for only admin
            print("r - register user")
        print("a - add task")
        print("va - view all tasks")
        print("vm - view my tasks")
        print("e - exit")
        if username == "admin":  # set for only admin
            print("s - statistics")

        selection = input("")

    # create condition to append new passwords
    if selection == "r":
        if username == "admin":
            reg_new_user()

    elif selection == "a":
        add_task()

    # view current tasks
    elif selection == "va":
        view_all()
    # view specific current tasks
    elif selection == "vm":
        source = open('tasks.txt', 'r+')
        for line in source.readlines():
            line = line.split(", ")
            lines_count = 0
            lines_count += 1
            if line[0] == username:  # shows tasks for specific users only
                print("task:" + str(lines_count))
                print("Task:\t\t\t\t" + (line[1]))
                print("Assigned to:\t\t" + (line[0]))
                print("Date assigned:\t\t" + (line[3]))
                print("Due date:\t\t\t" + (line[4]))
                print("Task complete?:\t\t" + (line[5]))
                print("Task_description: \n" + (line[2]))
                print("\n")
                source.close()
        task_selection = int(input("which task would you like to modify? alternatively type -1 to go back: "))
        if task_selection == -1:
            menu()
        else:
            task_selection = task_selection - 1
            print("what would you like to modify on the task?")
            print("c - \t\tchange status of completion from yes to no?")
            print("a - \t\tchange who the task is assigned to?")
            print("d - \t\tchange the due date")
            task_mod = input("")

            if task_mod == "c":
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (
                            change[0] + ", " + change[1] + ", " + change[2] + ", " + change[3] + ", " + change[
                        4] + ", " + "yes" '\n')
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("task status has been updated")

            elif task_mod == "a":
                new_user = input("Who has the task been assigned to?: ")
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (f"{new_user}, {change[1]}, {change[2]}, {change[3]}, {change[4]}, {change[5]}")
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("The user has been updated")
                    source.close()

            elif task_mod == "d":
                new_due_date = input("please enter the new due date: ")
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (
                    f"{change[0]}, {change[1]}, {change[2]}, {change[3]}, {new_due_date}, {change[5]}")
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("The new due date has been updated")
                    source.close()

    if selection == "s":
        if username == "admin":
            source = open('tasks.txt', 'r+')  # provides a count for users and passwords
            line_count = len(source.readlines())
            print("Amount of tasks:\t\t" + str(line_count))
            source.close()
            source = open('user.txt', 'r+')
            line_count = len(source.readlines())
            print("Amount of users:\t\t" + str(line_count))
            source.close()
    else:
        exit()

def task_overview():
    source = open('tasks.txt', 'r+')  # provides a count for users and passwords
    line_count = len(source.readlines())
    number_of_tasks = str(line_count)

    source = open('tasks.txt', 'r+')
    completed_tasks = 0
    for line in source.readlines():
        line = line.split(', ')
        if line[5] == "yes\n":
            completed_tasks += 1

    source = open('tasks.txt', 'r+')
    incomplete_tasks = 0
    for line in source.readlines():
        line = line.split(', ')
        if line[5] == "no\n":
            incomplete_tasks += 1

    overdue_tasks = 0
    source = open('tasks.txt', 'r+')
    for line in source.readlines():
        line = line.split(', ')
        today = str(date.today())
        today = datetime.strptime(today, "%Y-%m-%d")
        due_date = line[4]
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
        if today > due_date and line[5] == "no\n":
            overdue_tasks += 1

    incomplete_percentage = int(number_of_tasks)/int(incomplete_tasks)*100

    overdue_percentage = int(overdue_tasks)/int(number_of_tasks)*100

    overview1 = ("Task Overview: "+'\n')
    overview2 = ("The total number of tasks to date are: " + str(number_of_tasks)+'\n')
    overview3 = ("The total number of completed tasks to date are: " + str(completed_tasks)+'\n')
    overview4 = ("The total number of incomplete tasks to date are: " + str(incomplete_tasks)+'\n')
    overview5 = ("The total number of overdue tasks to date are: " + str(overdue_tasks)+'\n')
    overview6 = ("to date : " + str(incomplete_percentage) + "% of tasks are incomplete"+'\n')
    overview7 = ("to date : " + str(overdue_percentage) + "% of tasks are overdue"+'\n')

    print(overview1 + overview2 + overview3 + overview4 + overview5 + overview6 + overview7)
    with open('task_overview.txt', 'w') as f:
        f.write(overview1 + overview2 + overview3 + overview4 + overview5 + overview6 + overview7)  # writes new password
        print("Task Overview has been generated and saved as task_overview.txt\n")#generates stats and displays them, conditions set if new tasks are added

def user_overview():
    useroverview = []
    assignment = 0
    source = open('tasks.txt', 'r+')  # provides a count for users and passwords
    line_count = len(source.readlines())
    total_tasks = line_count

    user_file = open('user.txt', 'r+')
    for line in user_file.readlines():
        line = line.strip()
        user = line.split(", ")

        tasks = 0
        task_file = open('tasks.txt', 'r+')
        for line in task_file:
            line = line.split(", ")
            task = line
            if user[0] == task[0]:
                tasks += 1

        incomplete_tasks = 0
        task_file = open('tasks.txt', 'r+')
        for line in task_file:
            line = line.split(", ")
            task = line
            if user[0] == task[0] and task[5] == "no\n":
                incomplete_tasks += 1

        overdue_tasks = 0
        task_file = open('tasks.txt', 'r+')
        for line in task_file:
            line = line.split(", ")
            task = line
            today = str(date.today())
            today = datetime.strptime(today, "%Y-%m-%d")
            due_date = task[4]
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
            if user[0] == task[0] and task[5] == "no\n" and today > due_date:
                overdue_tasks += 1

        overdue_percentage = int(tasks) / int(overdue_tasks) * 100
        incomplete_task_percent = int(tasks) / int(incomplete_tasks) * 100
        task_percent = int(tasks) / int(total_tasks) * 100

        user_overview = (
            f"username:{user[0]}, total amount of tasks:{tasks}. task percentage out of total amount of tasks: {task_percent}%, total percentage of tasks incomplete ={incomplete_task_percent}%, the percentage of overdue tasks are:{overdue_percentage}%.\n")
        user_overview = (''.join(user_overview))
        useroverview.append(user_overview)
        print("User overview:")
        print(user_overview)#generates data and displays for each user, conditions set if a new user is added

    with open('user_overview.txt', 'w') as f2, open('user.txt', 'r') as f:
        f2.writelines(useroverview)
        print("User overview has been generated and saved as user_overview.txt")

access = False
current_user = ""

#set conditions to loop if invalid user and password is given and allow access if correct details is submitted
while access == False:
    with open('user.txt', 'r+') as user_file:
        username = input("Please enter your name: ")
        password = input("Please enter your password: ")
        username = username.strip()
        password = password.strip()

        for line in user_file.readlines():
            line = line.strip()
            login_credentials = line.split(", ")

            if username == login_credentials[0] and password == login_credentials[1]:
                access = True

    if access == False:
        print("Invalid user and password")
#set menu
if access == True:
    current_user = username
    print(f"welcome {username}")
    print("Please select one of the following options: ")
    if username == "admin": #set for only admin
        print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    if username == "admin": #set for only admin
        print("gr - generate reports")
        print("ds - display statistics")
    selection = input("")

# create condition to append new passwords
if selection == "r":
    if username == "admin":
        reg_new_user()

elif selection == "a":
    add_task()

# view current tasks
elif selection == "va":
    view_all()
# view specific current tasks
elif selection == "vm":
    source = open('tasks.txt', 'r+')
    for line in source.readlines():
        line = line.split(", ")
        lines_count += 1
        if line[0] == username: #shows tasks for specific users only
            print("task:" + str(lines_count))
            print("Task:\t\t\t\t" + (line[1]))
            print("Assigned to:\t\t" + (line[0]))
            print("Date assigned:\t\t" + (line[3]))
            print("Due date:\t\t\t" + (line[4]))
            print("Task complete?:\t\t" + (line[5]))
            print("Task_description: \n" + (line[2]))
            print("\n")
            source.close()
    task_selection = int(input("which task would you like to modify? alternatively type -1 to go back: "))
    if task_selection == -1:
        menu()
    else:
        task_selection = task_selection - 1
        source = open('tasks.txt', 'r+')
        data = source.readlines()
        range = int(len(data))
        change = data[task_selection].split(', ')

        if change[5] == "no":
            print("what would you like to modify on the task?")
            print("c - \t\tchange status of completion from yes to no?")
            print("a - \t\tchange who the task is assigned to?")
            print("d - \t\tchange the due date")
            task_mod = input("")

            if task_mod == "c":
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (change[0] + ", " + change[1] + ", " + change[2] + ", " + change[3] + ", " + change[4] + ", " + "yes" '\n')
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("task status has been updated")#changes task status to and rewrites files

            elif task_mod == "a":
                new_user = input("Who has the task been assigned to?: ")
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (f"{new_user}, {change[1]}, {change[2]}, {change[3]}, {change[4]}, {change[5]}")
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("The user has been updated")
                    source.close() #changes person assigned to and rewrites files

            elif task_mod == "d":
                new_due_date = input("please enter the new due date: ")
                source = open('tasks.txt', 'r+')
                data = source.readlines()
                range = int(len(data))
                change = data[task_selection].split(', ')
                data[task_selection] = (f"{change[0]}, {change[1]}, {change[2]}, {change[3]}, {new_due_date}, {change[5]}")
                with open('tasks.txt', 'r+') as f2:
                    f2.write(''.join(data))
                    print("The new due date has been updated")
                    source.close()#changes due date and rewrites files
        else:
            print("This task has already been completed")#prevents modifying a completed task

if selection == "ds":
    if username == "admin":
        source = open('tasks.txt', 'r+')
        line_count = len(source.readlines())#number of lines = number of tasks
        print("Amount of tasks:\t\t" + str(line_count))
        source.close()
        source = open('user.txt', 'r+')
        line_count = len(source.readlines())#number of users = number of lines
        print("Amount of users:\t\t" + str(line_count))
        source.close()

if selection == "gr":
    if username == "admin":
        task_overview()
        user_overview()
else:
    exit()
#End finally