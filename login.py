import userinfo
import task
import errorHandler


# Gets id and handle exception then send id for authentication
# EFFECTING everywhere the customer enters a blank reply and sending them back here -- bug
# while True:
#     try:
#         print(" ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ")
#         confirm_id = int(input("Enter your user id: "))
#         customer_pin_authenticator(confirm_id)
#
#     except ValueError:
#         print("Sorry, that is not allowed <<Invalid Entry err>>")
#         continue

# Solution to previous issue above
def customer_authenticator():
    print(" ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ")
    errorHandler.id_value_handler()
    # showing unresolved reference because the variable isn't defined within the function
    customer_pin_authenticator(confirm_id)


# Authenticate user id and pin if in userinfo
def customer_pin_authenticator(pass_id, trial=3):
    if pass_id == userinfo.id:
        errorHandler.pin_value_handler(pass_id)
        # showing unresolved reference because the variable isn't defined within the function
        if confirm_pin == userinfo.pin:
            if pass_id == userinfo.id and confirm_pin == userinfo.pin:
                task.task_for_customers()
        else:
            print("<<<Timed Out>>>")
            customer_authenticator()

    else:
        print("id not found: contact the administrator if you are sure of the id !!! ")
        # send customer back to id authentication because of wrong pin
        customer_authenticator()
