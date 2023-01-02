## Code for building own Python IDLE, for computer having python vesion 3 installed in it, else could change the version on line 40,
# for compiling purpose.

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
from PIL import Image, ImageTk
import os
root = Tk()
root.title("Python IDLE")
root.geometry("1200x700")
root.configure(bg="light yellow", highlightcolor="yellow", bd=3)
root.resizable(False, False)
file_path = ' '

def set_file_path(path):
    global file_path
    file_path = path
def open_file():

    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        code_input.delete('1.0', END)
        code_input.insert('1.0', code)
        set_file_path(path)
def save():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = code_input.get('1.0', END)
        file.write(code)
        set_file_path(path)
def run():
    if file_path == '':
        messagebox.showerror("Python IDLE", "Save Your Code")
        return
    command = f'python3 {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
#  input area
code_input = Text(root, font=("Consolas", "18"),bg="white", bd=5, pady=5, padx=5)
code_input.place(x=120, y=0, width=1200)
#output area
code_output = Text(root, font=("Consolas", "18"), bg="black", fg="lightgreen", bd=5, highlightcolor="yellow")
code_output.place(x=120, y=600, width=1200, height=100)
## Menus
Run = Image.open("run.png")
Save = Image.open("save.png")
menubar = Menu(root)
filebar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filebar)

openbar = Menu(menubar, tearoff=0)
filebar.add_cascade(label='Open', menu=openbar)
openbar.add_command(label="Open",   command=open_file)  #open bar
root.config(menu=menubar)
reimage_1 = Run.resize((100, 100))
img = ImageTk.PhotoImage(reimage_1)
reimage_2 = Save.resize((100, 100))
img1 = ImageTk.PhotoImage(reimage_2)
## buttons
Button(root, image=img, bg="#323846", bd=0, command=run).place(x=10, y=30) ## run button
Button(root, image=img1, bg="#323846", bd=0, command=save).place(x=10, y=200) ## save button
## More button could be added like this.
root.mainloop()



