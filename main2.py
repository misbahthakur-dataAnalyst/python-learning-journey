#   import tkinter for creating GUI(graphical user interphase) apps
import tkinter as tk
from tkinter import filedialog, messagebox

#main window code
root= tk.Tk()
root.title("simple text editor")
root.geometry("800x600")


# create text area
text= tk.Text(
    root,
    wrap=tk.WORD,
    font=("helvetic", 12)
)



text.pack(expand=True,fill=tk.BOTH)

#main logic starts now

#function 1- to create a new file

def new_file():
    text.delete(1.0, tk.END)

# FUNCTION-2 TO OPEN A NEW FILE
def open_file():
    # open file dialogue
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )


    if file_path:
        #open file
        with open(file_path, "r")as file:
            # clear old text
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())


# function 3 - save the file


def save_file():
    # open save file dialogue
    file_path= filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w")as file:
            file.write(text.get(1.0, tk.END))


    messagebox.showinfo("info", "file saved successfully")




#create menu bar

menu= tk.Menu(root)
root.config(menu=menu)
file_menu= tk.Menu(menu)

# new open, save, exit

# add file menu to menu bar

file_menu.add_cascade(label="file", menu=file_menu)


file_menu.add_command("new", command=new_file)
file_menu.add_command("open", command=open_file)
file_menu.add_command("save", command=save_file)
file_menu.add_separator()
file_menu.add_command("exit", command=root.quit)


#starts and keeps the window open
root.mainloop()
