'''class Line:

    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def distance(self,cord1,cord2):

        distance = ((cord2[0] - cord1[0]) ** 2 + (cord2[1] - cord1[1]) ** 2) ** 0.5
        return distance

    def slope(self,cord1,cord2):
        slope = ((cord2[1]-cord1[1])/(cord2[0]-cord1[0]))
        return slope

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

print(li.distance(coordinate1,coordinate2))
print(li.slope(coordinate1,coordinate2))'''


class Cylinder:
    pi = 3.14

    def __init__(self,height = 1,radius = 1):
        self.height = height
        self.radius = radius

    def volume(self,):
        volume = (Cylinder.pi*((self.radius)**2)*self.height)
        print(volume)

    def surface_area(self):
        area = (2*Cylinder.pi*self.radius*self.height) + (2*Cylinder.pi*self.radius*self.radius)
        print(area)


class Account:
    def __init__(self,name,funds):
        self.name = name
        self.funds = funds

    def __str__(self):
        print(f"Account Owner : {self.name}")

    def __len__(self):
        print()

    def owner(self):
        print(self.name)

    def balance(self):
        print(self.funds)

    def deposit(self,number):
        print("Deposit Accepted")
        self.funds = self.funds + number
        return self.funds

    def withdraw(self,number):
        if self.funds > number:
            print("Withdrawal accepted")
            self.funds = self.funds - number
            return self.funds
        else:
            print("Not enough funds ")

    def again(self):
        input("Do you want to do any thing else [Y/N]:").lower()



act1 = Account("User",100)

turn = 0
while True:
    try:
        print(act1)
    except TypeError:
        pass
    if turn == 0:
        user = input("What do you want to do ""\n""1)Withdraw""\n""2)Deposit""\n" "3)Check Balance : ")
        print('\n'*100)

        if user == "1":
            wit_amount = int(input("How Much Do you want to withdraw : "))
            act1.withdraw(wit_amount)
            again1 = input("Do you want to do anything else [Y/N]: ").lower()
            if again1 == "y":
                turn = 0
                print("\n" * 100)
                continue
            else:
                turn = 1
                break
        if user == "2":
            dep_amount = int(input("How Much Do you want to Deposit : "))
            act1.deposit(dep_amount)
            again_2 = input("Do you want to do anything else [Y/N]: ").lower()
            if again_2 == "y":
                turn = 0
                print("\n" * 100)
                continue
            else:
                turn = 1
                break

        if user == "3":
            print("The account balance is $",end ="")
            act1.balance()
            again = input("Do you want to do anything else [Y/N]: ").lower()
            if again == "y":
                turn = 0
                print("\n"*100)
                continue
            else:
                turn = 1
                break

    else:
        print("\n""Thank You Bye")




