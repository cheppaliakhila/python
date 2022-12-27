class customer :
    '''this class developed by akhila'''
    bankname ='State Bank of India'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('net balance:',self.balance)
    def  withdraw(self,amount):
       if amount>self.balance:
           print('sorry insufficient balance')
       else:
           self.balance=self.balance-amount
           print('net balance:',self.balance)
print('welcome to ',customer.bankname)
name=input('Enter your name:')
cl=customer(name)
while True:
    print('D - Deposit \n W - Withdraw \n E- Exit')
    optio=input('Enter  the option:')
    opt=optio.lower()
    if opt=='d':
       amt=eval(input('Enter the amount:'))
       cl.deposit(amt)
    elif opt=='w':
        amnt=eval(input('Enter the amount to withdraw:'))
        cl.withdraw(amnt)
    elif opt=='e':
          print('Thank you')
          break
    else :
        print('enter the valid option:')
            
