import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator!")
        self.master.minsize(900,300)
        self.master.maxsize(900,300)
        label = Label(text="Enter custom text or click the Default HTML Page button")
        label.grid(row=0,column=1)
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=4, column=3,padx=(0,10))
        self.custombtn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.custombtn.grid(row=4, column=6)
        self.entry = Entry(width=40)
        self.entry.grid(row=2, column =1, padx=(10,0), pady=(10,0))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def customHTML(self):
        entry = Entry(self)
        customText = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + customText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
