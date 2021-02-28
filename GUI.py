from tkinter import *
import tkinter.messagebox


def insert0():
    v0 = 0
    txtScreen.insert(END, v0)


def insert1():
    v1 = 1
    txtScreen.insert(END, v1)


def insert2():
    v2 = 2
    txtScreen.insert(END, v2)


def insert3():
    v3 = 3
    txtScreen.insert(END, v3)


def insert4():
    v4 = 4
    txtScreen.insert(END, v4)


def insert5():
    v5 = 5
    txtScreen.insert(END, v5)


def insert6():
    v6 = 6
    txtScreen.insert(END, v6)


def insert7():
    v7 = 7
    txtScreen.insert(END, v7)


def insert8():
    v8 = 8
    txtScreen.insert(END, v8)


def insert9():
    v9 = 9
    txtScreen.insert(END, v9)


def cancel():
    Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel!")
    if Cancel > 0:
        root.destroy()
        return


def clear():
    txtScreen.delete("1.0", END)
    buttonLeftarrow1 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
    buttonLeftarrow1.grid(row=0, column=0, padx=2, pady=2)

    buttonLeftarrow2 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
    buttonLeftarrow2.grid(row=1, column=0, padx=2, pady=2)

    buttonLeftarrow3 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
    buttonLeftarrow3.grid(row=2, column=0, padx=2, pady=2)

    buttonLeftarrow4 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
    buttonLeftarrow4.grid(row=3, column=0, padx=2, pady=2)

    buttonRightarrow1 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
    buttonRightarrow1.grid(row=0, column=0, padx=2, pady=2)

    buttonRightarrow2 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
    buttonRightarrow2.grid(row=1, column=0, padx=2, pady=2)

    buttonRightarrow3 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
    buttonRightarrow3.grid(row=2, column=0, padx=2, pady=2)

    buttonRightarrow4 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
    buttonRightarrow4.grid(row=3, column=0, padx=2, pady=2)


def pin_check():
    pinNo = txtScreen.get("1.0", "end-1c")
    if pinNo == str(1234):
        txtScreen.delete("1.0", END)

        txtScreen.insert(END, '\t\t   XXX BANK ' + "\n\n\n\n")
        txtScreen.insert(END, 'WITHDRAW\t\t\t\tDEPOSIT ' + "\n\n\n")
        txtScreen.insert(END, 'INFO\t\t\t\tHISTORY ' + "\n\n\n")
        txtScreen.insert(END, 'EDIT\t\t\t\t LOGOUT ' + "\n\n\n")
        buttonLeftarrow1 = Button(topFrame2left, text=">>>", width=20, height=3, state=NORMAL)
        buttonLeftarrow1.grid(row=0, column=0, padx=2, pady=2)

        buttonLeftarrow1 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=NORMAL)
        buttonLeftarrow1.grid(row=0, column=0, padx=2, pady=2)

        buttonLeftarrow2 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=NORMAL)
        buttonLeftarrow2.grid(row=1, column=0, padx=2, pady=2)

        buttonLeftarrow3 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=NORMAL)
        buttonLeftarrow3.grid(row=2, column=0, padx=2, pady=2)

        buttonLeftarrow4 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=NORMAL)
        buttonLeftarrow4.grid(row=3, column=0, padx=2, pady=2)

        buttonRightarrow1 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=NORMAL)
        buttonRightarrow1.grid(row=0, column=0, padx=2, pady=2)

        buttonRightarrow2 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=NORMAL)
        buttonRightarrow2.grid(row=1, column=0, padx=2, pady=2)

        buttonRightarrow3 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=NORMAL)
        buttonRightarrow3.grid(row=2, column=0, padx=2, pady=2)

        buttonRightarrow4 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=NORMAL)
        buttonRightarrow4.grid(row=3, column=0, padx=2, pady=2)
    else:
        txtScreen.delete("1.0", END)
        txtScreen.insert(END, '\t\t   Invalid Pin ' + "\n\n\n\n")


root = tkinter.Tk()
root.title(100 * " " + "ATM")
root.geometry("830x590+280+0")
root.configure(background="gainsboro")

# ==============================FRAMES===============================================
mainFrame = tkinter.Frame(root, bd=20, width=784, height=700, relief=RIDGE)
mainFrame.grid()

topFrame1 = tkinter.Frame(mainFrame, bd=7, width=734, height=300, relief=RIDGE)
topFrame1.grid(row=2, column=0, padx=12)

topFrame2 = tkinter.Frame(mainFrame, bd=7, width=734, height=300, relief=RIDGE)
topFrame2.grid(row=0, column=0, padx=8)

topFrame2left = tkinter.Frame(topFrame2, bd=5, width=190, height=300, relief=RIDGE)
topFrame2left.grid(row=0, column=0, padx=2)

topFrame2mid = tkinter.Frame(topFrame2, bd=5, width=200, height=300, relief=RIDGE)
topFrame2mid.grid(row=0, column=1, padx=2)

topFrame2right = tkinter.Frame(topFrame2, bd=5, width=190, height=300, relief=RIDGE)
topFrame2right.grid(row=0, column=2, padx=2)

# ==============================WITGES===============================================

txtScreen = tkinter.Text(topFrame2mid, height=12, width=42, bd=12, font=("arial", 12, "bold"))
txtScreen.grid(row=0, column=0)

# ================================TOP LEFT BUTTONS===============================================
buttonLeftarrow1 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
buttonLeftarrow1.grid(row=0, column=0, padx=2, pady=2)

buttonLeftarrow2 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
buttonLeftarrow2.grid(row=1, column=0, padx=2, pady=2)

buttonLeftarrow3 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
buttonLeftarrow3.grid(row=2, column=0, padx=2, pady=2)

buttonLeftarrow4 = tkinter.Button(topFrame2left, text=">>>", width=20, height=3, state=DISABLED)
buttonLeftarrow4.grid(row=3, column=0, padx=2, pady=2)
# ================================TOP RIGHT BUTTONS===============================================

buttonRightarrow1 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
buttonRightarrow1.grid(row=0, column=0, padx=2, pady=2)

buttonRightarrow2 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
buttonRightarrow2.grid(row=1, column=0, padx=2, pady=2)

buttonRightarrow3 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
buttonRightarrow3.grid(row=2, column=0, padx=2, pady=2)

buttonRightarrow4 = tkinter.Button(topFrame2right, text="<<<", width=20, height=3, state=DISABLED)
buttonRightarrow4.grid(row=3, column=0, padx=2, pady=2)

# ================================PIN BUTTONS===============================================

pinBtn1 = tkinter.Button(topFrame1, text="1   (QZ)", width=20, height=3, state=NORMAL, command=insert1)
pinBtn1.grid(row=2, column=0, padx=6, pady=4)

pinBtn2 = tkinter.Button(topFrame1, text="2   (ABC)", width=20, height=3, state=NORMAL, command=insert2)
pinBtn2.grid(row=2, column=1, padx=6, pady=4)

pinBtn3 = tkinter.Button(topFrame1, text="3   (DEF)", width=20, height=3, state=NORMAL, command=insert3)
pinBtn3.grid(row=2, column=2, padx=6, pady=4)

pinBtnCnc = tkinter.Button(topFrame1, text="CANCEL", width=20, height=3, state=NORMAL, background="red", command=cancel)
pinBtnCnc.grid(row=2, column=3, padx=6, pady=4)

pinBtn4 = tkinter.Button(topFrame1, text="4   (GHI)", width=20, height=3, state=NORMAL, command=insert4)
pinBtn4.grid(row=3, column=0, padx=6, pady=4)

pinBtn5 = tkinter.Button(topFrame1, text="5   (JKL)", width=20, height=3, state=NORMAL, command=insert5)
pinBtn5.grid(row=3, column=1, padx=6, pady=4)

pinBtn6 = tkinter.Button(topFrame1, text="6   (MNO)", width=20, height=3, state=NORMAL, command=insert6)
pinBtn6.grid(row=3, column=2, padx=6, pady=4)

pinBtnClr = tkinter.Button(topFrame1, text="CLEAR", width=20, height=3, state=NORMAL, background="yellow",
                           command=clear)
pinBtnClr.grid(row=3, column=3, padx=6, pady=4)

pinBtn7 = tkinter.Button(topFrame1, text="7   (PRS)", width=20, height=3, state=NORMAL, command=insert7)
pinBtn7.grid(row=4, column=0, padx=6, pady=4)

pinBtn8 = tkinter.Button(topFrame1, text="8   (TUV)", width=20, height=3, state=NORMAL, command=insert8)
pinBtn8.grid(row=4, column=1, padx=6, pady=4)

pinBtn9 = tkinter.Button(topFrame1, text="9   (WXY)", width=20, height=3, state=NORMAL, command=insert9)
pinBtn9.grid(row=4, column=2, padx=6, pady=4)

pinBtnEnt = tkinter.Button(topFrame1, text="ENTER", width=20, height=3, state=NORMAL, background="green",
                           command=pin_check)
pinBtnEnt.grid(row=4, column=3, padx=6, pady=4)

pinBtnE = tkinter.Button(topFrame1, width=20, height=3, state=DISABLED)
pinBtnE.grid(row=5, column=0, padx=6, pady=4)

pinBtn0 = tkinter.Button(topFrame1, text="0", width=20, height=3, state=NORMAL, command=insert0)
pinBtn0.grid(row=5, column=1, padx=6, pady=4)

pinBtnEm = tkinter.Button(topFrame1, width=20, height=3, state=DISABLED)
pinBtnEm.grid(row=5, column=2, padx=6, pady=4)

pinBtnEmp = tkinter.Button(topFrame1, width=20, height=3, state=NORMAL)
pinBtnEmp.grid(row=5, column=3, padx=6, pady=4)

if __name__ == '__main__':
    root.mainloop()
