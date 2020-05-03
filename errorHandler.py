# handles every possible errors


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
    print(x + "Can not be blank")
