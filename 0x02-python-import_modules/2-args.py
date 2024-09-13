#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("{} argument:".format(len(argv)), end="\n")
        for index, value in enumerate(argv, start=1):
            print("{}: {}".format(index, value))
    elif len(argv) > 1:
        print("{} arguments:".format(len(argv)), end="\n")
        for index, value in enumerate(argv, start=1):
            print("{}: {}".format(index, value))
    else:
        print("{} arguments.".format(len(argv)))
