#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 20, 2022
# This program asks the user for an input level and
# then tells them what their mark range is in percentages

import time


def calc_mark(level_from_user):
    # User input cases
    # Returns case to the main function
    return {
        'R': "0-49%",
        '1-': "50-52%",
        '1': "53-56%",
        '1+': "57-59%",
        '2-': "60-62%",
        '2': "63-66%",
        '2+': "67-69%",
        '3-': "70-72%",
        '3': "73-76%",
        '3+': "77-79%",
        '4-': "80-85%",
        '4': "86-90%",
        '4+': "91-95%",
        '4++': "96-100%"
    }.get(level_from_user, "Not a valid level")


def main():
    # this function gets user input and
    # prints the final range
    # Get user input for level
    print("This program converts levels to percentages.")
    time.sleep(1)
    level = input("Enter the level that you were given : ")

    # Call the calculation function and print the percent range
    percentage = calc_mark(level)
    print(" ")
    print(percentage)
    print(" ")


if __name__ == "__main__":
    main()
