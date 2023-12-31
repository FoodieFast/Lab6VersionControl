# Group Members: Ashidbilig Tamir, Eric Zhang
def encode(password):
    result = ""
    for char in password:
        result += str((int(char) + 3) % 10)
    return result
# Goes through each digit of the password, adds 3, if greater 10, drops 10. Then added to result


def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3) % 10)
        # decoding each digit of the password
        decoded_password = decoded_password + decoded_digit
    return decoded_password
# returns the fully decoded password


def main():
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        # Menu

        user_input = input("Please enter an option: ")

        if user_input == "1":
            entered_password = input("Please enter your password to encode:")
            encoded_password = encode(entered_password)
            print("Your password has been encoded and stored!\n")
            # Encodes

        elif user_input == "2":
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.\n")
            # Decodes and prints output of both

        elif user_input == "3":
            break
            # Quits program


if __name__ == "__main__":
    main()
    # Runs main
