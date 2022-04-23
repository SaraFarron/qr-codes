# import qrcode
#
#
# data = """
# https://keep.google.com/u/0/#NOTE/1GCkc5WjLg9C3MfHZQFamTUNNE5MVJ-BldERVz2zS2-jQMDtRs8YriLFcBnK96f1Fwus
# """
#
# img = qrcode.make(data)
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")


import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root_tk = customtkinter.CTk()  # create CTk window like you do with the Tk window
root_tk.geometry("400x240")


def button_function():
    print("button pressed")


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=root_tk, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

root_tk.mainloop()
