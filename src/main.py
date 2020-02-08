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

    # encrption function 
    def encryption(self, message, shifter_key):
        encryption_result = ""

        # go through every character
        for i in range(len(message)):
            letter = message[i]

            if (letter.isupper()):
                encryption_result += chr((ord(letter) + shifter_key - 65)%26 +65)
            elif (letter.islower()):
                encryption_result += chr((ord(letter) + shifter_key - 97)%26 +97)
            elif (letter == " "):
                encryption_result += " "
        
        return encryption_result

    # decryption function 
    def decryption(self, message, shifter_key):
        decryption_result = ""

        # go through every character
        for i in range(len(message)):
            letter = message[i]

            if (letter.isupper()):
                decryption_result += chr((ord(letter) - shifter_key - 65)%26 +65)
            elif (letter.islower()):
                decryption_result += chr((ord(letter) - shifter_key - 97)%26 +97)
            elif (letter == " "):
                decryption_result += " "
        
        return decryption_result    


root_window = MainWindow()

if __name__ == "__main__":
    root_window.mainloop()
