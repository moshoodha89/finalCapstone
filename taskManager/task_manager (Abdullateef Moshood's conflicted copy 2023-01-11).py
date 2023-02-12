#=====importing libraries===========
'''This is the section where you will import libraries'''

from getpass import getuser


#===section to write the usernames and passwords into the user.txt file==#



#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
db_username = []
db_password = []
logged_in_user = ""
username = ""

def user_login():
    with open('user.txt', 'r') as db:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        # here, I'm pulling out the username and password from the user.txt file and splitting them
        global db_username
        global db_password
        global logged_in_user
        for i in db:
            a,b = i.split(', ')
            b = b.strip()
            db_username.append(a)
            db_password.append(b)
        data = dict(zip(db_username, db_password)) # I had to make them into a dictionary to use them
        
        # I'm checking if the username and password match
        if username in db_username and password in db_password:
            
            print("\n")
            logged_in_user = [x for x in db_username if x.startswith(username)]
            logged_in_user = ''.join(logged_in_user)

            # NOTE: Do something about the logged_in_user below
            print(f"You're logged on as {logged_in_user}. Welcome back!")
            
        else:
            print("Oops, username or password is wrong! Please try again")
            user_login()
user_login()


           
print("\n")
            
#====New Account Creation====

'''In this block you will write code to add a new user to the user.txt file
    - You can follow the following steps:
    - Request input of a new username
    - Request input of a new password
    - Request input of password confirmation.
    - Check if the new password and confirmed password are the same.
    - If they are the same, add them to the user.txt file,
    - Otherwise you present a relevant message.'''


menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

if menu == 'r':
    
    def create_user():
        with open('user.txt', 'a') as db: # now changed from 'w' to 'a' to enable adding new details below the user.txt doc
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            password1 = input("Enter password again: ")
            if password != password1:
                print("Password do not match! Please try again")
                create_user()
            else:
                with open('user.txt', 'a') as db:
                    db.write(username+', '+password+'\n')
                    print("Success. Account created!")
    create_user()



#====Adding New Task====
    '''In this block you will put code that will allow a user to add a new task to task.txt file
         - You can follow these steps:
             - Prompt a user for the following: 
                 - A username of the person whom the task is assigned to,
                 - A title of a task,
                 - A description of the task and 
                 - the due date of the task.
             - Then get the current date.
             - Add the data to the file task.txt and
             - You must remember to include the 'No' to indicate if the task is complete.'''

elif menu == 'a':
        
      # Now, I will write the details above into the tasks.txt file
        def assign_task():  
            with open('T21/tasks.txt', 'a') as f:
                username = input("Please enter the username of the person you want to assign the task to: ")
                task = input("Please enter the title of the task: ")
                description = input("Please enter the task description: ")
                due_date = input("Please enter the task due date: ")
                date_assigned = "22 Dec 2022"
                status = "No"
                f.write(username+', '+task+', '+description+', '+due_date+', '+date_assigned+', '+status+'\n')
                print("Success")
        
        assign_task()

   
#====Vieweing All Task====


elif menu == 'va':
    
    with open('T21/tasks.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip()
            temp = temp.split(", ")
            print("-"*100)
            headers = [
                'Assigned To  ',
             'Task         ', 
            'Description  ', 
            'Due Date     ', 
            'Date Assigned', 
            'Completed?   ']  
            for t, s in zip(headers, temp):
                gap = ' '*10
                print('{}:{}{}'.format(t,gap,s))
            print("-"*100)


    
        

elif menu == 'vm':

 
    
    def display_tasks():
    # Read the tasks from the file
        with open('T21/tasks.txt', 'r') as f:
            global username
            tasks = f.readlines()

        # Filter the tasks based on the username
        filtered_tasks = [task for task in tasks if task.startswith(logged_in_user)]
        print(filtered_tasks)
        
    display_tasks()
        



elif menu == 'e':
    print('Goodbye!!!')
    exit()

else:
    print("You have made a wrong choice, Please Try again")