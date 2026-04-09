import tasks


print("Wellcome to task manger of Mohamed")
while True:
    user_input = int(input("If you want to add task press [1], to Logout press [0] : ").lower().strip()) # option to open the application
    if user_input == 1:
        title_task = input("Write the title of task : ").title().strip()
        tasks.add_task(title_task)
    elif user_input == 0:
        print("Okay, see you later!")
        break


        

