def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1 and first != 0:
        return first * get_multiplied_digits((int(str_number[1:])))
    elif first != 0:
        return first
    else:
        return 1


print(get_multiplied_digits(42000))
