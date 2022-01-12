class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print('Your total balance is $1000')

    def withdrawl(self,balance):
        new_amount = 100 - balance
        print("You have withdrawn amount "+str(balance) + ". Your remaining balance is "+ str(new_amount))

def main():
    print("This is the World Bank")
    Account = input("Please enter your acount number: ")
    Card_number = input("Insert your card number: ")
    pin_number  = input("Enter your pin number: ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.Withdrawl")
    number = int(input("Enter the number : "))

    if (number == 1):
        new_user.check_balance()
    elif (number == 2):
        balance = int(input("Enter the amount to withdraw : "))
        new_user.withdrawl(balance)
    else:
        print("Enter a number you want to be your account :")

if __name__ == "__main__":
    main()