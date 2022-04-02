import os
from tkinter import *
from tkinter import Place, filedialog, mainloop
from tkinter import Button, Label, ttk
import tkinter as tk

class wii: 

        def __init__(self) -> None:

                self.root = tk.Tk()

                self.frm = ttk.Frame(self.root).grid()
                self.root.title('NASOS DECODER')
                self.root.geometry('800x400')
                #self.root.resizable(False, False)
                screen_width = self.root.winfo_screenwidth()
                screen_height = self.root.winfo_screenheight()
                x_cordinate = int((screen_width/2) - (800/2))
                y_cordinate = int((screen_height/2) - (400/2))
                self.root.geometry("{}x{}+{}+{}".format(800, 400, x_cordinate, y_cordinate))
                self.upload_filevar = tk.StringVar()
                
       
                self.home()

        def home(self):
                self.next_btn = tk.Button(self.root, text='select file', command=self.browseFiles, width=7, height=1)
                self.next_btn.place(x=200, y=150)
                self.con_btn = tk.Button(self.root, text='Confirm', command=self.confirm, width=7, height=1)
                self.con_btn.place(x=350, y=220)
                self.cons = tk.Label(self.root, text="                   WHEN YOU CLICK CONFIRM, PROGRESS HAPPENS IN COMMAND PROMPT AND THE APPLICATION \n                  MAY BECOME UNRESPONSIVE JUST MINIMIZE IT WILL BECOME ACTIVE WHNE PROCESS IS FINISHED", font=('calibre', 10, 'bold')).place(x=1, y=50)
                

        def browseFiles(self):
                self.upload_filevar = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Nasos", "*.dec*"), ("all files", "*.*")))
                tk.Label(self.root, text=self.upload_filevar, font=('calibre', 10, 'bold')).place(x=350,y=150)

        def confirm(self):
           os.system(f'start cmd /k dec-decode.exe "{self.upload_filevar}"')  
           
                   

root=wii()
root = mainloop()           

