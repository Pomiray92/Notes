def annoying_decorator(f):
    def decorated_function(*args, **kwargs):
        print('I will not do what you want!')
    
    return decorated_function


@annoying_decorator
def greeting(name):
    print(f'Hi {name}')

@annoying_decorator
def sum_(x, y):
    return x + y


greeting('Mathias')
print(sum_(3, 4))