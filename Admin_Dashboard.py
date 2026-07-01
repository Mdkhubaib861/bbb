from tkinter import *
from tkinter import messagebox
from Admin_Add_page import Add_Student_screen
from Delete import Delete_Window
from Search_Student import Search_Screen
from update import Update_Screen
from connectdb import *


cursor1.execute("SELECT * FROM student_info")
for x in cursor1.fetchall():
    print(x)


class Admin_Dashboard_Screen:
    def __init__(self,root,admin_screen):
        self.root=root
        self.admin_screen=admin_screen
        self.root.overrideredirect(True)
        self.root.title("Admin Dashboard Page")
        self.root.state("zoomed")
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#E0F7FA")

        self.root.rowconfigure(1, weight=0)

        left_frame=Frame(self.root,bg="#1E293B")
        left_frame.grid(row=0, column=0,rowspan=30,columnspan=2,sticky="nsew")

        for i in range(10):
            self.root.columnconfigure(i, weight=1)

        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)

        header = Frame(self.root, bg="#1a73e8", height=60)
        header.grid(row=0, column=0, columnspan=10, sticky="nsew")

        Label(header,
              text="MMANTC Admin Dashboard",
              font=("Century", 22, "bold"),
              bg="#1a73e8",
              fg="white").pack(expand=True)

        admin_btn=Button(self.root,text="Add Student",font=("Roboto",15,"bold"),width=20,bg="Skyblue",command=self.open_add_student)
        admin_btn.grid(row=1,column=0,columnspan=2,padx=5,pady=20,sticky=W)
        delete_stud_btn = Button(self.root,text="Delete Student",font=("Roboto",15,"bold"),width=20,bg="Skyblue",command=self.open_delete_student)
        delete_stud_btn.grid(row=2, column=0,columnspan=2,padx=5,pady=20,sticky="wn")
        update_stud_btn = Button(self.root, text="Update Student", font=("Roboto", 15, "bold"), width=20, bg="Skyblue",command=self.open_update_student)
        update_stud_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        search_stud_btn = Button(self.root, text="Search Student", font=("Roboto", 15, "bold"), width=20, bg="Skyblue",command=self.open_search_student)
        search_stud_btn.grid(row=4, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        exit_btn = Button(self.root,text="Exit",font=("Roboto", 15, "bold"),command=self.exit_fun,width=20, bg="#FF2E2E")
        exit_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=20,sticky="wn")
        logout_btn = Button(self.root, text="Logout", font=("Roboto", 15, "bold"), command=self.logout, width=20,bg="RoyalBlue1")
        logout_btn.grid(row=6, column=0, columnspan=2, padx=5, pady=20, sticky="wn")


        box_width = 20
        box_height = 4

        l_students = Label(self.root,
                           text="Total Students\n955",
                           font=("Roboto", 16, "bold"),
                           width=box_width,
                           height=box_height,
                           bg="#E3F2FD",
                           relief="ridge")
        l_students.grid(row=2, column=3, padx=20, pady=15)

        student_male = Label(self.root,
                             text="Total Male Students\n550",
                             font=("Roboto", 16, "bold"),
                             width=box_width,
                             height=box_height,
                             bg="#E8F5E9",
                             relief="ridge")
        student_male.grid(row=2, column=4, padx=20, pady=15)

        student_female = Label(self.root,
                               text="Total Female Students\n405",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#F3E5F5",
                               relief="ridge")
        student_female.grid(row=2, column=5, padx=20, pady=15)

        diploma_student = Label(self.root,
                               text="Total Diploma Students\n405",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#FFF3E0",
                                relief="ridge")
        diploma_student.grid(row=3, column=3, padx=20, pady=15)

        Degree_student = Label(self.root,
                                text="Total Degree Students\n550",
                                font=("Roboto", 16, "bold"),
                                width=box_width,
                                height=box_height,
                                bg="#ECEFF1",
                                relief="ridge")
        Degree_student.grid(row=3, column=4, padx=20, pady=15)

        Total_Faculty = Label(self.root,
                               text="Total Faculty\n56",
                               font=("Roboto", 16, "bold"),
                               width=box_width,
                               height=box_height,
                               bg="#FFE5D9",
                               relief="ridge")
        Total_Faculty.grid(row=3, column=5, padx=20, pady=15)


    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def logout(self):
        a = messagebox.askyesno("Logout", "Are you sure you want to Logout?")
        if a:
            self.root.destroy()  # close dashboard
            self.admin_screen.deiconify()  # show login again
            messagebox.showinfo("Logout", "Logged out successfully!")

    def open_add_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Add_Student_screen(new_window, self.root)

    def open_delete_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Delete_Window(new_window, self.root)

    def open_search_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Search_Screen(new_window, self.root)

    def open_update_student(self):
        self.root.withdraw()
        new_window = Toplevel()
        Update_Screen(new_window, self.root)
