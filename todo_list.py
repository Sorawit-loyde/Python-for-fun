import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        todo_list.insert(tk.END,task)
        entry.delete(0,tk.END)

root = tk.Tk()
root.title("To Do List")

frame = tk.Frame(root)
frame.pack(padx=20,pady=20)

entry = tk.Entry(frame,width=40)
entry.grid(row = 0,column=0,padx=5,pady=5)

add_button = tk.Button(frame,text="Add task ",command= add_task)
add_button.grid(row = 0,column=1,padx=5,pady=5)

todo_list = tk.Listbox(frame,width=40,height=10)
todo_list.grid(row=1,columnspan=2,padx=5,pady=5)

root.mainloop()


