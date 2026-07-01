from tkinter import *
from tkinter import messagebox

class StudentDashboard:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Dashboard")
        self.root.geometry("700x500")
        self.root.configure(bg="white")
        Label(self.root,
              text="MMANTC Student Dashboard",
              font=("Century", 22, "bold"),
              bg="white",
              fg="darkblue").grid(row=0, column=0, columnspan=2, pady=20)

        Label(self.root, text="Full Name:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=1, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="Shah Faisal",
              font=("Roboto", 14),
              bg="white").grid(row=1, column=1, sticky=W, pady=5)

        Label(self.root, text="PRN Number:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=2, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="1234567890",
              font=("Roboto", 14),
              bg="white").grid(row=2, column=1, sticky=W, pady=5)

        Label(self.root, text="Course:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=3, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="B.Tech",
              font=("Roboto", 14),
              bg="white").grid(row=3, column=1, sticky=W, pady=5)

        Label(self.root, text="Branch:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=4, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="E&TC Engineering",
              font=("Roboto", 14),
              bg="white").grid(row=4, column=1, sticky=W, pady=5)

        Label(self.root, text="Year:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=5, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="II",
              font=("Roboto", 14),
              bg="white").grid(row=5, column=1, sticky=W, pady=5)

        Label(self.root, text="Category:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=6, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="OBC",
              font=("Roboto", 14),
              bg="white").grid(row=6, column=1, sticky=W, pady=5)

        Label(self.root, text="Date of Birth:",
              font=("Roboto", 14, "bold"),
              bg="white").grid(row=7, column=0, sticky=W, padx=50, pady=5)

        Label(self.root, text="12/05/2005",
              font=("Roboto", 14),
              bg="white").grid(row=7, column=1, sticky=W, pady=5)
        Button(self.root,
               text="Logout",
               font=("Roboto", 12, "bold"),
               bg="red",
               fg="white",
               width=10,
               command=self.logout).grid(row=8, column=1, pady=30, sticky=W)

        self.root.mainloop()

    def logout(self):
        ask = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if ask:
            self.root.destroy()
        else:
            pass
        self.root.destroy()
StudentDashboard()