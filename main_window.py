from Home_page import home_screen
from tkinter import Tk

class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")
        self.root.resizable(width=False, height=False)

        home_screen(self.root)

        self.root.mainloop()


MainWindow()
