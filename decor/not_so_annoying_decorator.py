def not_so_annoying_decorator(f):
    def decorated_function(*args, **kwargs):
        print('Hey... I will execute your thing...')
        f(*args, **kwargs)
        print('Done...')
    return decorated_function


@not_so_annoying_decorator
def greeting(name):
    print(f'Hello {name}')


greeting('Mathias')
