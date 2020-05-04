# handles every possible errors

import login
import task


#  to handle ValueError for any calling but not working
def wrong_input(err):
    err = err
    try:
        err
    except ValueError:
        print("Sorry, that is not allowed")


# Action not allowed
def not_allowed(x):
    print("Not Allowed")


# field cannot be blank error handler
def not_black(x):
    while True:
        try:
            task.collect_task = int(input("Entry: "))
            return
        except ValueError:
            print(x + "Can not be blank")
            continue


# value exception for confirming custome_id
def id_value_handler():
    while True:
        try:
            global confirm_id
            login.confirm_id = int(input("Enter your user id: "))
            confirm_id = login.confirm_id
            return confirm_id
        except ValueError:
            print("Sorry, that is not allowed <<Invalid Entry err>>")
            continue


# value exception for confirming customer_pin
def pin_value_handler(pass_id):
    while True:
        try:
            global confirm_pin
            login.confirm_pin = int(input("Welcome Back," + str(pass_id) + ", Enter your user pin: "))
            confirm_pin = login.confirm_pin
            return confirm_pin
        except ValueError:
            print("Sorry, that is not allowed <<Invalid Entry err>>")

