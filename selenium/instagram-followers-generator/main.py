from account import InstaAccount

print("Hello, Welcome to the Instagram followers generator!")
print("Enter Instagram details.")
username = input("Username: ")
password = input("Password: ")
similar_account = input("Name of account that similar to yours: ")

my_account = InstaAccount()
my_account.login(username, password)
my_account.follow_all_followers(similar_account)
my_account.close_driver()