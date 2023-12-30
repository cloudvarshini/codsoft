import tkinter as tk


root = tk.Tk()
root.configure(bg="White")
root.title("My To Do List")


root.geometry("300x400")
lbl_title = tk.Label(root, text="To Do List")
lbl_title.pack()

lbl_display = tk.Label(root,text="")
lbl_display.pack()

tasks = []

##tasks = ["Read newspaper","Home Work","Do internship"]

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)


def clear_listbox():
    lb_tasks.delete(0,"end")
def add_task():
    task = text_input.get()
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter the task."
    text_input.delete(0,"end")
def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()
def del_all():
    global tasks
    tasks = []
    update_listbox()

text_input = tk.Entry(root, width=20)
text_input.pack()

btn_add_task = tk.Button(root, text="Add",width="10",command=add_task)
btn_add_task.pack()

btn_del_one = tk.Button(root, text="Delete",width="10",command=del_one)
btn_del_one.pack()

btn_del_all = tk.Button(root, text="Delete All",width="10",command=del_all)
btn_del_all.pack()

lb_tasks = tk.Listbox(root)
lb_tasks.pack()

root.mainloop()