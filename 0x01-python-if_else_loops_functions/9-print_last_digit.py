#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(f"{abs(number) % 10}")
        return abs(number) % 10
    else:
        print(f"{-(abs(number) % 10)}")
        return -(abs(number) % 10)
