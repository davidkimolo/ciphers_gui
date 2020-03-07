# imports
import main as mn 
import tkinter

# cipher_combo_box 
cipher_combo_box = mn.ttk.Combobox(values = [
    "caesar cipher",
    "ROT13",
    "Vigenere cipher"
])
cipher_combo_box.grid(row = 4, column = 0, padx = 35)
cipher_combo_box.current(1)

def get_cipher_combo_box_value():
    cipher_value = cipher_combo_box.get()
    return cipher_value

the_cipher_value = get_cipher_combo_box_value()

# logical functions
# move encrypted text
def move_text_to_decrypt_box():
    # check which cipher was selected
    """
    if combox value == cipher A:
        do function
    elif combox value == cipher B:
        do function
    """
    if (the_cipher_value == "caesar cipher"):
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
    elif (the_cipher_value == "ROT13"):
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
            decrption_box.insert("1.0", mn.MainWindow.encrypt_rot13(moving_text, moving_text, int(shifter_key_number)))
            encryption_box.delete("1.0", mn.tkinter.END) 
    elif (the_cipher_value == "Vigenere cipher"):
        empty_message = "Error! The encryption box or shifter key box is empty\n"

# move decrypted text
def move_text_to_encrypted_box():

    if (the_cipher_value == "caesar cipher"):
        shifter_key_number = 13
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

    elif (the_cipher_value == "ROT13"):
        # check for an empty error message
        empty_message = "Error! The encryption box or shifter key box is empty\n"
        moving_text = decrption_box.get("1.0", mn.tkinter.END)
        shifter_key_number = shifter_key_box.get("1.0", mn.tkinter.END)

        # checking if the decryption box has an error message
        if empty_message in moving_text:
            decrption_box.delete("1.0", mn.tkinter.END)
        # check if the decryption box is empty
        elif len(moving_text) < 2 or len(shifter_key_number) < 2:
            encryption_box.insert("1.0", empty_message)
        # decrypt the message and send it to the encryption box
        else:
            encryption_box.insert("1.0", mn.MainWindow.decrypt_rot13(moving_text, moving_text, int(shifter_key_number)))
            decrption_box.delete("1.0", mn.tkinter.END)




# create a title
placeholder_label = mn.tkinter.Label(text = "                     ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0 , column =0 )

title_label = mn.tkinter.Label(text = "Cryptographic Ciphers", font = ("times", 20), bg = "light grey")
title_label.grid(row =0 , column =1 )

placeholder_label = mn.tkinter.Label(text = "                      ", font = ("times", 20), bg = "light blue")
placeholder_label.grid(row =0 , column =2 )


# encryption_message
encryption_message = mn.tkinter.Label(text = "Encrypt", font = ("times", 17), pady = 20, bg = "light blue")
encryption_message.grid(row = 1, column = 0, sticky = mn.tkinter.W)

# decryption_message
decryption_message = mn.tkinter.Label(text = "Decrypt", font = ("times", 17), pady = 20, bg = "light blue")
decryption_message.grid(row = 1, column = 2, sticky = mn.tkinter.E)

# encryption_box
encryption_box = mn.tkinter.Text(height = 12, width = 50, font = ("times", 16))
encryption_box.grid(row = 2, column = 0, sticky = mn.tkinter.W)

# shifter_key
shifter_key = mn.tkinter.Label(text = "Shifter Key / Keyword", font  = ("times", 15), bg = "light blue")
shifter_key.grid(row = 1, column = 1)

# shifter_key_box
shifter_key_box = mn.tkinter.Text(height = 2, width = 8, font = ("times", 15))
shifter_key_box.grid(row = 2, column = 1)
shifter_key_box.insert(tkinter.END,"13")
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

# cipher chooser
cipher_choose_label = tkinter.Label(text = "Choose cipher: ", font = ("text", 15), bg = "light blue")
cipher_choose_label.grid(row = 4, column = 0, sticky = mn.tkinter.W, pady = 10)



# loop the program
if __name__ == "__main__":
    mn.root_window.mainloop()

