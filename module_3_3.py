def print_params (a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params(3, 'two', 3)
print_params(3, 'two',)
print_params()
#----------------------------#
print ("\n")
values_list = [3, 'hi', False]
values_dict = {'a': 4, 'b': 'bye', 'c': True}

print_params(*values_list)
print_params(**values_dict)

#-----------------#
values_list_2 = [3, 'one']

print ("\n")
print_params(*values_list_2, 56)
print_params(*values_list_2)