import time
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tick Tack Toe")

click = True
def cheaker(buttons):
    global click
    #buttons["text"] == " " and 
    if click == True:
        buttons["text"] = "X"
        click = False
    elif click == False:
        buttons["text"] = "O"
        click = True
    if(button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
         button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
         button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
         button5["text"] == "X" and button2["text"] == "X" and button8["text"] == "X" or
         button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
         button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
         button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" ):
        tkinter.messagebox.showinfo("Winner", "X has won a game")
        tk.destroy()
        time.sleep(3)
        quit()
        
    if(button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
         button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
         button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
         button5["text"] == "O" and button2["text"] == "O" and button8["text"] == "O" or
         button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
         button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
         button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" ):
        tkinter.messagebox.showinfo("Winner", "O has won a game")
        tk.destroy()
        time.sleep(3)
        quit()
    
buttons = StringVar()

button1 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button1))
button1.grid(row = 1, column = 0, sticky = S+N+E+W)
button2 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button2))
button2.grid(row = 2, column = 0, sticky = S+N+E+W)
button3 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button3))
button3.grid(row = 3, column = 0, sticky = S+N+E+W)
#########################################################################################################################
button4 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button4))
button4.grid(row = 1, column = 1, sticky = S+N+E+W)
button5 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button5))
button5.grid(row = 2, column = 1, sticky = S+N+E+W)
button6 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button6))
button6.grid(row = 3, column = 1, sticky = S+N+E+W)
#########################################################################################################################
button7 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button7))
button7.grid(row = 1, column = 2, sticky = S+N+E+W)
button8 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button8))
button8.grid(row = 2, column = 2, sticky = S+N+E+W)
button9 = Button(tk, text = " ", font = "algerian 30 bold", height = 4, width = 8, command = lambda:cheaker(button9))
button9.grid(row = 3, column = 2, sticky = S+N+E+W)
#########################################################################################################################

tk.mainloop()
