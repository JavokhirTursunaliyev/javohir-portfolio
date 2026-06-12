# Coursework Assessment 1
# Name: Javohir Tursunaliyev
# Student No: 2427229

import os.path
import string

def welcome():
    print("Welcome to the Caesar Cipher \nThis program encrypts and decrypts text with the Caesar Cipher")


def enter_message():
    mode = ''
    message = ''
    shift = 0
    mode = input("Would you like to encrypt (e) or decrypt (d): ")
    if mode == "e":
        message = input("what message would you like to encrypt: ")
        shift = input("What is a shift number: ")


    elif mode =="d":
        message = input("what message would you like to decrypt: ")
        shift = input("What is a shift number: ")

    return (mode, message, shift)


def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            elif char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message.upper()



def decrypt(message, shift):
    return encrypt(message, -shift)
def process_file(filename, mode, shift):
    list_messages = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                list_messages.append(encrypt(line.strip(), shift) if mode == 'e' else decrypt(line.strip(), shift))
    except FileNotFoundError:
        print("File not found.")
    return list_messages
def write_messages(lines):
    with open('results.txt', 'w') as file:
        for line in lines:
            file.write(line + '\n')
def is_file(filename):
    return os.path.isfile(filename)
def message_or_file():
    mode = ''
    filename = None
    message = None
    shift = 0

    while mode not in ['e', 'd']:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
        if mode not in ['e', 'd']:
            print("Invalid Mode")

    source = input("Would you like to read from a file (f) or the console (c)? ").lower()
    if source == 'f':
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename")
    elif source == 'c':
        message = input("What message would you like to {}? ".format("encrypt" if mode == 'e' else "decrypt")).upper()

    while True:
        try:
            shift = int(input("What is the shift number: "))
            if not 0 <= shift <= 25:
                print("Invalid Shift")
            else:
                break
        except ValueError:
            print("Invalid Shift")

    return (mode, message, filename, shift)


def main():
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()

        if filename:
            messages = process_file(filename, mode, shift)
            if messages:
                print("Output written to results.txt")
                write_messages(messages)
        else:
            result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
            print(result)

        repeat = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if repeat != 'y':
            print("Thanks for using the program, goodbye!")
            break


# Program execution begins here
if __name__ == '__main__':
    main()
