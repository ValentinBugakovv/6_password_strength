import re

black_list = ["Password1"]


def get_password_strength(password):
    count = 0
    if password in black_list:
        count = 1
        return count
    if re.search("\d+", password) is not None:
        count += 2
    if re.search("[A-Z]", password) is not None:
        count += 2
    if re.search("\W", password) is not None:
        count += 2
    if re.search("[a-z]", password) is not None:
        count += 2
    if len(password) >= 10:
        count += 2
    return count


def main():
    _password = input("input your password\n")
    security_result = get_password_strength(_password)
    print("Your password strength is {}".format(security_result))


if __name__ == "__main__":
    main()
