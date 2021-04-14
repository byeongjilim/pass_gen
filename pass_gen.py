#! /usr/bin/python3

import sys
from random import randint

args_arr = sys.argv[1:]


def make_random_password(length):
    result = ""
    for i in range(length):
        type_of_chr = randint(1, 3)
        if type_of_chr == 1:
            result += chr(randint(48, 57))
        elif type_of_chr == 2:
            result += chr(randint(65, 90))
        elif type_of_chr == 3:
            result += chr(randint(97, 122))
    print(result)


def is_int(test_str):
    try:
        int(test_str)
        return True
    except ValueError:
        return False


if len(args_arr) == 0:
    make_random_password(8)
else:
    if len(args_arr) == 1:
        if(is_int(args_arr[0])):
            make_random_password(int(args_arr[0]))
