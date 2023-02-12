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
            logged_in_user = db_username
            print("\n")
            print(f"You're logged on {logged_in_user}. Welcome back!")
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
    # pass
    
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
        # pass
        
      # Now, I will write the details above into the tasks.txt file
        def assign_task():  
            with open('tasks.txt', 'a') as f:
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
# '''In this block you will put code so that the program will read the task from task.txt file and \
#     print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#          You can do it in this way:
#             - Read a line from the file.
#             - Split that line where there is comma and space.
#             - Then print the results in the format shown in the Output 2 
#             - It is much easier to read a file using a for loop.'''

elif menu == 'va':
    # pass
    with open('tasks.txt', 'r') as f:
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
        # pass
        # if db_username == "'mosh'":
        if logged_in_user == "mosh":
            print("good")
        else:
            print("bad")
        print(logged_in_user)
        # def user_login():
        #     with open('user.txt', 'r') as f:
        #         lines = f.readlines()
        #         for line in lines:
        #             login_details = line.strip().split(',')
        #             if login_details[0] == db_username and login_details[1] == db_password:
        #                 logged_in_user = db_username
        #                 return True
        #             return False
       
        #     if user_login():
        #         print('Welcome, {}!'.format(logged_in_user))
        #     else:
        #         print('Sorry, invalid login details. Please try again.')

        #     with open('user.txt', 'r') as f:
        #         # db_username = [line.split(", ")[0] for line in f]
        #         # db_password = [line.strip()[1] for line in f]
        #         # print(db_username, db_password)
        #         for line in f:
        #             parts = line.strip().split(":")
        #             if parts[0] == username and parts[1] == password:
        #                 print(username, password)
        #                 return True
        #             else:
        #                 return False
                
        # check_login("mosh", "mosh123")     

        # if user_login():
        #     current_user = db_username
        #     print(current_user)
        #     # with open('tasks.txt', 'r') as f:
        #     #     for line in f:
        #     #         print(line.strip())
        # else:
        #     print("invalid login")      

            # username == islogin()
            # print(checkuser)
            
            # for user in username:
            #     if user == checkuser:
            #         print("Oh yea")
        # here, I'm pulling out the username and password from the user.txt file and splitting them
            # db_username = []
            # db_password = []
            # for i in f:
            #     a,b = i.split(', ')
            #     b = b.strip()
            #     db_username.append(a)
            #     # db_username = db_username.append(a)
            #     print(db_username)
                # db_password.append(b)
        # data = dict(zip(db_username, db_password)) # I had to make them into a dictionary to use them
        




            # for line in f:
                
            #     if line.strip == username:
            #         with open('task.txt', 'r') as f:
            #             lines = f.readlines()
            #             for line in lines:
            #                 task_view = line.split("\n")
            #                 print(task_view)

            

#         '''In this block you will put code the that will read the task from task.txt file and
#          print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
#          You can do it in this way:
#             - Read a line from the file
#             - Split the line where there is comma and space.
#             - Check if the username of the person logged in is the same as the username you have
#             read from the file.
#             - If they are the same print it in the format of Output 2 in the task PDF'''

elif menu == 'e':
    print('Goodbye!!!')
    exit()

else:
    print("You have made a wrong choice, Please Try again")