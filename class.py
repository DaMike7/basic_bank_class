import random
class Account:
    def __init__(self,Bank_Name):
        self.Bank_Name = Bank_Name
        self.User_account_name = ""
        self.User_account_number = 0
        self.User_pin = 0
        self.User_account_balance = 0
        self.User_info ={}
        
    def bank_name(self):
        name = f"{self.Bank_Name}."
        return name

    def CheckBalance(self):
        if self.User_info:
            for M in range(2):
                try:
                    VERIFY = int(input("\nEnter Pin To Proceed\n"))
                except:
                    print("\ndigits only")
                else:
                    if VERIFY == self.User_pin:
                        print("processing....")
                        return self.User_account_balance
                    else:
                        print("\nincorrect!\nyou have 1 chance(s) left")
        else:
            print("\nno account found\ncan\'t perform action")

    def Create_acc(self):
        print("\nprocessing.....")
        fill = True
        while fill:
            F_name = input("\nEnter Your First Name ")
            if F_name == "":
                print("\n*empty!")

            else:
                fill = False
                fill2 = True
                while fill2:
                    M_name = input("\nEnter Your Middle Name ")
                    if M_name == "":
                        print("\n*empty!")
                    else:
                        fill2 = False
                        fill3 = True
                        while fill3:
                            L_name = input("\nEnter Your Last Name ")
                            if L_name == "":
                                print("\n*empty!")
                            else:
                                fill3 = False
                            get_age = True
                            while get_age:
                                try:
                                    AGE = int(input(f"\nHow Old Are You,{L_name}? "))
                                except:
                                    print("\n*Numerical inputs only!")
                                else:
                                    get_age = False
                                    print("saving info....")
                                    #

        NAME = f"{F_name} {M_name} {L_name}"
        print("\nSet Pin")

        set_pass = True
        while set_pass:
            try:
                pin = int(input("\nset your 4 digit pin "))
            except:
                print("\ndigits only!")
            else:
                if len(str(pin)) == 4:
                    try:
                        PIN = int(input("\nconfirm pin "))
                    except:
                        print("\ndigits only")
                    else:
                        if len(str(PIN)) == 4 and PIN == pin:
                            print("\npin set successfully!")
                            set_pass = False

                        else:
                            print("\npins not the same\nset pin again!")
                else:
                    print("\nlenght must be equal to 4 ")


        ACC_NUM = random.randint(2113413567,2119789234)
        print(f"Your Account Number is {ACC_NUM}.")
        self.User_account_name = NAME
        self.User_account_number = ACC_NUM
        self.User_pin = PIN

        self.User_info["Account Name"] = NAME
        self.User_info["Age"] =  AGE
        self.User_info["Pin"] = PIN
        self.User_info["Account Number"] = ACC_NUM

    def Account_info(self):
        if self.User_info:
            print("\nProcessing....")
            #Authenticate = True
            #while Authenticate 
            for chances in range(1):
                try:
                    verify = int(input("\nEnter your pin "))
                except:
                    print("\n*digits only")
                else:
                    if verify == self.User_pin:
                        for k,v in (self.User_info):#.items():
                            print(f"{k} : {v}")
                            #continue
                    else:
                        print(f"\n*incorrect\nyou have {chances} chances left")

        else:
            print("\nNo info found!\ncreate an account")
    
    def Deposit(self):
        print("processing...")
        print("\nMin Deposit N500\nMax Deposit 200,000")
        deposit = True
        while deposit:
            try:
                Deposit_amt = int(input("\nEnter amount N"))
            except:
                print("\n*must be digits only!")
            else:
                if Deposit_amt < 500:
                    print("\namount must be less than N500")
                elif Deposit_amt >200_000:
                    print("amount must nkt be greater than N200,000")
                else:
                    print("\nprocessing.....")
                    self.User_account_balance += float(Deposit_amt)
                    deposit = False

        print("\nSuccessful")

    def Withdrawal(self):
        print("\nprocessing....")
        if self.User_info:
            print("\nMin withdrawal : N1000\nMax withdrawal : N100,000")
            try:
                withdrawal_amt = int(input("\nEnter amount N"))
            except:
                print("\n*digits only!")
            else:
                if withdrawal_amt < 1000:
                    print("\n*withdrawal amount must not be less than N1000!")
                elif withdrawal_amt > 100_000:
                    print("\n*you can withdraw more than N1000,000 at once")
                else:
                    if withdrawal_amt < Mollow_bank.User_account_balance:
                        print("\n*insufficient balance ")

                    elif withdrawal_amt > Mollow_bank.User_account_account:
                        print("\n*insufficient balance")

                    else:
                        for withdrawal in range(1):
                            try:
                                withdrawal_pin = int(input("\nEnter pin "))
                            except:
                                print("\n*digits only")

                            else:
                                print("\nverifying...")
                                if withdrawal_pin == self.User_pin:
                                    self.User_account_balance -= float(withdrawal_amt)
                                    print("\nSuccessful")

                                
                                else:
                                    print("\n*incorrect pin\nretry")

        else:
            print("\n*no account!\ncreate an account!")

def main(Mollow_bank):
    print(f"Welcome {Mollow_bank.Bank_Name}")
    take_action = True
    while take_action:
        Actions = input("\nEnter :\n\"c\" to Create Account\n\"ca\" to Check Account Info\n\"d\" to Deposit.\n\"w\" to Withdraw.\n\"cb\" to check balance.\n\n")
        if Actions == "":
            print("\n*empty!")

        elif Actions == "c":
            Mollow_bank.Create_acc()

        elif Actions == "ca":
            Mollow_bank.Account_info()
        
        elif Actions == "d":
            Mollow_bank.Deposit()

        elif Actions == "cb":
                print(f"N{Mollow_bank.CheckBalance()}")

        elif Actions == "w":
            Mollow_bank.Withdraw()

        elif Actions == "q":
            print("\nExiting...\nThanks for your time!")
            exit()
        else:
            print("\n*invalid!\nEnter \"q\" to quit")


Mollow_bank = Account("Mollow Bank")
if __name__ == "__main__":
    main(Mollow_bank)
