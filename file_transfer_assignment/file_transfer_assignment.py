import shutil
import os
import tkinter
import time

from tkinter import *

#Creates the frame
class ParentWindow(Frame):
    #initializes the gui interface
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry(f"{1080}x{720}")
        self.master.title("")

        #label for writing the body
        self.lblBody = Label(self.master, text = "File Trasfer System",
                             font=('Helvetica',16))
        self.lblBody.grid(row=0, columnspan=4)

        #Label for Source
        self.lblSource = Label(self.master, text = 'Source Folder', font=('Helvetica', 8))
        self.lblSource.grid(row=1, column=0, columnspan=2)

        #Label for Destination
        self.lblDest = Label(self.master, text = 'Destination Folder', font=('Helvetica', 8))
        self.lblDest.grid(row=1, column=3, columnspan=2)

        #Entry for Source
        self.entSourceFolder = Entry(self.master, font=('Helvetica', 10))
        self.entSourceFolder.grid(row=2, column=0)

        #Button for Source
        self.btnSource = Button(self.master, text='Select', width=10,height=1, command=self.viewSource)
        self.btnSource.grid(row=2,column=1)
        
        #Entry for Destination
        self.entDestFolder = Entry(self.master, font=('Helvetica', 10))
        self.entDestFolder.grid(row=2,column=3)

        #Button for Destination
        self.btnDest = Button(self.master, text='Select', width=10,height=1, command=self.viewDest)
        self.btnDest.grid(row=2,column=4)

        #List Entry for Source
        self.listSource = Listbox(self.master, width=40, height=20)
        self.listSource.grid(row=3,column=0,columnspan=2)
        
        #List Entry for Destination
        self.listDest = Listbox(self.master,width=40, height=20)
        self.listDest.grid(row=3,column=3,columnspan=2)
            
        #view button that calls the view function
        self.btnTransAll = Button(self.master, text='Transfer All Files', width=20, height=2,
                             command=self.transferAll)
        self.btnTransAll.grid(row=4, column=0, columnspan = 2)
        
        #Transfer button that will use the transfer function
        self.btnTransfer = Button(self.master, text='Transfer files modded within 24hrs', width=30, height=2,
                             command=self.transfer24)
        self.btnTransfer.grid(row=4, column=3, columnspan = 2)
        
        #cancel button that calls the clear
        self.btnClear = Button(self.master, text='Clear All', width=10, height=2,
                             command=self.clear, bg='blue',fg='white')
        self.btnClear.grid(row=5,column=0, columnspan=2)
        
        #cancel button that calls the cancel function
        self.btnClose = Button(self.master, text='Close', width=10, height=2,
                             command=self.close, bg='red',fg='white')
        self.btnClose.grid(row=5,column=3, columnspan=2)
        
    def viewSource(self):
        source = self.entSourceFolder.get()
        filesSource = os.listdir(source)
        print(filesSource)

        self.listSource.delete(0,END)
        if not filesSource:
            self.listSource.insert(END, 'There is nothing here!')
        else:
            for i in filesSource:
                self.listSource.insert(END, i)
    def viewDest(self):
        destination = self.entDestFolder.get()
        filesDest = os.listdir(destination)
        print(filesDest)
        self.listDest.delete(0,END)
        if not filesDest:
            self.listDest.insert(END, 'There is nothing here!')
        else:
            for i in filesDest:
                self.listDest.insert(END, i)
    def transferAll(self):
        source = self.entSourceFolder.get()
        destination = self.entDestFolder.get()
        #grabs the source folder
        files = os.listdir(source)
        #
        for i in files:
            shutil.move(source+i, destination)
        self.listSource.delete(0,END)
        self.listDest.delete(0,END) 
    #transfers files from source to destination
    def transfer24(self):
        source = self.entSourceFolder.get()
        destination = self.entDestFolder.get()
        #grabs the source folder
        files = os.listdir(source)
        #
        for i in files:
            modFileTime = os.path.getmtime(source+i)
            if (time.time() - modFileTime) / 3600 > 24:
                shutil.move(source+i, destination)
        self.listSource.delete(0,END)
        self.listDest.delete(0, END)
    #function closes out the application
    def clear(self):
        self.listSource.delete(0,END)
        self.listDest.delete(0,END)
        self.entSourceFolder.delete(0, END)
        self.entDestFolder.delete(0,END)
    #function closes out the application
    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
 
