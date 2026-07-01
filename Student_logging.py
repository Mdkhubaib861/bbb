from tkinter import *
from tkinter import messagebox

class Student_screen:
    def __init__(self,root,new_window):
        self.root=root
        self.new_window=new_window
        self.root.title("Student Logging")
        self.root.resizable(False,False)
        Label(self.root,text="MMANTC Student Login",font=("Century",25,"bold")).grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        L1=Label(self.root,text="Enter User ID",font=("Roboto",15,"bold"))
        L1.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        E1=Entry(self.root,width=20,font=("Roboto",15,"bold"))
        E1.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        L2 = Label(self.root, text="Enter Password", font=("Roboto", 15, "bold"))
        L2.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        E2 = Entry(self.root, width=20, font=("Roboto", 15, "bold"),show="*")
        E2.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        stu_login_btn = Button(self.root, text="Login", font=("Roboto", 15, "bold"),width=20,bg="#71B3F5")
        stu_login_btn.grid(row=3, column=0, padx=6, pady=6)
        exit_btn = Button(self.root, text="Exit", font=("Roboto", 15, "bold"), command=self.exit_fun, width=20,bg="#FF2E2E")
        exit_btn.grid(row=3, column=1, padx=6, pady=6)
        back_btn = Button(self.root, text="Back to Menu", font=("Roboto", 15, "bold"), command=self.go_back, width=10,bg="#FF2E2E")
        back_btn.grid(row=0, column=3, padx=6, pady=6)

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def go_back(self):
        self.root.destroy()
        self.new_window.deiconify()
