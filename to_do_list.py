
# this block deals with saving the "to do tasks" in json file (so that its permanenetly saved in the hard disk and not just 
#get saved in the ram so that the user can view its previos tasks too and doesnt hv to re write them again ) and loading of the previously
# enetered to do tasks by the user 

import json
from datetime import datetime 

def save_tasks(tasks,file_name="tasks.json"):
    with open (file_name,"w") as f:
        json.dump(tasks,f,indent=4)



def load_tasks(file_name="tasks.json"):
    try:
       with open (file_name,"r") as f:
           return json.load(f)
    except FileNotFoundError:
        return []
    

# this block deals with the user interaction with his/her "to do tasks"

def add_tasks(tasks,title,deadline):
    tasks.append({"title":title,"deadline":deadline,"done":False})

def remove_task(tasks,index):
    if 1<=index<=len(tasks):
        tasks.pop(index-1)
    else:
        print("invalid task number")

def mark_done(tasks,index):
    if 1<=index<=len(tasks):
        tasks[index-1]["done"]=True
        print("Congratulations for completing your tasks")
    else:
        print("Invalid task number")

def sort_tasks(tasks):
    tasks.sort(key=lambda x:datetime.strptime(x["deadline"], "%d/%m/%y"))

def show_tasks(tasks):
    if not tasks:
        print("No tasks found")
    else:
        for i,t in enumerate(tasks,start=1): #enumerate gives numbering to each element of the list which we call as index and while doing that, it generates tuple like (index,element)
                                     #here the tuple is (i,t) where i=numbering of each elemnt(here,dict) and t = elemnt of the list(here,dict) 
                                     #here we are saying to python that "hey pyhton use the enumerate function to index or number each element of the list(here,tasks) and then
                                     # extract i and t in enumerated tasks while looping through each element in the list"
            status="TASK COMPLETED" if t["done"] else "TASK NOT COMPLETED" 
            print(f"{i} . {t['title']} - {t['deadline']} [{status}]")


def main():
    tasks=load_tasks()
    while True:
        print("Welcome to our to do task mananger ")
        print("Click 1 to add task")
        print("click 2 to remove task")
        print("click 3 to mark tasks done")
        print("click 4 to sort task")
        print("click 5 to show tasks")
        print("click 6 to save and exit")
        
        choice=input("Enter your choice from the above: ")
        
        if choice=="1":
            title=input("Enter title: ")
            deadline=input("Enter deadline: ")
            add_tasks(tasks,title,deadline)
            
        elif choice=="2":
            index=int(input("Enter index of the task you want to remove: "))
            remove_task(tasks,index)
            
        elif choice=="3":
            index=int(input("Enter the index of the task you want to mark done: "))
            mark_done(tasks,index)
        
        elif choice=="4":
            sort_tasks(tasks)
            print("Tasks are sorted by deadline")
        
        elif choice=="5":
            show_tasks(tasks)
            
        elif choice=="6":
            save_tasks(tasks,file_name="tasks.json")
            print("Saved succesfully")
            break
        
        else:
            print("Invalid choice.Try again.")
            
if __name__=="__main__":
    main()


            
            
           
                
        
            
            
            
            
        
        
    








