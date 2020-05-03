import login
import project_info


# program entrance
def welcome_customer():
    print("''''''''''Welcome To ATM System Project''''''''''")
    print("Developer: " + project_info.developer_name)
    print("Project Name: " + project_info.project_name)
    print("Project Start Date: " + project_info.project_start_date)
    login.customer_authenticator()


welcome_customer()
