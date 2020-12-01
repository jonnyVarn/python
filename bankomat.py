import json
import os

class ATM():
    def __init__(self, balance, pin, name):
        self.balance = balance 
        self.pin=pin
        self.name=name

    def greeter(self):
        print("Welcome to the bank of Zeros and Ones!")
        print("Enter your pin, 4 or 6 digits")

    def login(self):
        valid=False
        while valid==False:
            userpin=input("Enter PIN: ")
            #if not len(int(pin))==4 or not len(int(pin))==6 or str.isdigit(pin)==False:
            #:
            if (len(userpin)==4 or len(userpin)==6) and str.isdigit(userpin) and self.pin==userpin:
                 print("Valid pin, welcome human + " + self.name)
                 valid=True
            else:
                print("not valid")
        #try:
            
            
                
            
                #raise Exception('el should not exceed 10. The value of x was: {}'.format(x))
                #raise Exception(“The pin should have four or six digits”)
        #else:
         #   print(len(pin))
         #   print("4 or 6 digits pin")
               
        #except: 
            #print("Please enter a valid PIN")
    def check_balance(self):
        str(self.balance)
        print("your balance is {}".format(self.balance))
        return self.balance

    def deposit(self):
        deposit_amount=input("How much do you want to deposit?")
        self.balance += int(deposit_amount)
        print("After deposit you have " + str(self.balance) + " kr")

    def withdraw(self):
        print("How much do you want to withdraw?")
        print("you have " +str(self.balance) +"kr")
        withdraw_amount=input("Enter amount to withdraw: ")
        
        if int(withdraw_amount) > (self.balance):
            print(" DECLINED ")
        else: 
            self.balance = self.balance - int(withdraw_amount)
            print("balance is now  " + str(self.balance) + " kr")
    
    def collect_intrest(self):
        years=input("How many years do you want to skip?")
        self.balance = self.balance * (int(years)*1.1)
        print("balance is now  " + str(self.balance))


        
    
    
def menu(object):
    menu_dict={0:"Quit", 1:"Deposit money", 2:"Withdraw money", 3:"Check balance", 4:"Collect intrest"}
    print(json.dumps(menu_dict, sort_keys=True, indent=-2))
    to_do=input() 
    while to_do!="0":
        if to_do !="1" or to_do !="2" or to_do !="3" or to_do !="4" or  to_do !="0":
    
            if to_do =="1":
                object.deposit()
                
            if to_do =="2":
                object.withdraw()
                
            if to_do =="3":
                object.check_balance()
    
            
            if to_do =="4":
                object.collect_intrest()
                

            if to_do =="0":
                break
            
        print(json.dumps(menu_dict, sort_keys=True, indent=-2))
        to_do=input() 
        
    

    




atm1=ATM(100, "1234", "Jonny")
atm1.greeter()
atm1.login()
menu(atm1)


  




#atm1.check_balance()






#ta ut säta in , samla ränta



