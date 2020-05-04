import task
open_statement_of_accout = open("statement_of_account.txt", "r")
current_balance_figure = open_statement_of_accout
withdrawal_amount = 0.00
deposit_amount = 0.00


def s(x):
    global current_balance_figure
    current_balance_figure = float(x) + current_balance_figure
    open_statement_of_accout_for_deposit = open("statement_of_account.txt", "w")
    open_statement_of_accout_for_deposit.write(current_balance_figure)
    print("#" + current_balance_figure + ", Deposited Successfully")
    task.task_for_customers()
    return current_balance_figure
