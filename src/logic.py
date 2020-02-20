# # imports

# # caesars' cipher function

# # encryption

# def encryption(message, shifter_key):
#     encryption_result = ""

#     # go through every character
#     for i in range(len(message)):
#         letter = message[i]

#         if (letter.isupper()):
#             encryption_result += chr((ord(letter) + shifter_key - 65)%26 +65)
#         else:
#             encryption_result += chr((ord(letter) + shifter_key - 97)%26 +97)
    
#     return encryption_result

# # move the text


# def encrypt_rot13(message, key=13):
#     encryption_result = ""

#     for i in range(len(message)):
#         letter = message[i]
#         if (letter.isalpha()):
#             if (letter.isupper()):
#                 encryption_result += chr((ord(letter) - key - 65)%26 +65)
#             elif (letter.islower()):
#                 encryption_result += chr((ord(letter) - key - 97)%26 +97)
#         elif (letter.isnumeric()):
#             encryption_result += letter
#         elif (letter == " "):
#             encryption_result += letter
#         else:
#             if (letter == "."):
#                 encryption_result += letter 
#     return encryption_result

# print(encrypt_rot13("o"))


import tkinter
from tkinter import ttk 

main_window = tkinter.Tk()

main_window.geometry("800x800")

new_combo_box = ttk.Combobox(values = [
    "David",
    "Alex"
])
new_combo_box.grid(row = 0, column = 0)
new_combo_box.current(1)

def get_combo_value():
    the_value = new_combo_box.get()
    return the_value

selected = get_combo_value()

execute_button = tkinter.Button(text = "select", command = get_combo_value)
execute_button.grid(row = 1, column = 0)

change_label = tkinter.Label(text = selected)
change_label.grid(row = 2, column = 0)
change_label.update()

print(selected)

main_window.mainloop()