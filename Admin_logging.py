from tkinter import *
from tkinter import messagebox
from Admin_Dashboard import Admin_Dashboard_Screen

class Admin_screen:
    def __init__(self,root,menu_screen):
        self.root=root
        self.menu_screen=menu_screen

        self.username = StringVar()
        self.password = StringVar()

        self.root.title("Admin Logging")
        self.root.resizable(False,False)
        self.root.config(bg="#E0F7FA")

        # Label(self.root,text="MMANTC Admin Login",font=("Century",25,"bold")).grid(row=0,column=0,columnspan=4,padx=10,pady=10)
        header = Frame(self.root, bg="#1E293B", height=60)
        header.grid(row=0, column=0, columnspan=4, sticky="nsew",padx=10,pady=10)

        Label(header,
              text="MMANTC Admin Dashboard",
              font=("Century", 25, "bold"),
              bg="#1E293B",
              fg="white").pack(expand=True)
        L1=Label(self.root,text="Enter User ID",font=("Roboto",15,"bold"),bg="#E0F7FA")
        L1.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        E1=Entry(self.root,width=30,font=("Roboto",15,"bold"),textvariable=self.username)
        E1.grid(row=1,column=1,padx=10,pady=10,sticky=W)
        L2=Label(self.root, text="Enter Password",font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L2.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        E2=Entry(self.root, width=30, font=("Roboto", 15, "bold"),show="*",textvariable=self.password)
        E2.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        ad_login_btn = Button(self.root, text="Login", font=("Roboto", 15, "bold"),width=15,bg="#71B3F5",command=self.check_login)
        ad_login_btn.grid(row=3, column=1, padx=6, pady=6)
        exit_btn = Button(self.root, text="Exit", font=("Roboto", 15, "bold"), command=self.exit_fun, width=15,bg="#FF2E2E")
        exit_btn.grid(row=3, column=2, padx=6, pady=6)
        back_btn = Button(self.root, text="Go Back", font=("Roboto", 15, "bold"), command=self.go_back, width=15,bg="#6F8FAF")
        back_btn.grid(row=3, column=0, padx=6, pady=6)

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def check_login(self):
        # if self.username.get() == "" or self.password.get() == "":
        #     messagebox.showerror("Error","Please enter both username and password")
        # else:
            if self.username.get() == "" and self.password.get() == "":
                self.root.withdraw()
                new_window = Toplevel()
                Admin_Dashboard_Screen(new_window, self.root)
            else:
                messagebox.showerror("Error", "Invalid username or password")

    def go_back(self):
        self.root.destroy()
        self.menu_screen.deiconify()

