# imports
import tkinter
# main class 

class MainWindow(tkinter.Tk):
    """ This is the main window, a child class of tkinter """
    def __init__(self):
        super().__init__()
        """ The main window properties """
        # main window title
        self.title("Cryptographic Ciphers")
        # main window size
        self.geometry("1320x400")
        # main window color
        self.configure(background = "light grey")

root_window = MainWindow()

if __name__ == "__main__":
    root_window.mainloop()
