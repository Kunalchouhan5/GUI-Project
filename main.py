from tkinter import *
 
from tkinter import messagebox
 
tasks_list = []
 
counter = 1
 
def inputError() :
     

    if enterTaskField.get() == "" :
         
    
        messagebox.showerror("Input Error")
         
        return 0
     
    return 1
 
def clear_taskNumberField() :
     

    taskNumberField.delete(0.0, END)
 
def clear_taskField() :
 

    enterTaskField.delete(0, END)
     
def insertTask():
 
    global counter
     

    value = inputError()
 

    if value == 0 :
        return
 


    content = enterTaskField.get() + "\n"
 

    tasks_list.append(content)
 


    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
 

    counter += 1
 

    clear_taskField()
 
def delete() :
     
    global counter
     

    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
 

    number = taskNumberField.get(1.0, END)
 


    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 


    clear_taskNumberField()
     

    try:
        tasks_list.pop(task_no - 1)
    except:
        print("Item not found")

    counter -= 1
     

    TextArea.delete(1.0, END)
 

    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
 
if __name__ == "__main__" :
 

    gui = Tk()
 

    gui.configure(background = "#BBE5ED")
 

    gui.title("ToDo App")
 

    gui.geometry("400x400")
 

    enterTask = Label(gui, text = "Enter Your Task", bg = "#BBE5ED")
 


    enterTaskField = Entry(gui)
 



    Submit = Button(gui, text = "Submit", fg = "#FFF", bg = "#390099", command = insertTask)
 



    TextArea = Text(gui, height = 15, width = 25, font = "lucida 13")
 

    taskNumber = Label(gui, text = "Delete Task Number", bg = "#FF0054", fg="#FFF")
                        
    taskNumberField = Text(gui, height = 1, width = 10, font = "lucida 13")
 



    delete = Button(gui, text = "Delete", fg = "#FFF", bg = "#FF5400", command = delete)
 



    Exit = Button(gui, text = "Exit", fg = "#FFF", bg = "#FF5400", command = exit)
 



    enterTask.grid(row = 0, column = 2)
 

    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
                        
    Submit.grid(row = 1, column = 3)
         


    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 5, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 4, column = 2, padx = 4)
 


    delete.grid(row = 4, column = 3, pady = 5)
                        
    Exit.grid(row = 4, column = 4, padx=10)
    

    gui.mainloop()
