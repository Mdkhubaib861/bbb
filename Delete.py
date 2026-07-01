
from tkinter import *
from tkinter import messagebox

class Delete_Window:
    def __init__(self, root, delete_screen):
        self.root = root
        self.delete_screen = delete_screen

        self.root.title("Delete Student")
        self.root.state("zoomed")   # Full screen
        self.root.config(bg="#E0F7FA")

        # ===== HEADER =====
        header = Frame(self.root, bg="#1a73e8", height=60)
        header.pack(fill=X)

        Label(header,
              text="MMANTC - Delete Student",
              font=("Century", 22, "bold"),
              bg="#1a73e8",
              fg="white").pack(pady=10)

        # ===== MAIN FRAME =====
        main_frame = Frame(self.root, bg="#E0F7FA")
        main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # ===== LEFT FRAME (INPUT) =====
        left_frame = Frame(main_frame, bg="white", bd=2, relief="ridge")
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(left_frame,
              text="Enter Student Details",
              font=("Roboto", 18, "bold"),
              bg="white").pack(pady=20)

        # Student ID
        Label(left_frame, text="Student ID", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.student_id = Entry(left_frame, width=30, font=("Roboto", 12))
        self.student_id.pack(padx=20, pady=5)

        # Name
        Label(left_frame, text="Student Name", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.student_name = Entry(left_frame, width=30, font=("Roboto", 12))
        self.student_name.pack(padx=20, pady=5)

        # Course
        Label(left_frame, text="Course", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.course = Entry(left_frame, width=30, font=("Roboto", 12))
        self.course.pack(padx=20, pady=5)

        # Year
        Label(left_frame, text="Year", font=("Roboto", 14), bg="white").pack(anchor="w", padx=20)
        self.year = Entry(left_frame, width=30, font=("Roboto", 12))
        self.year.pack(padx=20, pady=5)

        # Search Button
        Button(left_frame,
               text="Search Student",
               bg="#1a73e8",
               fg="white",
               font=("Roboto", 12, "bold"),
               command=self.search_student).pack(pady=20)

        # ===== RIGHT FRAME (PREVIEW) =====
        right_frame = Frame(main_frame, bg="white", bd=2, relief="ridge")
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)

        Label(right_frame,
              text="Student Information",
              font=("Roboto", 18, "bold"),
              bg="white").pack(pady=20)

        self.info_box = Label(right_frame,
                              text="No student selected",
                              font=("Roboto", 14),
                              bg="#F5F5F5",
                              width=40,
                              height=10,
                              relief="sunken",
                              anchor="nw",
                              justify=LEFT)

        self.info_box.pack(padx=20, pady=20)

        # Delete Button
        Button(right_frame,
               text="Delete Student",
               bg="red",
               fg="white",
               font=("Roboto", 14, "bold"),
               command=self.delete_student).pack(pady=10)

        # Back Button
        Button(right_frame,
               text="Back",
               bg="gray",
               fg="white",
               font=("Roboto", 12),
               command=self.go_back).pack(pady=10)

    # ===== FUNCTIONS =====

    def search_student(self):
        sid = self.student_id.get()
        name = self.student_name.get()

        if sid == "" or name == "":
            messagebox.showwarning("Input Error", "Please enter ID and Name")
            return

        # Dummy data (replace with DB later)
        info = f"""
Student ID: {sid}
Name: {name}
Course: B.Tech
Year: 2nd Year
Status: Active
"""

        self.info_box.config(text=info)

    def delete_student(self):
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this student?")

        if confirm:
            self.student_id.delete(0, END)
            self.student_name.delete(0, END)
            self.course.delete(0, END)
            self.year.delete(0, END)

            self.info_box.config(text="No student selected")

            messagebox.showinfo("Success", "Student Deleted Successfully!")

    def go_back(self):
        self.root.destroy()
        self.delete_screen.deiconify()