import userinfo
import task


# Gets id and handle exception then send id for authentication
# EFFECTING everywhere the customer enters a blank reply and sending them back here -- bug
def customer_authenticator():
    while True:
        try:
            print(" ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ^^^ ")
            confirm_id = int(input("Enter your user id: "))
            customer_pin_authenticator(confirm_id)

        except ValueError:
            print("Sorry, that is not allowed <<Invalid Entry err>>")
            continue


# Authenticate user id and pin if in userinfo
def customer_pin_authenticator(pass_id):
    if pass_id == userinfo.id:
        confirm_pin = int(input("Welcome Back, " + str(pass_id) + ", Enter your user pin: "))
        if confirm_pin == userinfo.pin:
            if pass_id == userinfo.id and confirm_pin == userinfo.pin:
                task.task_for_customers()
    else:
        print("id not found: contact the administrator if you are sure of the id !!! ")
        # send customer back to id authentication because of wrong pin
        customer_authenticator()
