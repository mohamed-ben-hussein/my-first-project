
def save_task(task_text):
    with open("tasks.txt","a", encoding="utf-8") as file:
        file.write(task_text + "\n===============================\n")