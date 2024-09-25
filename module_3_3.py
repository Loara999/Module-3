def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(1, 2, 3)
print_params(1, 2)
values_list = [5, 2.5, 'Яблоко']
values_dict = {'a': 5, 'b': 6, 'c': 4}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 2]
print_params(*values_list_2, 42)
