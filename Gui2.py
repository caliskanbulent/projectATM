import tkinter as tk
from tkinter import messagebox
from ATM_project import customer



# GLOBAL VARIABLES FOR COLORS
w = '#FFFFFF'
g = '#20FF0F'
lg = '#778899'
r = '#8B0000'

class Gui_atm(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, bg=w, **kwargs)


        self.cst=customer.Customer
        self.master=master
        self.master.title('ATM')
        self.master.config(bg=w)
        self.master.geometry('350x500')
        self.master.resizable(False, False)

        self.head = tk.Label(self.master, text=' WELCOME TO THE XXX BANK ATM ', justify='center', bg=w, font='Courier 13')
        self.head.grid(row=0, column=0, pady=6)

        self.log_head = tk.Label(self.master, text=f"{15 * '-'} LOGIN {15 * '-'}", justify='center', bg=w, font='Courier 10')
        self.log_head.grid(row=1, column=0, pady=6)

        self.sig_head = tk.Label(self.master, text=f"{15 * '-'} SIGNUP {15 * '-'}", justify='center', bg=w, font='Courier 10')
        self.sig_head.grid(row=6, column=0, pady=6)
        # LOGIN SECTION
        self.log_id = tk.Label(self.master, text='Account No', bg=w, font='Courier 10')
        self.log_id.grid(row=2, column=0, sticky='w')
        self.id_box = tk.Entry(self.master, bg=lg, width=32)
        self.id_box.grid(row=2, column=0, sticky='e', padx=2)

        self.log_pin = tk.Label(self.master, text='Pin', bg=w, font='Courier 10')
        self.log_pin.grid(row=3, column=0, sticky='w')
        self.log_box = tk.Entry(self.master, bg=lg, show='*', width=32)
        self.log_box.grid(row=3, column=0, sticky='e', padx=2)

        self.log_btn = tk.Button(self.master, text='Login', bg=g, relief='flat', width=18,command=lambda:[self.destroy_master(), self.login_page()])
        self.log_btn.grid(row=4, column=0, columnspan=2, pady=6, padx=2, sticky='e')

        self.log_out = tk.Label(self.master, text='', bg=w, font='Courier 9', width=19)
        self.log_out.grid(row=5, column=0, sticky='e')

        # SIGNUP SECTION
        self.name = tk.Label(self.master, text='Name', bg=w, font='Courier 9')
        self.name.grid(row=7, column=0, sticky='w')
        self.name_box = tk.Entry(self.master, bg=lg, width=32)
        self.name_box.grid(row=7, column=0, sticky='e', padx=2)

        self.surname = tk.Label(self.master, text='Surname', bg=w, font='Courier 9')
        self.surname.grid(row=8, column=0, sticky='w')
        self.surname_box = tk.Entry(self.master, bg=lg, show='*', width=32)
        self.surname_box.grid(row=8, column=0, sticky='e', padx=2)

        self.pin = tk.Label(self.master, text='Pin', bg=w, font='Courier 9')
        self.pin.grid(row=9, column=0, sticky='w')
        self.pin_box = tk.Entry(self.master, bg=lg, show='*', width=32)
        self.pin_box.grid(row=9, column=0, sticky='e', padx=2)

        self.adress = tk.Label(self.master, text='Adress', bg=w, font='Courier 9')
        self.adress.grid(row=10, column=0, sticky='w')
        self.adress_box = tk.Entry(self.master, bg=lg, width=32)
        self.adress_box.grid(row=10, column=0, sticky='e', padx=2)

        self.mail = tk.Label(self.master, text='mail', bg=w, font='Courier 9')
        self.mail.grid(row=11, column=0, sticky='w')
        self.mail_box = tk.Entry(self.master, bg=lg, width=32)
        self.mail_box.grid(row=11, column=0, sticky='e', padx=2)

        self.balance = tk.Label(self.master, text='Balance', bg=w, font='Courier 9')
        self.balance.grid(row=12, column=0, sticky='w')
        self.balance_box = tk.Entry(self.master, bg=lg, width=32)
        self.balance_box.grid(row=12, column=0, sticky='e', padx=2)

        self.sin_btn = tk.Button(self.master, text='SignUp', bg=g, relief='flat', width=18)
        self.sin_btn.grid(row=13, column=0, columnspan=2, pady=6, padx=2, sticky='e')

        self.sin_out = tk.Label(self.master, text='', bg=w, font='Courier 9', width=19)
        self.sin_out.grid(row=14, column=0, sticky='e')

        self.quit_btn = tk.Button(self.master, text='Quit', bg=r, relief='flat')
        self.quit_btn.grid(row=15, column=0, sticky='w', padx=4)
    def logOut_menu(self):
        root = tk.Tk()
        run = Gui_atm(root)
        run.mainloop()
    def destroy_master(self):
        self.master.destroy()

    def destroy_editPage(self):
        self.editPage.destroy()

    def destroy_logPage(self):
        self.logPage.destroy()


    def login_page(self,logPage=None):
        self.logPage=logPage
        self.logPage=tk.Tk()
        self.logPage.title('ATM')
        self.logPage.config(bg=w)
        self.logPage.geometry('350x500')
        self.logPage.resizable(False, False)
        self.head = tk.Label(self.logPage, text=' WELCOME TO THE XXX BANK ATM ', justify='center', bg=w, font='Courier 13')
        self.head.grid(row=0, column=0, pady=6)

        self.log_head = tk.Label(self.logPage, text=f"{15 * '-'} HELLO xxx {15 * '-'}", justify='center', bg=w, font='Courier 10')
        self.log_head.grid(row=1, column=0, pady=6)
        self.balan = tk.Label(self.logPage, text=f'Your current balance\nis xxx', bg=w, font='Courier 11',justify='center')
        self.balan.grid(row=2, column=0, columnspan=2, pady=5, padx=4)


        # LOGIN SECTION
        self.log_btn = tk.Button(self.logPage, text='Deposit', bg=g, relief='flat', width=18)
        self.log_btn.grid(row=3, column=0, sticky='w')
        self.id_box = tk.Entry(self.logPage, bg=lg, width=32)
        self.id_box.grid(row=3, column=0, sticky='e', padx=2)
        self.log_out = tk.Label(self.logPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out.grid(row=4, column=0)

        self.log_btn2 = tk.Button(self.logPage, text='Withdraw', bg=g, relief='flat', width=18)
        self.log_btn2.grid(row=5, column=0, sticky='w')
        self.log_box = tk.Entry(self.logPage, bg=lg, show='*', width=32)
        self.log_box.grid(row=5, column=0, sticky='e', padx=2)
        self.log_out2 = tk.Label(self.logPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out2.grid(row=6, column=0)

        self.sin_btn = tk.Button(self.logPage, text='My Info', bg=g, relief='flat', width=18)
        self.sin_btn.grid(row=7, column=0, sticky='w')
        self.log_out3 = tk.Label(self.logPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out3.grid(row=8, column=0)
        self.sin_btn = tk.Button(self.logPage, text='show process history', bg=g, relief='flat', width=18)
        self.sin_btn.grid(row=9, column=0, sticky='w')
        self.log_out4 = tk.Label(self.logPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out4.grid(row=10, column=0)
        self.sin_btn = tk.Button(self.logPage, text='Edit', bg=g, relief='flat', width=18,command=lambda:[self.destroy_logPage(), self.edit()])
        self.sin_btn.grid(row=11, column=0, columnspan=2, sticky='w')

        self.logout_btn = tk.Button(self.logPage, text='LOG OUT', bg=r, relief='flat',command=lambda:[self.destroy_logPage(), self.logOut_menu()])
        self.logout_btn.grid(row=15, column=0, sticky='n', padx=4)

    def edit(self,editPage=None):

        self.editPage = editPage
        self.editPage = tk.Tk()
        self.editPage.title('ATM')
        self.editPage.config(bg=w)
        self.editPage.geometry('350x500')
        self.editPage.resizable(False, False)
        self.head = tk.Label(self.editPage, text=' WELCOME TO THE XXX BANK ATM ', justify='center', bg=w,font='Courier 13')
        self.head.grid(row=0, column=0, pady=6)

        self.log_head = tk.Label(self.editPage, text=f"{15 * '-'} HELLO xxx {15 * '-'}", justify='center', bg=w,font='Courier 10')
        self.log_head.grid(row=1, column=0, pady=6)

        self.edit_adress = tk.Button(self.editPage, text='New Adress', bg=g, relief='flat', width=18)
        self.edit_adress.grid(row=2, column=0, sticky='w')
        self.edit_adress_box = tk.Entry(self.editPage, bg=lg, width=32)
        self.edit_adress_box.grid(row=2, column=0, sticky='e', padx=2)
        self.log_out = tk.Label(self.editPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out.grid(row=3, column=0)

        self.edit_mail = tk.Button(self.editPage, text='New mail', bg=g, relief='flat', width=18)
        self.edit_mail.grid(row=4, column=0, sticky='w')
        self.edit_mail_box = tk.Entry(self.editPage, bg=lg, show='*', width=32)
        self.edit_mail_box.grid(row=4, column=0, sticky='e', padx=2)
        self.log_out2 = tk.Label(self.editPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out2.grid(row=5, column=0)

        self.edit_pin = tk.Button(self.editPage, text='New Pin', bg=g, relief='flat', width=18)
        self.edit_pin.grid(row=6, column=0, sticky='w')
        self.edit_pin_box = tk.Entry(self.editPage, bg=lg, show='*', width=32)
        self.edit_pin_box.grid(row=6, column=0, sticky='e', padx=2)
        self.log_out3 = tk.Label(self.editPage, text='', bg=w, font='Courier 9', width=19)
        self.log_out3.grid(row=7, column=0)

        self.logout_btn = tk.Button(self.editPage, text='LOG OUT', bg=r, relief='flat',command=lambda:[self.destroy_editPage(), self.login_page()])
        self.logout_btn.grid(row=15, column=0, sticky='n', padx=4)

root = tk.Tk()
run = Gui_atm(root)

run.mainloop()


