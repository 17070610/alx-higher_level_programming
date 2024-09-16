#!/usr/bin/pyhton3
if __name__ == "__main__":
    def no_c(my_string):
        new_str = ""
        for char in my_string:
            if char != 'c' and char != 'C':
                new_str += char
         return new_str
