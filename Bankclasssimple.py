class Bankaccount(object):

    def __init__(self,name,Balance=0.0):
        self.name=name
        self.Balance=Balance

    def Deposit(self,Amount):
        if Amount>0:
            self.Balance+=Amount
            return self.Balance
    def Withdraw(self,Amount):
        if Amount>self.Balance:
            raise RuntimeError("You cannot withdraw money more than that you have on your account")
        else:
            self.Balance-=Amount
            return self.Balance

jeff=Bankaccount("Jeffy",1000)
jeff.Withdraw(10000)
