#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x == 0:
            print(my_list[0])
            return x
        else:
            count = 0
            for ele in my_list:
                if count > (x - 1):
                    break
                print(ele, end="")
                count += 1
            return (my_list[x - 1])
    except IndexError:
        return my_list[-1]
    finally:
        print()
