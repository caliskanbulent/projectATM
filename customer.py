import fileinput
import os
import time
import sys

try:
    f = open('Accounts.txt', 'r')
    f.close()
except FileNotFoundError:
    f = open('Accounts.txt', 'w')
    f.close()


class Customer:
    def __init__(self, account_name="", account_surname="", password="", adress="", mail=""):
        self.account_name = account_name
        self.account_surname = account_surname
        self.account_password = password
        self.adress = adress
        self.mail = mail
        self.accounts_list = self.read_file('Accounts.txt')

    def read_file(self, file_name):
        opened_file = open(file_name, 'r')
        lines_list = []
        for line in opened_file:
            line = line.split()
            lines_list.append(line)
        return lines_list

    def fileInput(self, searchExp, replaceExp):
        for line in fileinput.input('Accounts.txt', inplace=1):
            if searchExp in line:
                line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)

    def edit(self, acc_list):
        for account in acc_list:
            if account[0] == self.login_id and account[3] == self.login_password:
                choice = int(input(
                    '1) edit name \n2) edit surname \n3) edit password\n4) edit adress\n5) edit mail \nchoice>> '))
                if choice == 1:
                    print(f'current name={account[1]}\n')
                    new_name = input("enter new name?")
                    self.fileInput(account[1], new_name)
                    print("The name has been changed")
                    self.menu2(account)
                elif choice == 2:
                    print(f'current name={account[2]}\n')
                    new_surname = input("enter new surname?")
                    self.fileInput(account[2], new_surname)
                    print("The surname has been changed")
                    self.menu2(account)
                elif choice == 3:
                    current_pin = (input("please enter current password"))
                    if current_pin == account[3]:
                        new_pin = input("enter new pin? ")
                        self.fileInput(account[3], new_pin)
                        print("The pin has been changed")
                        self.menu2(account)
                    else:
                        print("invalid pin")
                        self.edit(self.accounts_list)
                elif choice == 4:
                    print(f'current adress={account[4]}\n')
                    new_adress = input("enter new adress(with /)? ")
                    self.fileInput(account[4], new_adress)
                    print("The adress has been changed ")
                    self.menu2(account)
                elif choice == 5:
                    print(f'current mail={account[5]}\n')
                    new_mail = input("enter new mail? ")
                    self.fileInput(account[5], new_mail)
                    print("The mail has been changed")
                    self.menu2(account)
                else:
                    print('ERROR: Wrong choice')
                    self.edit(self.accounts_list)

    def clear_screen(self):
        os.system('cls')
        print()

    def print_process(self, process):
        date = '{}'.format(process[2:7])
        print('{0}	{1}	{2}{3: ^10} {4: ^10}'.format(
            process[0],
            process[1].center(len('change_password')),
            date.center(len(date)),
            process[7],
            process[8]
        )
        )

    def withdraw(self, ls):
        current_balance = int(ls[6])
        print('Your current balance: ' + ls[6] + ' €')
        withdraw_amount = int(input('Enter withdraw amount(€): '))
        if withdraw_amount > current_balance:
            print("ERROR: You can't withdraw more than your current balance")
        else:
            current_balance -= abs(withdraw_amount)
        file_name = ls[0] + '.txt'
        process_list = self.read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1

        id_file.write('{0}	withdraw			{1}	{2}	{3}\n'.format(str(last_id), str(time.ctime()), ls[6],
                                                                              str(current_balance)))
        id_file.close()
        ls[6] = str(current_balance)
        print('Your current balance: ' + ls[6] + ' €')
        return ls

    def deposit(self, ls):
        current_balance = int(ls[6])
        print('Your current balance: ' + ls[6] + ' €')
        deposit_amount = int(input('Enter deposit amount(€): '))
        current_balance += abs(deposit_amount)

        file_name = ls[0] + '.txt'
        process_list = self.read_file(file_name)
        id_file = open(file_name, 'a')

        if len(process_list) == 0:
            last_id = 1
        else:
            last_id = int(process_list[len(process_list) - 1][0]) + 1

        id_file.write('{0}	deposit				{1}	{2}	{3}\n'.format(str(last_id), str(time.ctime()), ls[6],
                                                                                 str(current_balance)))
        id_file.close()
        ls[6] = str(current_balance)
        print('Your current balance: ' + ls[6] + " €")

        return ls

    def show_history(self, ls):
        choice = int(input('1) show deposit processes\n2) show withdraw processes\nchoice>> '))
        file_name = ls[0] + '.txt'
        id_list = self.read_file(file_name)
        top_line = '\nID	' + 'Type'.center(len('change_password')) + 'Date and Time'.center(40) + 'before'.center(
            10) + 'after'.center(15)
        print(top_line)
        print('-' * len(top_line))
        if choice == 1:
            for line in id_list:
                if line[1] == 'deposit':
                    self.print_process(line)
        elif choice == 2:
            for line in id_list:
                if line[1] == 'withdraw':
                    self.print_process(line)
        else:
            print('ERROR: Wrong choice')

        input('\nPress Enter to go back..')

    def login(self, acc_list):
        self.login_id = input('Please, Enter your info=\n>>ID: ')
        self.login_password = input('>>Password: ')
        found = False
        for account in acc_list:
            if account[0] == self.login_id and account[3] == self.login_password:
                found = True
                self.menu2(account)
                break
            else:
                continue

        if not found:
            self.clear_screen()
            print('Wrong ID or Password')
            self.login(acc_list)

        else:
            acc_file = open('Accounts.txt', 'w')
            print('Saving changes...')
            for acc in acc_list:
                for elements in acc:
                    acc_file.write("%s	" % elements)
                acc_file.write('\n')

    def create_account(self, ls):
        self.account_name = input('Enter Your Name: ')
        self.account_surname = input('Enter Your Surname: ')
        self.adress = input('Enter Your adress: ')
        self.mail = input('Enter Your mail adress: ')
        self.account_password = input('Enter Your Password: ')

        print("Creating Your Account .....")
        accounts_file = open('Accounts.txt', 'a')

        if len(ls) == 0:
            new_last_id = 1
        else:
            new_last_id = int(ls[len(ls) - 1][0]) + 1

        line = '{0}	{1}	{2}	{3} {4} {5} 0\n'.format(str(new_last_id), self.account_name, self.account_surname,
                                                             self.account_password, self.adress, self.mail, )

        accounts_file.write(line)
        id_file_name = str(new_last_id) + '.txt'
        id_file = open(id_file_name, 'w')
        print("Your Account Has Been Created And Your Id Is " + str(new_last_id))
        id_file.close()
        accounts_file.close()
        ls.append(
            [str(new_last_id), self.account_name, self.account_surname, self.account_password, self.adress, self.mail,
             '0'])

    def menu2(self, account):
        print("\n---------Hello, {0}--------- ".format(account[1]))
        while True:
            ch = int(input(
                "\n1) show info \n2) show process history\n3) deposit\n4) withdraw\n5) Edit\n6)logout\n\nchoice>> "))
            self.clear_screen()
            if ch == 1:
                print(
                    "ID: {}\nName: {}\nSurname: {}\nAdress: {}\nMail: {}\nBalance: {}\n".format(account[0], account[1],
                    account[2], account[4],account[5], account[6]))

            elif ch == 2:
                self.show_history(account)
            elif ch == 3:
                self.deposit(account)
            elif ch == 4:
                self.withdraw(account)
            elif ch == 5:
                self.edit(self.accounts_list)
            elif ch == 6:
                break
            else:
                print("ERROR: Wrong choice\n")

    def run(self):
        count = True
        while count:
            choice = int(input('1) Login\n2) Create Account\n3) Exit\n\nchoice>>  '))
            if choice == 1:
                self.clear_screen()
                try:
                    self.login(self.accounts_list)
                except KeyboardInterrupt:
                    self.clear_screen()

            elif choice == 2:
                self.create_account(self.accounts_list)

            elif choice == 3:
                exit()
            else:
                self.clear_screen()
                print("ERROR: Wrong choice\n")


root = Customer()
root.run()
