from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import messagebox

root = Tk(className="Simple Text Editor")
textPad = scrolledtext.ScrolledText(root,width=600,height=600)

def open_command():
    file = filedialog.askopenfile(parent=root,mode="rb",
                                  title="Please select your file: ")
    if file != None:
        contents = file.read()
        textPad.insert("1.0",contents)
        file.close()

def save_command():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = textPad.get("1.0",END+"-1c")
        file.write(data)

def exit_command():
    if messagebox.askokcancel("Quit","Do you really want to quit?"):
        root.destroy()

def about_command():
    label = messagebox.showinfo("About",
                                "Simple Text Editor by Stephen Beck made in "
                                "Python3 and Tkinter.")

def work():
    print("Working, please wait...")

def res():
    print("GUI window has been re-sized.")
    root.geometry("200x100")

def norm():
    print("GUI window set to default")
    root.geometry("400x300")

menu_1 = Menu(root)
root.config(menu=menu_1)

# Define menus in a dictionary so we can iterate over them to create 'em.
menus = {"File":{"New file":work,
                 "Open":open_command,
                 "Save":save_command,
                 "Exit":exit_command},
         "Edit":{"Resize":res,
                 "Normal":norm},
         "View":{"About":about_command}}

# Add menus
for m in menus:
    current_menu = Menu(menu_1)
    menu_1.add_cascade(label=m,
                       menu=current_menu)
    for n in menus[m]:
       current_menu.add_command(label=n,
                                command=menus[m][n])


# Missing features for the future here:
    # -- Recognize & run code that's entered into the text editor
    # -- Cut, copy & paste features

# Add status bar
status = Label(root,
               text="Run",
               bg="yellow",
               relief=SUNKEN,bd=1)
status.pack(side=BOTTOM,fill=X)

textPad.pack()
root.mainloop()
