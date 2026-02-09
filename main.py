import tkinter as tk
#functions
def leave():
    root.destroy()




#window set up / settings
root = tk.Tk()
root.title("Basic tkinter set up :3")
root.geometry("300x300")

#widgits being created
stop = tk.Button(root, command = leave, text = "Stop")


#add widget to windows :3
stop.place(x=0,y=0)




root.mainloop()
