username = input("Whats your name?\n")
def identify_user():
    username_list = ["Orion", "Bob Joe", "joe Bob"]
    if username in username_list:
        print("Hello", username)
    else:
        print("Go Away", username)
identify_user()

device_id = ["1001", "1002", "1003", "1004", "1005"]
