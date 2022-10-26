def print_numbers_recursive(n):
    if n == 0:
        print(0)
        return
    else:
        print_numbers_recursive(n - 1)
        print(n)

def print_number_iterative(n):
    print('---- iterative')
    m = 0
    while n >= 0:
        print(m)
        m += 1
        n = n - 1


print('---- recursive')
print_numbers_recursive(5)
print_number_iterative(5)