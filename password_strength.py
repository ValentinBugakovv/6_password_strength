import re

black_list = ["Password1"]


def check_basic_rules_password(password):
    count = 0
    if password in black_list or len(password) <= 4:
        count = 1
    return count


def get_password_strength(password):
    count = 0
    if re.search("\d+", password):
        count += 2
    if re.search("[A-Z]", password):
        count += 3
    if re.search("\W", password):
        count += 3
    if re.search("[a-z]", password):
        count += 2
    return count


def main():
    _password = input("input your password\n")
    if check_basic_rules_password(_password) != 1:
        security_result = get_password_strength(_password)
        print("Your password strength is {}".format(security_result))
    print("Protecting your password is 1. Change the password!")


if __name__ == "__main__":
    main()
