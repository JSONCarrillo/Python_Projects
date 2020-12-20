#import tkinter for the GUI and os for opening up the browser window
import tkinter
import os

from tkinter import *

#Creates the frame
class ParentWindow(Frame):
    #initializes the gui interface
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry(f"{1080}x{720}")
        self.master.title("Web Page Generator")

        #label for writing the body
        self.lblBody = Label(self.master, text = "Write HTML Body Here!",
                             font=('Helvetica',20))
        self.lblBody.grid(row=0, columnspan=2)

        #creates the text box for users to write their html
        self.txtBody = Text(self.master, height=20, width=100)
        self.txtBody.grid(row=1,columnspan=2)

        #subit button that calls the submit function
        self.sumbit = Button(self.master, text='Submit', width=10, height=2,
                             command=self.submit)
        self.sumbit.grid(row=2, column=0)

        #cancel button that calls the cancel function
        self.cancel = Button(self.master, text='Cancel', width=10, height=2,
                             command=self.cancel)
        self.cancel.grid(row=2, column=1)
        
    def submit(self):
        #saves the input of the text box as a variable
        submittedText = self.txtBody.get("1.0", END)

        #saves the full html tags as a variable and formats the submitted user text into a wildcard
        html = f"<html><body>{submittedText}</body></html>"

        #creates and writes into a generated html file 
        wrt = open ("web_page_generator.html", "w")

        #writes the html variable into the document
        wrt.write(html)
        wrt.close()

        #os opens the file in browser containing the written code from the user
        os.startfile("web_page_generator.html")

    #function closes out the application
    def cancel(self):
        self.master.destroy()      

if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
 
