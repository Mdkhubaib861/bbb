from tkinter import *
from tkinter import messagebox
from Admin_logging import Admin_screen
from Student_logging import Student_screen

class home_screen:
    def __init__(self,root):
        self.root=root
        self.root.title("Home Page")
        self.root.resizable(False,False)
        self.root.config(bg="#E0F7FA")
        header = Frame(self.root, bg="#1E293B", height=60)
        header.grid(row=0, column=0,sticky="nsew",columnspan=3,padx=10,pady=10)

        Label(header,
              text="MMANTC Admin Dashboard",
              font=("Century", 25, "bold"),
              bg="#1E293B",
              fg="white").pack(expand=True)
        admin_btn=Button(self.root,text="Admin",font=("Roboto",15,"bold"),width=25,bg="Skyblue",command=self.open_admin_screen)
        admin_btn.grid(row=1,column=0,columnspan=3,padx=6,pady=6)
        student_btn=Button(self.root,text="Student",font=("Roboto",15,"bold"),width=25,bg="Skyblue",command=self.open_student_screen)
        student_btn.grid(row=2, column=0, columnspan=3, padx=6, pady=6)
        exit_btn=Button(self.root,text="Exit",font=("Roboto", 15, "bold"),command=self.exit_fun,width=20, bg="#FF2E2E")
        exit_btn.grid(row=3, column=0, columnspan=3, padx=6, pady=6)


    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def open_admin_screen(self):
        self.root.withdraw()
        new_window=Toplevel()
        Admin_screen(new_window,self.root)

    def open_student_screen(self):
        self.root.withdraw()
        new_window=Toplevel()
        Student_screen(new_window,self.root)

