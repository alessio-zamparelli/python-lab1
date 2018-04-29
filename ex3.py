

def todo_manager():
    print("""
    Insert the number corresponding to the action you want to perform:
1 insert a new task;
2 remove a task;
3 show all the tasks;
4 close the program.
Your choice:
    """)
    choice = input()
    if(choice == '1'):
    elif(choice == '2'):
    elif(choice == '3'):
    elif(choice == '4'):
    else:
        print("choice not valid, try again")