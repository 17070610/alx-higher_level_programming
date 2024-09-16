#!/usr/bin/python3
if __name__ == "__main__":
    def element_at(my_list, idx):
        for i, idx in enumerate(my_list):
            if idx < 0 or idx > len(my_list):
                return None
            else:
                print("Element at index {:d} is {}".format(idx, my_list[idx]))
