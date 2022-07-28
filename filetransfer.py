import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets the title of window
        self.master.title("File Transfer")
        #button to select files from source dir
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #entry for source dir selection
        self.source_dir = Entry(width=75)
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #button to select destination
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column = 0, padx=(20,10), pady=(15,10))

        #entry for destination
        self.destination_dir = Entry(width=75)
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the conent that is inserted in entry, to insert our own path
        self.source_dir.delete(0,END)
        #insert method will insert the user slecetion
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):

        time = os.path.getmtime(tkinter.filedialog.askdirectory())
        if time <= 24:
            transferFiles(self)
        #source directory retrieved
        source = self.source_dir.get()
        #destination dir retrieved
        destination = self.destination_dir.get()
        #list of files in source dir
        source_files = os.listdir(source)
        #runs through each file in dir
        for i in source_files:
            #moves file to destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfullyt transferred.')

    def exit_program(self):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


