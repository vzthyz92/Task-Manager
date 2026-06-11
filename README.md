# Task Manager - Part 1

## Overview

Task Manager is a command-line Python application that allows users to manage tasks and user accounts through a simple text-based interface.

This project demonstrates fundamental Python programming concepts including:

- File handling
- Dictionaries
- Loops and conditionals
- User authentication
- Date handling
- Basic task management

## Features

### User Authentication
- Login using credentials stored in `user.txt`
- Validation of usernames and passwords
- Error handling for missing user files

### User Registration
- Register new users
- Prevent duplicate usernames
- Password confirmation validation

### Task Management
- Add new tasks
- Assign tasks to users
- Store task details in `tasks.txt`
- Automatically record task creation date

### Task Viewing
- View all tasks
- View tasks assigned to the currently logged-in user

## Technologies Used

- Python 3
- File I/O
- Datetime Module





# Task Manager - Part 2

## Overview

Task Manager Part 2 expands upon the original task management system by introducing role-based access control and advanced task administration features.

The application allows users to manage tasks while giving administrators additional privileges such as viewing completed tasks and deleting tasks.

## Features

### User Authentication
- Secure login validation using stored credentials
- User data stored in `user.txt`

### Role-Based Access

#### Administrator
The administrator account can:

- Register new users
- Add tasks
- View all tasks
- View personal tasks
- View completed tasks
- Delete tasks

#### Standard Users
Standard users can:

- Add tasks
- View all tasks
- View their assigned tasks

### Task Management

Users can:

- Assign tasks to specific users
- Create task descriptions
- Set due dates
- Record task assignment dates automatically

### Task Viewing

#### View All Tasks
Displays all tasks in a formatted layout.

#### View My Tasks
Displays only tasks assigned to the logged-in user.

#### View Completed Tasks (Admin Only)
Displays tasks marked as completed.

### Task Deletion (Admin Only)

Administrators can:

- View task summaries
- Select tasks by index
- Permanently remove tasks from the system

## Technologies Used

- Python 3
- Datetime Module
- File Handling
- Dictionaries
- Lists
- Conditional Logic
