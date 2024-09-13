#!/usr/bin/pyhton3
if __name == "__main__":
    from sys import argv
    if len(argv) > 0:
        print("{} arguments:".format(len(argv)), end="\n")
        for index, value in enumerate(argv, start=1):
            print("{}: {}".format(index, value))
    else:
        print("{} arguments.".format(len(argv)))
