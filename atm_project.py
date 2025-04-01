class ATM:
    '''
    constructor 
    @param atm_number: int
    @param atm_balance: int
    @param pin: int 
    '''
    def __init__(self, atm_number, atm_balance=0, pin=1234):
        self.atm_number = atm_number
        self.atm_balance = atm_balance
        self.pin = pin
    
    '''
    function to set the atm pin
    @param pin: int
    return: None
    '''    
    def set_pin(self, pin):
        if len(str(pin)) != 4:
            return "PIN must be 4 digits"
        else:
            self.pin = pin
            return "PIN set successfully"
        
    '''
    function to check balance by manager
    return: int
    '''
    def check_balance(self):
        return self.atm_balance
    
    '''
    function to check balance by user
    @param pin: int
    return: int
    '''
    def check_balance_user(self, pin):
        if pin == self.pin:
            return self.atm_balance
        else:
            return "Invalid PIN"
        
    '''
    function deposite 
    @param pin: int
    @param amount: int
    return: string
    '''
    def deposit(self, pin, amount):
        if pin == self.pin:
            if amount <= 0:
                return 'Not enough amount'  
            self.atm_balance += amount
            return f"Deposited {amount}. New balance is {self.atm_balance}."
        
        else:
            return "Invalid PIN"
    
    '''
    function widrown 
    @param pin: int
    @param amount: int
    return: string
    '''
    def wid(self, pin, amount):
        if pin ==self.pin:
            if amount > self.atm_balance:
                return 'not enough amount'
            self.atm_balance -= amount
            return f"Deposited {amount}. New balance is {self.atm_balance}."
        else:
            return "Invalid PIN"
    '''
    function str method 
    return: string
    '''
    def __str__(self):
        return f"ATM Number: {self.atm_number}, ATM Balance: {self.atm_balance}, PIN: {self.pin}"
    

class Manager:
    '''
    constructor 
    @param atm: ATMs list
    '''
    def __init__(self, atms=[], enter=1234):
        self.atms = atms
        self.enter = int(enter)    
        
    '''
    function to issue a new atm
    @param atm_number: int
    return: string
    '''
    def issue_atm(self, atm_number):
        new_atm = ATM(atm_number)
        self.atms.append(new_atm)
        return f"ATM {atm_number} issued."
    
    '''
    function to check total balance of all atms
    return: int
    '''
    def total_balance(self):
        total = 0
        for atm in self.atms:
            total += atm.check_balance()
        return total
    
    '''
    function to search atm by number
    @param atm_number: int
    return: ATM object or None
    '''
    def search_atm(self, atm_number):
        for atm in self.atms:
            if atm.atm_number == atm_number:
                return atm
        return None

def welcome_message():
    print("Welcome to the ATM Management System")

# function to run program
def main():
    manager = Manager() # create manager object
    welcome_message() # print welcome message
    while 1:
        
        print("Login As \n1. Manager \n2. ATM \n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            enter = input("Enter password : ")
            if manager.enter != int(enter):
                print("wrong password")
                continue
            while 1:
                print("Manager Menu \n1. Issue ATM \n2. Check Total Balance \n3. logout")
                choice = input("Enter your choice: ")
                if choice == '1':
                    atm_number = input("Enter ATM Number: ")
                    print(manager.issue_atm(atm_number))
                elif choice == '2':
                    print(f"Total Balance: {manager.total_balance()}")
                elif choice == '3':
                    break
                else:
                    print("Invalid Choice")
        elif choice == '2':
            atm_number = input("Enter ATM Number: ")
            if manager.search_atm(atm_number) is None:
                print("ATM not found")
                continue
            atm = manager.search_atm(atm_number)
            while 1:
                print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. set pin \n5. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    pin = int(input("Enter PIN: "))
                    if atm.pin != pin:
                        print("try again")
                        continue
                    print(atm.check_balance_user(pin))
                elif choice == '2':
                    pin = int(input("Enter PIN: "))
                    if atm.pin != pin:
                        print("try again")
                        continue
                    amount = int(input("Enter Amount to Deposit: "))
                    print(atm.deposit(pin, amount))
                elif choice == '3':
                    pin = int(input("Enter PIN: "))
                    if atm.pin != pin:
                        print("try again")
                        continue
                    amount = int(input("Enter Amount to Withdraw: "))
                    print(atm.wid(pin, amount))
                elif choice == '4':
                    pin = int(input("Enter New PIN: "))
                    print(atm.set_pin(pin))
                elif choice == '5':
                    break
                else:
                    print("Invalid Choice")
        elif choice == '3':
            print("Thank you for using ATM Management System")
            break
        else:
            print("Invalid Choice")
            
if __name__ == "__main__":
    main()

