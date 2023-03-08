def encode_password(password: str) -> str:
    """Encodes a password by adding 3 to each digit."""
    password_enc_list = [str(int(num) + 3) for num in password]  # simplified the encoding process using list comprehension
    return ''.join(password_enc_list)


def decode_password(password_enc: str) -> str:
    """Decodes a password by subtracting 3 from each digit."""
    password_list = [str(int(num) - 3) for num in password_enc]  # simplified the decoding process using list comprehension
    return ''.join(password_list)


if __name__ == '__main__':
    menu_choice = 0

    while menu_choice != 3:
        print("Menu\n-----------\n1. Encode\n2. Decode\n3. Quit\n")

        menu_choice = int(input("Please enter an option: "))

        if menu_choice == 1:
            password_raw = input('Please enter your password to encode: ')
            try:
                password_enc = encode_password(password_raw)  # added a try-except block to catch invalid input
            except ValueError:
                print("Invalid input! Password should only contain digits.\n")
                continue
            print("Your password has been encoded and stored!")
        elif menu_choice == 2:
            password_enc = input('Please enter the encoded password: ')
            try:
                password_raw = decode_password(password_enc)  # added a try-except block to catch invalid input
            except ValueError:
                print("Invalid input! Encoded password should only contain digits.\n")
                continue
            print(f"The encoded password is {password_enc}, and the original password is {password_raw}.")  # used an f-string for string formatting
        elif menu_choice == 3:
            break