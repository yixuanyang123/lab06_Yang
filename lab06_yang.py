# Name: Yixuan Yang
def encode(password):
    encoded_password = ""
    for element in password:
        element = int(element) + 3
        encoded_password += str(element)
    return encoded_password


def decode(password):
    decoded_password = ""
    for element in password:
        element = int(element) - 3
        decoded_password += str(element)
    return decoded_password


if __name__ == "__main__":
    game_continue = True
    password_stored = False
    while game_continue:
        # 1. print the menu
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        # input an option by users
        option = int(input("Please enter an option: "))

        # encode password
        if option == 1:
            if not password_stored:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
                password_stored = True
            elif password_stored:
                print(f"The decoded password is {decoded_password}, and the original password is {password}")

        # decode password
        if option == 2:
            if password_stored:
                print(f"The encoded password is {encoded_password}, and the original password is {password}")
                password_stored = False
            elif not password_stored:
                password = input("Please enter your password to decode: ")
                decoded_password = decode(password)
                print("Your password has been decoded and stored!")
                password_stored = True

        # quit the program
        if option == 3:
            game_continue = False
