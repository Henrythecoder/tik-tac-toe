from tkinter import *
from tkinter import messagebox
import tkinter as tk


root = Tk()
root.title("Tik-Tak-Toe")

player = 1

def btn_click(buttons):
    global player
    # when button is clicked check for win else if "not used" put corresponding letter
    if buttons["text"] == "":
        if player == 1:
            buttons["text"] = "X"

            check_for_win()
            player = 2

        else:
            buttons["text"] = "O"
            check_for_win()
            player = 1


def check_for_win():
    if button1["text"]== "O" and button2["text"] == "O" and button3["text"] == "O" \
            or button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" \
            or button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" \
            or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" \
            or button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" \
            or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" \
 \
            or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" \
            or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" \
            or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" \
            or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" \
            or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" \
            or button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" \
 \
            or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" \
            or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" \
            or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" \
            or button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" :

        messagebox.showinfo("Title", "PLAYER "+str(player)+" WINS")
# place all buttons
button1 = Button(root,font="Times 40", height=4, width=8, command= lambda: btn_click(button1))
button1.grid(row=0, column=0)

button2 = Button(root,font="Times 40", height=4, width=8, command= lambda: btn_click(button2))
button2.grid(row=0, column=1)

button3 = Button(root,font="Times 40", height=4, width=8, command= lambda: btn_click(button3))
button3.grid(row=0, column=2)

button4 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button4))
button4.grid(row=1, column=0)

button5 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button5))
button5.grid(row=1, column=1)

button6 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button6))
button6.grid(row=1, column=2)

button7 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button7))
button7.grid(row=2, column=0)

button8 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button8))
button8.grid(row=2, column=1)

button9 = Button(root,font="Times 40",height=4, width=8,command= lambda: btn_click(button9))
button9.grid(row=2, column=2)

player1_label = tk.Label(text="player1:", font="Times 20")
player1_label.grid(row=0,column=6)



root.mainloop()