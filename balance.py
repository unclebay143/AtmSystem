from purse import current_balance_figure
import deposit

def current_balance():
    print("Your Current Balance is: " + str(current_balance_figure.readline()))
    deposit.customer_deposit()
