from tkinter import *
from datetime import datetime
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import cv2
from connectdb import *
import time
from PIL import Image, ImageTk
from tkinter import Canvas

class Add_Student_screen:
    def __init__(self,root,add_screen):
        self.root = root
        self.add_screen = add_screen
        self.root.title("Add Student")
        self.root.state("zoomed")
        self.root.overrideredirect(True)
        self.root.resizable(width=False, height=False)
        self.root.columnconfigure(4, weight=1)
        self.root.config(bg="#E0F7FA")
        self.stname=StringVar()
        self.dob=StringVar()
        self.gender = StringVar(value="Male")
        self.email = StringVar()
        self.category = StringVar()
        self.address = StringVar()
        self.aadhaar = StringVar()
        self.prn = StringVar()
        self.course = StringVar()
        self.branch = StringVar()
        self.year = StringVar()
        self.percent = StringVar()
        self.photo = StringVar()



        for i in range(10):
            self.root.columnconfigure(i, weight=1)

        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)

        header = Frame(self.root, bg="#1E293B", height=60)
        header.grid(row=0, column=0, columnspan=10, sticky="nsew")

        Label(header,
              text="MMANTC Admin Dashboard",
              font=("Century", 22, "bold"),
              bg="#1E293B",
              fg="white").pack(expand=True)

        # Label(self.root, text="MMANTC Admin Add Student", font=("Century", 22, "bold")).grid(row=0, column=2, columnspan=4,padx=10, pady=7,sticky=W)
        Label(self.root, text="Student Information", font=("Century", 15, "bold"),bg="#E0F7FA").grid(row=1, column=0,columnspan=4, padx=10,pady=7)
        L1 = Label(self.root, text="Enter Student Full Name:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L1.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.E1 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.stname)
        self.E1.grid(row=2, column=1, padx=10, pady=10, sticky=W)
        L2 = Label(self.root, text="Enter Date of Birth:",font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L2.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.dob = DateEntry(self.root,
                             width=20,
                             background='darkblue',
                             foreground='white',
                             borderwidth=2,
                             date_pattern='dd/mm/yyyy',
                             font=("Roboto", 12),bg="#E0F7FA",textvariable=self.dob)

        self.dob.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        L1 = Label(self.root, text="Enter Student Gender:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L1.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        E2 = Radiobutton(self.root,text="Male",variable=self.gender,value="Male",font=("Roboto", 10),bg="#E0F7FA")
        E2.grid(row=4, column=1, padx=10, pady=10, sticky=W)
        E3= Radiobutton(self.root,text="Female",variable=self.gender,value="Female",font=("Roboto", 10),bg="#E0F7FA")
        E3.grid(row=4, column=1, padx=10, pady=10)
        L10 = Label(self.root, text="Enter Student Email:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L10.grid(row=5,column=0, padx=10, pady=10, sticky=W)
        self.E10 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.email)
        self.E10.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        Label(self.root,
              text="Select Category:",
              font=("Roboto", 15, "bold"),bg="#E0F7FA").grid(row=6, column=0, padx=10, pady=10, sticky=W)

        self.category_var = StringVar()

        self.category_dropdown = ttk.Combobox(self.root,
                                              textvariable=self.category,
                                              values=["General", "OBC", "SC", "ST","EWS"],
                                              font=("Roboto", 12),
                                              width=20,
                                              state="readonly")

        self.category_dropdown.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        self.category_dropdown.set("Select Category")

        L4 = Label(self.root, text="Enter Student Aadhaar No:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L4.grid(row=7, column=0, padx=10, pady=10, sticky=W)
        E4 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.aadhaar)
        E4.grid(row=7, column=1, padx=10, pady=10, sticky=W)
        L5 = Label(self.root, text="Enter Student Address:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L5.grid(row=8, column=0, padx=10, pady=10, sticky=W)
        E5 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.address)
        E5.grid(row=8, column=1, padx=10, pady=10, sticky=W)
        L6 = Label(self.root, text="Enter Student PRN:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L6.grid(row=9, column=0, padx=10, pady=10, sticky=W)
        E6 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.prn)
        E6.grid(row=9, column=1, padx=10, pady=10, sticky=W)
        L11 = Label(self.root, text="Enter Student Branch:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L11.grid(row=11, column=0, padx=10, pady=10, sticky=W)
        L12 = Label(self.root, text="Student Course:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L12.grid(row=10, column=0, padx=10, pady=10, sticky=W)
        self.course_var = StringVar()

        self.course_dropdown = ttk.Combobox(self.root,
                                            textvariable=self.course,
                                            values=["Bachelor of Engineering (BE)","Polytechnic Engineering (Diploma)"],
                                            font=("Roboto", 12),
                                            width=20,
                                            state="readonly")

        self.course_dropdown.grid(row=10, column=1, padx=10, pady=10, sticky=W)

        self.course_dropdown.set("Select Course")

        self.Branch_var = StringVar()

        self.Branch_dropdown = ttk.Combobox(self.root,
                                              textvariable=self.branch,
                                              values=["Computer Science Engineering", "Mechanical Engineering", "Electrical Engineering ", "Electronic and Telecommunication", "Civil Engineering"],
                                              font=("Roboto", 12),
                                              width=20,
                                              state="readonly")

        self.Branch_dropdown.grid(row=11, column=1, padx=10, pady=10, sticky=W)

        self.Branch_dropdown.set("Select Branch")

        Label(self.root, text="Select Year:", font=("Roboto", 15, "bold"), bg="#E0F7FA").grid(row=13, column=0, padx=10,
                                                                                              pady=10, sticky=W)
        self.year_var = StringVar()

        self.year_dropdown = ttk.Combobox(self.root,
                                          textvariable=self.year,
                                          values=["First", "Second", "Third", "Fourth"],
                                          font=("Roboto", 12),
                                          width=20,
                                          state="readonly")

        self.year_dropdown.grid(row=13, column=1, padx=10, pady=10, sticky=W)

        self.year_dropdown.set("Select Year")
        L8 = Label(self.root, text="Enter Student 12th Percentage:", font=("Roboto", 15, "bold"),bg="#E0F7FA")
        L8.grid(row=14, column=0, padx=10, pady=10, sticky=W)
        E8 = Entry(self.root, width=25, font=("Roboto", 15, "bold"),textvariable=self.percent)
        E8.grid(row=14, column=1, padx=10, pady=10, sticky=W)


        exit_btn = Button(self.root,text="Exit",font=("Roboto", 15, "bold"),command=self.exit_fun,width=10, bg="#FF2E2E")
        exit_btn.grid(row=15, column=0, padx=5, pady=10,sticky=W)

        back_btn = Button(self.root, text="Go Back", font=("Roboto", 15, "bold"), command=self.go_back, width=15,
                          bg="#6F8FAF")
        back_btn.grid(row=15, column=1, padx=6, pady=6)
        # ===== Student Photo Section =====

        photo_frame = Frame(self.root, bd=2, relief="ridge",bg="LightBlue4")
        photo_frame.grid(row=1, column=4, rowspan=10, padx=20, pady=(40,20), sticky="n")

        photo_frame.config(width=230, height=580)
        photo_frame.grid_propagate(False)

        Label(photo_frame,
              text="Camera Preview",
              font=("Roboto", 12, "bold"),bg="LightBlue4").pack(pady=5)

        # Passport size photo placeholder
        self.canvas = Canvas(photo_frame,
                             width=180,
                             height=150,
                             bg="lightgray",
                             highlightthickness=1,
                             highlightbackground="black")

        self.canvas.pack(pady=10)

        # Buttons frame
        btn_frame = Frame(photo_frame,bg="LightBlue4")
        btn_frame.pack(pady=10)


        preview_btn = Button(btn_frame,
                              text="Preview",
                              font=("Roboto", 10, "bold"),
                              width=10,
                              command=self.start_camera,
                              bg="LightBlue3")

        preview_btn.grid(row=0, column=0, padx=5)

        capture_btn = Button(btn_frame,
                             text="Capture",
                             font=("Roboto", 10, "bold"),
                             width=10,
                             command=self.capture_image,
                             bg="LightBlue3")

        capture_btn.grid(row=0, column=1, padx=5)

        Label(photo_frame,
              text="Captured Image",
              font=("Roboto", 11, "bold"),bg="LightBlue4").pack(pady=(10, 5))

        self.capture_canvas = Canvas(photo_frame,
                                     width=180,
                                     height=200,
                                     bg="lightgray",
                                     highlightthickness=1,
                                     highlightbackground="black")

        self.capture_canvas.pack(pady=5)

        self.savebtn=Button(self.root,text="Save Record",font=("Roboto", 15, "bold"),command=self.store_data,width=10, bg="#FF2E2E")
        self.savebtn.grid(row=15, column=7, padx=5, pady=10, sticky=W)

    def capture_image(self):

        name_input = self.E1.get().strip()

        if name_input == "":
            from tkinter import messagebox
            messagebox.showwarning("Missing Name", "Please enter student name first")
            return

        name = name_input.split()[0]

        dob = self.dob.get().replace("/", "-")

        filename = f"Photo_{name}_{dob}.jpg"
        self.photo=filename

        ret, frame = self.cam.read()

        if ret:
            cv2.imwrite(filename, frame)
            print("Image saved as:", filename)

            # STOP camera preview
            self.stop_camera()

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, _ = frame.shape
            center_x = w // 2
            center_y = h // 2

            crop_size = min(h, w) // 2

            frame = frame[
                center_y - crop_size:center_y + crop_size,
                center_x - crop_size:center_x + crop_size
            ]

            img = Image.fromarray(frame)
            img = img.resize((200, 200))

            self.captured_img = ImageTk.PhotoImage(img)

            self.capture_canvas.delete("all")
            self.capture_canvas.create_image(0, 0, anchor="nw", image=self.captured_img)

        else:
            print("Picture not captured")


    def start_camera(self):
        self.cam = cv2.VideoCapture(0)

        if not self.cam.isOpened():
            print("Camera not detected")
            return

        self.show_frame()

    def show_frame(self):
        ret, frame = self.cam.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            h, w, _ = frame.shape
            center_x = w // 2
            center_y = h // 2

            crop_size = min(h, w) // 2

            frame = frame[
                center_y - crop_size:center_y + crop_size,
                center_x - crop_size:center_x + crop_size
            ]

            img = Image.fromarray(frame)
            img = img.resize((200, 200))

            self.imgtk = ImageTk.PhotoImage(img)

            self.canvas.create_image(0, 0, anchor="nw", image=self.imgtk)

        if hasattr(self, "cam"):
            self.canvas.after(10, self.show_frame)

    def submit_data(self):
        name = self.E1.get()
        dob = f"{self.day.get()}/{self.month.get()}/{self.year.get()}"
        category = self.category_var.get()
        year = self.year_var.get()

        print("Name:", name)
        print("DOB:", dob)
        print("Category:", category)
        print("Year:", year)

    def exit_fun(self):
        ask=messagebox.askyesno("Exit","Are you sure you want to exit?")
        if ask:
            self.root.destroy()
        else:
            pass

    def go_back(self):
        self.root.destroy()
        self.add_screen.deiconify()
        self.add_screen.state("zoomed")

    def show_year(self):
        print("Selected Year:", self.year_var.get())

    def stop_camera(self):
        if hasattr(self, "cam"):
            self.cam.release()
            del self.cam

    def store_data(self):
        q1='''INSERT INTO student_info (st_name,
                          dob,
                          gender,
                          email,
                          category,
                          address,
                          aadhaar,
                          prn,
                          course,
                          branch,
                          year,
                          percent,
                          photo
                          )
        VAlUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        '''



        dob_text = self.dob.get()
        dob_mysql = datetime.strptime(dob_text, "%d/%m/%Y").strftime("%Y-%m-%d")
        v1=(self.stname.get(),dob_mysql,self.gender.get(),self.email.get(),str(self.category.get()),str(self.address.get()),str(self.aadhaar.get()),str(self.prn.get()),str(self.course.get()),str(self.branch.get()),str(self.year.get()),str(self.percent.get()),self.photo)

        cursor1.execute(q1,v1)
        conn.commit()
        messagebox.showinfo("Alert",self.email.get())
