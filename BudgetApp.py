from collections import OrderedDict
import math

class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.total = 0.0
        self.depo = 0.0
    

    def deposit(self,amount,description=None):
        self.amount = float(amount)
        self.total += self.amount
        if description is None:
            self.ledger.append({"amount":self.amount,"description":""})
        else:
            self.ledger.append({"amount":self.amount,"description":description})
        self.depo = self.amount

    def withdraw(self,amount,description=None):
        self.amount = float(amount)
        
        if  (self.check_funds(self.amount) == False):
            self.total -= self.amount
            if description is None:
                self.ledger.append({"amount":-abs(self.amount),"description":""})
            else:
                self.ledger.append({"amount":-abs(self.amount),"description":description})           
            return True
        else:
            return False
    
    def show(self):
        header = "*"*15+self.name+"*"*15+"\n"
        cat = ""
        for l in self.ledger:
            cat += str("{:<23}".format(l["description"]))+str("{:>7.2f}".format(round(l["amount"],2)))+"\n"
        total = "Total: "+"{:.2f}".format(self.total)+"\n"
        return header + cat + total
        

    def get_balance(self):
        return self.total

    def transfer(self,amount,budget_categ):
        self.amount = float(amount)
        self.budget_categ = budget_categ
        if self.withdraw(self.amount, "Transfer from {}".format(budget_categ)):
            self.deposit(self.amount,"Transfer to {}".format(self.name))
            return True
        else:
            False
            print(budget_categ)  
            
    def check_funds(self,amount):
        self.amount = float(amount)

        if self.total <= self.amount:
            return True
        else:
            return False



def create_spend_chart(categories):
    tot = 0
    percentage = []
    names = []
    for cat in categories:
        names.append(cat.name)
        withdraw = 0  
        for l in cat.ledger:
            if l["amount"] < 0:
                tot += abs(float(l["amount"]))
                withdraw += abs(float(l["amount"]))
        percentage.append(withdraw)

    percentage = [x/tot for x in percentage]
    percentage = [ int((((x*100)-9)//10)*10) for x in percentage]    
    first = {}

    for r in range(100,-1,-10):
        top = str(r).rjust(3)+"|"
        first[top] = ""
        for per in percentage:
            if per >= r:
                first[top] = first.get(top,"o ") + "o "

    out = []
    for k,v in first.items():
        out.append(k+" "+v)
    mid = "\n".join(out)    
    
    len_names = [len(x) for x in names]
    header = "Percentage spent by category\n"
    foot = "{:>9}".format("- "*len(categories))

    bfoot = ""
    for l in range(len_names[1]):
        end=[]
        for name in names:
            try:
                end.append(name[l])
            except:
                end.append(" ")

        bfoot += "{:>8}".format(" ".join(end))+"\n"
    return header + mid + "\n" + foot + "\n" + bfoot    
      

## Testing Functions ##
an = Category("Food")
an.deposit(100,"food")
an.withdraw(57,"thai")
an.withdraw(2,"grocery")
an.deposit(80,"thai")
bn = Category("Clothing")
bn.deposit(20,"shirt")
bn.withdraw(7,"pants")


test = [an,bn]

print(create_spend_chart(test))







