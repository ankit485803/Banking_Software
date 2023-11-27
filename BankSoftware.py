

# Banking_Software (Author: Ankit Kumar)
# https://github.com/ankit485803/Banking_Software
# https://replit.com/@ankit485803/BankingSoftware#main.py



class Customer:

  def __init__(self, cn, ci, cj):
    self.cname = cn
    self.cid = ci
    self.cjob = cj

  def getCName(self):
    return self.cname

  def getCid(self):
    return self.cid

  def getCjob(self):
    return self.cjob

  def setCJob(self, new_job):
    self.cjob = new_job


class Accounts:

  def __init__(self, cust, acc_no, bal):
    self.customer = cust
    self.account_number = acc_no
    self.balance = bal

  def deposit(self, amt):
    self.balance += amt

  def withdraw(self, amt):
    self.balance -= amt

  def getCustomer(self):
    return self.customer

  def getAccountNumber(self):
    return self.account_number

  def getBalance(self):
    return self.balance


class BankAccounts:

  def __init__(self, acc_list):
    self.alist = acc_list

  def addAccount(self, acc):
    for i in self.alist:
      if i is acc:
        print("Account already exists")
        return
    self.alist.append(acc)

  def removeAccount(self, acc):
    ind = 0  #index
    for i in self.alist:
      if i is acc:
        self.alist.pop(ind)
        return
      ind += 1
    print("The account does not exist")

  def printAllCBalances(self):
    print("Printing all account numbers and balances: ")
    for i in self.alist:
      print(i.customer.getCName(), i.getAccountNumber(), i.getBalance())


c1 = Customer("Ajay", 100, "Teacher")
c2 = Customer("Ram", 101, "Business")
c3 = Customer("Shyam", 102, "Students")

a1 = Accounts(c1, 1100, 10000)
a2 = Accounts(c2, 1101, 100000)
a3 = Accounts(c3, 1102, 1000)

b1 = BankAccounts([])
b1.addAccount(a1)
b1.addAccount(a2)
b1.addAccount(a3)

b1.printAllCBalances()
a1.deposit(100000)
b1.printAllCBalances()





##Create a menu based software with the following options. After a task is done, return to
##the menu till 'x' is not pressed
'''
1. Add Customer
2. Update Customer Job
3. Create Account
4. Deposit Amount
5. Withdraw Amount
6. Get Balance
7. Add Account in Branch
8. Remove Account from Branch
9. Print All Customer Balances
x. Quit
'''
