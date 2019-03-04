'''
The sample Username and Password to enter the bank is :

Username = smith
Password = 1252

The rules of the bank is you cannot  withdraw the whole ammout there should be atleast something in the account 
No limits on depositing the money

'''






import time  # Used to create  small effect when the user is logging in


class Account:  # Main Class with User Data

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds

    # Prints when called Check Balance
    def balance(self):
        print(self.funds)

    # Deposit's the User's amount and add's it to the current balance
    def deposit(self, number):
        print("The Deposit amount was Accepted.\n")
        self.funds = self.funds + number
        return self.funds

    # Withdraw's the money user asked and subtracts it from the current balance
    def withdraw(self, number):
        if self.funds > number:
            print("The Withdrawal amount was accepted.\n")
            self.funds = self.funds - number
            return self.funds

        # If the user enter's an invalid amount to withdraw

        else:
            print("Sorry You Don't Have Enough Funds...\n ")
    #
    # def again(self):
    #     input("Do you want to do any thing else [Y/N]:").lower()

# List of Account Holder's in PyBANK


users = {"jack": {"password": "9911" , "funds": 700},
         "smith": {"password": "1252", "funds": 2000},
         "don": {"password": "1232", "funds": 1230},
         "alex": {"password": "8877", "funds": 1009},
         "max": {"password": "0001", "funds": 1340},
         }

name = 0  # Helps to control the loop for asking the user name and password
turn = 0  # Helps to control the Withdraw, Deposit, Check balance conditions
ask = 0   # Helps to control the Flow of asking the user if they want to do anything again

# The main Loop Which Controls the Program

while True:

    # Prints the name of the bank and welcomes the user...

    print("\t\tWELCOME TO PyBANK\n\n")

    # Authenticates the user by asking them their Username and Password

    while name == 0:
        print("Please enter the following...")
        username = input("Username : ").lower()
        password = input("Password : ")

        # Checks the condition and does not allow the Username to be empty

        if len(username) > 0:
            pass
        else:
            print("Username cannot be blank\n")
            continue

        # Checks the condition and does not allow the Password to be empty

        if len(password) > 0:
            pass
        else:
            print("Password cannot be blank\n")
            continue

        # Checks the user in the above Dictionary and authenticates

        if username in users:
            if password == users[username]["password"]:

                # Used this loop to show a effect when the user is logged in

                for i in range(1, 4):
                    print(".")
                    time.sleep(0.5)
                print("Login successful")
                print("\n")
                name = 1

        # If the user is not in the Dictionary does not allow them into the system

        else:
            print("Username or Password was wrong\n")
            name = 0
            continue

            # act1 is the user

        try:
            act1 = Account(username, users[username]["funds"])
        except KeyError:
            print("Wrong password try again")
            continue

        # turn helps to control the flow of transaction control

        while turn == 0:

            # Asks the User What task do they want to perform..

            user = input("What do you want to do select from the number below...""\n""1]Withdraw.""\n""2]Deposit.""\n" 
                         "3]Check Balance.""\n""--> ")
            print('\n\n')

            # Allow's User to Withdraw money

            if user == "1":
                wit_amount = int(input("How Much Amount Do you want to Withdraw $: ""\n"))
                act1.withdraw(wit_amount)

                # Ask's they User if they want to Do any task again.

                while ask == 0:
                    again1 = input("Do you want to do anything else [Y/N]: ").lower()
                    if again1 == "yes":
                        turn = 0
                        print("\n\n\n")
                        break
                    elif again1 == "no":
                        turn = 1
                        break
                    else:
                        print("Please only write yes or no.\n")
                        ask = 0
                        continue

            # Allow's User to Deposit money

            if user == "2":
                dep_amount = int(input("How Much Amount Do you want to Deposit : ""\n"))
                act1.deposit(dep_amount)

                # Ask's they User if they want to Do any task again.

                while ask == 0:
                    again2 = input("Do you want to do anything else [Y/N]: ").lower()
                    if again2 == "yes":
                        turn = 0
                        print("\n\n\n")
                        break
                    elif again2 == "no":
                        turn = 1
                        break
                    else:
                        print("Please only write yes or no.\n")
                        ask = 0
                        continue

            # Allow's User to Check Balance.

            if user == "3":
                print("The Current Account balance is $",end ="")
                act1.balance()

                # Ask's they User if they want to Do any task again.

                while ask == 0:
                    again = input("Do you want to do anything else [Y/N]: ").lower()
                    if again == "yes":
                        turn = 0
                        print("\n\n\n")
                        break
                    elif again == "no":
                        turn = 1
                        break
                    else:
                        print("Please only write yes or no.\n")
                        ask = 0
                        continue

    else:
        print("\n""Thank You For Using PyBank..")
        break


