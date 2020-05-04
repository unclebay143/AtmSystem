import purse
import balance

def customer_deposit():
    purse.deposit_amount = input("Enter Amount To Deposit: ")
    purse.s(purse.deposit_amount)
    # purse.current_balance_figure = purse.current_balance_figure + float(purse.deposit_amount)
    # balance.update_balance(purse.current_balance_figure)
