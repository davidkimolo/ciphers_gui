# imports
import main as mn 

# create a title
placeholder_label = mn.tkinter.Label(text = "                     ", font = ("times", 20))
placeholder_label.grid(row =0 , column =0 )

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times", 20))
title_label.grid(row =0 , column =1 )

placeholder_label = mn.tkinter.Label(text = "                      ", font = ("times", 20))
placeholder_label.grid(row =0 , column =2 )


# encryption_message
encryption_message = mn.tkinter.Label(text = "Encrypt", font = ("times", 17), pady = 20)
encryption_message.grid(row = 1, column = 0, sticky = mn.tkinter.W)

# decryption_message
decryption_message = mn.tkinter.Label(text = "Decrypt", font = ("times", 17), pady = 20)
decryption_message.grid(row = 1, column = 2, sticky = mn.tkinter.E)

# encryption_box
encryption_box = mn.tkinter.Text(height = 12, width = 50, font = ("times", 16))
encryption_box.grid(row = 2, column = 0, sticky = mn.tkinter.W)

# shifter_key
shifter_key = mn.tkinter.Label(text = "Shifter Key", font  = ("times", 15))
shifter_key.grid(row = 1, column = 1)

# shifter_key_box
shifter_key_box = mn.tkinter.Text(height = 2, width = 8, font = ("times", 15))
shifter_key_box.grid(row = 2, column = 1)

# encryption_button
encryption_button = mn.tkinter.Button(text = "                    ENCRYPT                     ", font = ("times", 15), pady = 10,)
encryption_button.grid(row = 3, column = 0, sticky = mn.tkinter.W)

# decrption_box
decrption_box = mn.tkinter.Text(height = 12, width = 50, font = ("times", 16))
decrption_box.grid(row = 2, column = 2, sticky = mn.tkinter.E)

# Decrption button 
decryption_button = mn.tkinter.Button(text = "                    DECRYPT                     ", font = ("times", 15), pady = 10,)
decryption_button.grid(row = 3, column = 2, sticky = mn.tkinter.E)

# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()

