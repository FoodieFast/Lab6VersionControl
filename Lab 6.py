
def encode(password):
    result = ""
    for char in password:
        result += str((int(char) + 3) % 10)
    return result


def main():
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = input("Please enter an option: ")

        if user_input == "1":
            entered_password = input("Please enter your password to encode:")
            encoded_password = encode(entered_password)
            print("Your password has been encoded and stored!")
            print(encoded_password)

        elif user_input == "2":
            pass
        elif user_input == "3":
            break


if __name__ == "__main__":
    main()
