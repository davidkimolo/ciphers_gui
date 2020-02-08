# imports
import main as mn 

# logical functions
# move encrypted text
def move_text_to_decrypt_box():
    empty_message = "Error! The encryption box or shifter key box is empty\n"
    moving_text = encryption_box.get("1.0", mn.tkinter.END)
    shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)
    # check if there is a empty error message
    if empty_message in moving_text:
        encryption_box.delete("1.0", mn.tkinter.END)
    
    elif (len(moving_text) < 2) or len(shifter_key_number) < 2:
        # checking if the text box is empty
        decrption_box.insert("1.0", empty_message)

    else:
        # encrypting the data and inserting it to the decryption box
        decrption_box.insert("1.0", mn.MainWindow.encryption(moving_text, moving_text, int(shifter_key_number)))
        encryption_box.delete("1.0", mn.tkinter.END)

# move decrypted text
def move_text_to_encrypted_box():

    # check for an empty error message
    empty_message = "Error! The encryption box or shifter key box is empty\n"
    moving_text =decrption_box.get("1.0", mn.tkinter.END)
    shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)

    # checking if the decryption box has an error message
    if empty_message in moving_text:
        decrption_box.delete("1.0", mn.tkinter.END)
    # check if the decryption box is empty
    elif len(moving_text) < 2 or len(shifter_key_number) < 2:
        encryption_box.insert("1.0", empty_message)
    # decrypt the message and send it to the encryption box
    else:
        encryption_box.insert("1.0", mn.MainWindow.decryption(moving_text, moving_text, int(shifter_key_number)))
        decrption_box.delete("1.0", mn.tkinter.END)



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
encryption_button = mn.tkinter.Button(text = "                    ENCRYPT                     ",
                                    font = ("times", 15), pady = 10, command = move_text_to_decrypt_box)
encryption_button.grid(row = 3, column = 0, sticky = mn.tkinter.W)

# decrption_box
decrption_box = mn.tkinter.Text(height = 12, width = 50, font = ("times", 16))
decrption_box.grid(row = 2, column = 2, sticky = mn.tkinter.E)

# Decrption button 
decryption_button = mn.tkinter.Button(text = "                    DECRYPT                     ",
                                        font = ("times", 15), pady = 10,  command = move_text_to_encrypted_box)
decryption_button.grid(row = 3, column = 2, sticky = mn.tkinter.E)

# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()

