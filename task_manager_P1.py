# ===== Importing external modules ===========
'''This is the section where you will import modules'''

#to import the current date and set format
from datetime import datetime

#modify local file path here (if necessary)
FILE_NAME1 = "user.txt"
FILE_NAME2 = "tasks.txt"

# ==== Login Section ====
'''Implement the following functionality
     Here you will write code that will allow a user to login.
   - Your code must read usernames and passwords from the user.txt file
   - You can use a list or dictionary to store a list of usernames and passwords from the file.
   - Use a while loop to validate your user name and password.'''

#open the file user.txt and read the data from this file into a dictionary, 
#then it will validate the username and password entered. 

#empty dictionary for username and password tuples
login_dict = {}

#try open file and store data tuple in dictionary if the file exists
try:
    with open(FILE_NAME1, "r", encoding="utf-8") as file:

        for line in file:
            username, password = line.strip().split(", ")
            login_dict[username] = password
               
#incase if file not found, then display msg to user
except FileNotFoundError:
    print("Error! The file user.txt was not found")
    exit()

while True:
    #prompt for username and password
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    #check if the username provided exists and if the p/w provided matches the p/w on record
    if username in login_dict and login_dict[username] == password:
        print("Successfully logged in!")
        break
    else:
        #incase the username DNE or p/w do not match
        print("Invalid username or password entered. Please try again.")



while True:
    # Present the menu to the user and make sure that the user input is converted to lower case.
    #I modified the standard menu to be a bit more aesthetic than in the template
    
    #display menu for user
    print("\n**** Main Menu ****")
    print("1. Enter \"r\" to register a new user")
    print("2. Enter \"a\" to add a new task")
    print("3. Enter \"va\" to view all tasks")
    print("4. Enter \"vm\" to view my tasks")
    print("5. Enter \"e\" to exit")
    
    #convert user selection to lowercase to avoid errors
    menu = input("Enter selection: ").lower()


    #option to register new user 
    if menu == 'r':
        '''This code block will add a new user to the user.txt file
            - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file, otherwise present a relevant message'''
        
        new_user = input("Enter an username for the new user: ")
        
        #if the username already exists in txt file
        if new_user in login_dict:
            print("The username you have entered already exists!")
            continue

        #prompt for new p/w and confirmation p/w 
        new_pw = input("Enter the password for the new user: ")
        confirm_pw = input("Please confirm your password: ")

        #check if the passwords match, else display error to user
        if new_pw != confirm_pw:
            print("The passwords you have entered do not match!")
            continue
        
        #write to file in tuple format 
        with open(FILE_NAME1, "a", encoding="utf-8") as file:
            file.write(f"\n{new_user}, {new_pw}")

        #create username and p/w pair
        login_dict[new_user] = new_pw
        print("New user has been created successfully.")  


    #if user selects to add a new task
    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        
        #get data for tasks using input and get current date and time using function
        task_user = input("Please enter the username associated with this task: ")
        task_title = input("Please enter the title of this task: ")
        task_desc = input("Please enter a short description of the task")
        due_date = input("Please enter the task deadline (e.g. 23 Feb 2026)")
        date_assigned = datetime.today().strftime("%d %b %Y")
        completed = "No"

        #append new task to file
        with open(FILE_NAME2, "a", encoding="utf-8"):
            file.write(f"\n {task_user}, {task_title}, {task_desc}, {due_date}, {date_assigned}, {completed}")
        print("New task successfully created. ")


    #if user selects to view all tasks
    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        
        #read contents from file and clean data
        with open(FILE_NAME2, "r", encoding="utf-8") as file:
            for line in file:
                contents = line.strip().split(", ")

                #display task data in the format provided in template
                print("\n-------------------------------")
                print(f"Assigned to:\t {contents[0]}")
                print(f"Task:\t\t {contents[1]}")
                print(f"Description:\t {contents[2]}")
                print(f"Date assigned:\t {contents[3]}")
                print(f"Due date:\t {contents[4]}")
                print(f"Completed:\t {contents[5]}")
                print("-------------------------------")


    #if selects to view only their task
    elif menu == 'vm':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have read from the file.
            - If they are the same you print the task in the format of Output 2 shown in the PDF '''
        
        # read contents from file and clean data
        with open(FILE_NAME2, "r", encoding="utf-8") as file:
            for line in file:
                contents = line.strip().split(", ")
        
                #display task data in desired format if it matches with username
                if contents[0] == username:       
                    print("\n-------------------------------")
                    print(f"Assigned to:\t {contents[0]}")
                    print(f"Task:\t\t {contents[1]}")
                    print(f"Description:\t {contents[2]}")
                    print(f"Date assigned:\t {contents[3]}")
                    print(f"Due date:\t {contents[4]}")
                    print(f"Completed:\t {contents[5]}")
                    print("-------------------------------")
        
   
    #incase user decides to exit
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")