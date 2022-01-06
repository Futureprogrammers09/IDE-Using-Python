'''
Name : Source code Editor in Python,
Author : FutureProgrammers( Abheet ),
Licence : MIT Licence,
Publisher : https://github.com/futureprogrammers09
'''

import datetime
import os
from tkinter import *
import subprocess
from tkinter.filedialog import asksaveasfilename , askopenfilename


root = Tk();
root.geometry("1320x650");
root.title("PyCharacter")
root.wm_iconbitmap("GIT LOGO.ico")
grey = "#f5f4f4"
file_path = ''
size = 20


abc = ""
if file_path != "":
    # global abc
    parent = os.path.dirname(file_path)
    print(parent)
    abc = os.listdir(parent)

now = datetime.datetime.now()
time = now.strftime("%d-%m-%Y")

if file_path == ' ':
    parent = os.path.dirname(file_path)
    print(parent)
    list = os.listdir(parent)
    value_t = '\n'.join(map(str, list))
    print(value_t)
    global_dir(value_t)

def increase():
    global size;
    size + 1
    

def set_file_path(path):
    global file_path;
    file_path = path
     

def new():
    path = askopenfilename(filetypes = [('Python File' , '*.py')])
    with open(path,  'r')  as file:
        code = file.read();
        editor.delete(1.0 , END)
        editor.insert('1.0' , code)
        # print(path)
        set_file_path(path);
         
         

def save_as():
    if file_path == ' ':
        path = asksaveasfilename(filetypes = [('Python File' , '*.py')])
         
    else:
        path = file_path
        with open(path,  'w')  as file:
            code = editor.get('1.0' , END)
            file.write(code)
            set_file_path(path);
             
         

def run():
    file =  f"python {file_path}"
    command = subprocess.Popen(file ,  stdout= subprocess.PIPE , stderr= subprocess.PIPE , shell=True)
    output , error = command.communicate()
    cmd.insert('1.0' , output)
    cmd.insert('1.0' , error)

#Editing the editor objects in the editor - IDE SOURCE CODE EDITOR - @coder09ABHEET
def cut():
    editor.event_generate(("<<Cut>>"))
def copy():
    editor.event_generate(("<<Copy>>"))
def paste():
    editor.event_generate(("<<Paste>>"))

#Get Editor Information



menu = Menu(root);

drop = Menu(menu)
drop.add_command(label="Open File" , command=new);
drop.add_command(label="New File")
drop.add_command(label="Save As" , command=save_as )
drop.add_command(label="Exit" , command=quit)
drop.add_command(label="Cut" ,command=cut)
drop.add_command(label="Copy" ,command=copy)
drop.add_command(label="Paste", command=paste)
menu.add_cascade(label="File" , menu=drop)
menu.add_command(label="Run" , command=run)

root.config(menu = menu) ;

#Frames in IDE
bottom = Frame(root,height=30 , bg="#1b39e2" , pady=10 , padx=10)
bottom.pack(fill=X, side=BOTTOM , anchor="s")

btn_1 = Button(bottom ,text = "+" , bg="#1b39e2",fg="#fff" , font=("PT Sans" , 14 , 'bold') , bd=0 , cursor="hand2" , command=increase )
btn_1.pack(side = RIGHT)

btn_text = Label(bottom ,text="Font Size",fg="#fff" , font=("PT Sans" , 13 , "bold") , bg="#1b39e2" , padx=10)
btn_text.pack(side = RIGHT)

btn_1 = Button(bottom ,text = "-" , bg="#1b39e2" ,fg="#fff" , font=("PT Sans" , 14 , 'bold') , bd=0 , cursor="hand2")
btn_1.pack(side = RIGHT)

#Time date function
time_dis = Label(bottom , text=time , bg="#1b39e2" ,fg="#fff" , font=("PT Sans" , 13 , 'bold') , bd=0 , padx=10)
time_dis.pack(side=LEFT)

#Left Sidebar in the editor
sidebar = Frame(root, width=1000 , bg=grey , padx=105 , pady=25 , bd=0)
sidebar.pack(fill=Y , side=LEFT )
text = Label(sidebar , text=abc)
text.pack()


#Main Editor - IDE
editor = Text(root , font=("PT Sans" , size),pady=15 , bd=0 , padx=15 , fg="#000")
editor.pack(fill=BOTH , expand=TRUE);

#CMD Terminal 
cmd = Text(root , height=8 , bg="#fcfcfc" , bd=0 , font=("PT Sans" , 15) , pady=20 , padx=20)
cmd.pack(anchor="se" , fill=X)

#Scroll Bar
scroll = Scrollbar(editor)
scroll.pack(fill=Y , side=RIGHT);
scroll.config(command=editor.yview)
editor.config(yscrollcommand=scroll.set) 


print(size)
root.mainloop()


