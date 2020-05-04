import withdraw
import balance
import deposit
import errorHandler


# list of available task on the ATM service
def task_for_customers():
    print("Enter a task: ")
    print(" 1. Check Balance")
    print(" 2. Deposit")
    print(" 3. Withdraw")
    print(" 4. Transfer")
    collect_task = input("")
    if int(collect_task) == "":
        errorHandler.not_black("Task")
    elif int(collect_task) == 1:
        balance.current_balance()
    elif int(collect_task) == 2:
        deposit.customer_deposit()
    elif int(collect_task) == 3:
        pass
    elif int(collect_task) == 4:
        pass
