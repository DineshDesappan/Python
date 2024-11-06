#Dinesh
print("Banking program")
print("1.Show balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")



def show_balance():
    print(f"balance is {balance}$")

def deposit():
    money = int(input("Enter the amount you want to deposit: "))
    print(f"amount {money} has been deposited successfully")
    return money
def withdraw(balance):
    withdrawl_amount = int(input("Enter the amount you want to withdraw: "))
    if balance < withdrawl_amount:
        print(f"balance is {balance}$. So, you don't have enough money to withdraw")
        return 0
    else:
        # balance -= withdrawl_amount
        print(f"amount {withdrawl_amount} has been withdraw successfully, remaining balance is {balance - withdrawl_amount}$")
        return withdrawl_amount
balance = 0
running = True
while running:
   user = int(input("Enter your Choice(1-4): "))
   if user == 1:
       show_balance()
   elif user == 2:
      balance += deposit()
   elif user == 3:
       balance -= withdraw(balance)
   elif user == 4:
       running = False
   else:
       print("Invalid input try again!")
       user = int(input("Enter your Choice(1-4): "))


