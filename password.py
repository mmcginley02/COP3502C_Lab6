# * * * * * * * * * * * * * * * * * * * * * * * *
# Code Title : Lab 6 Code - Git / Version Control
# Course : COP 3502C - Programming Fundamentals 1
# Author : Megan McGinley Ferguson
# Date: 3/6/2023
# * * * * * * * * * * * * * * * * * * * * * * * *

def pw_encoder(pw_raw):  #takes in string, converts to integer list for encoding, returns string
    pw_enc = ''
    pw_enc_list = []
    pw_list = list(pw_raw)

    pw_list = [int(num) for num in pw_list]

    for num in pw_list[0:]:
        num += 3  #encoding
        pw_enc_list.append(num)

    for num in pw_enc_list:
        pw_enc += str(num)

    return pw_enc


def pw_decoder(pw_enc): #takes in string, converts to integer list for encoding, returns string
    pass

if __name__ == '__main__':

    menu_choice = 0

    while menu_choice != 3: #loop until user quits program

        print("Menu\n-----------\n1. Encode\n2. Decode\n3. Quit\n")

        menu_choice = int(input("Please enter an option: "))

        if menu_choice == 1:
            pw_raw = input('Please enter your password to encode: ')
            pw_enc = pw_encoder(pw_raw)
            print("Your password has been encoded and stored!")
        elif menu_choice == 2:
            print('FIX ME')
            #pw_raw = pw_decoder(pw_enc)
            #print(f'The encoded password is {pw_enc}, and the original password is {pw_raw}.')
        elif menu_choice == 3:
            break