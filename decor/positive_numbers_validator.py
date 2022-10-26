from os import device_encoding


def validate_positive(f):
    def decorated_function(*args, **kwargs):
        for number in args:
            if number < 0:
                print('Negative numbers are not allowed!')
                return
        result = f(*args, **kwargs)
        return result
    return decorated_function


@validate_positive
def sum_(x, y):
    return x + y


print(sum_(9, 1))
print(sum_(-2, 3))
print(sum_(9, 1))