import task 
import storage

def add_task(title): # feture is working of adding any task in tasks.txt

    task.task_template["id"] += 1 
    new_id = task.task_template["id"]
    status = task.task_template["status"]

    task_text = f"Title : {title}\nID : {new_id}\nStatus : {status}"
    
    storage.save_task(task_text) # to save task in tasks.txt
    print("Done") # to sucsess added task