#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_args = len(argv) - 1
    result = 0
    if num_args == 0:
        print("{}".format(result))
    else:
        for value in argv[1:]:
            result += int(value)
        print("{}".format(result))
