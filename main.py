def encode(password):
    encoded_password = ""
    for element in password:
        element = int(element) + 3
        encoded_password += str(element)
    return encoded_password


if __name__ == "__main__":
    password = input("Please enter your password to encode: ")
    encoded_password = encode(password)
    print(f"The encoded password is {encoded_password}")
