#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Oct 23, 2023
# This program will ask the user
# for a number and it will tell them
# what month corresponds to it.


def main():
    # Get the user month and display message

    print("This program will ask the user for a number from 1 to 12")
    print("then it will tell them what month corresponds to it.")
    user_month = int(input("Please enter a integer from 1 to 12: "))

    # Check what month corresponds to user month
    match user_month:
        case 1:
            print("\n1 represents January.")

        case 2:
            print("\n2 represents February.")

        case 3:
            print("\n3 represents March.")

        case 4:
            print("\n4 represents May.")

        case 5:
            print("\n5 represents May.")

        case 6:
            print("\n6 represents June.")

        case 7:
            print("\n7 represents July.")

        case 8:
            print("\n8 represents August.")

        case 9:
            print("\n9 represents September.")

        case 10:
            print("\n10 represents October.")

        case 11:
            print("\n11 represents November.")

        case 12:
            print("\n12 represents December.")

        case _:
            print("\n{} is not a valid number.".format(user_month))


if __name__ == "__main__":
    main()
