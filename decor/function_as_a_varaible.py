# First Example
def f(x, y):
    return x + y

print(f(3, 4))
g = f
print(g(3, 4))


# Second Example
def greeting(f, name):
    print(f'Hello {f(name)}')

def lower_cased_name(name):
    return name.lower()

greeting(lambda n: n.upper(), 'mathias')
greeting(lambda n: n.lower(), 'MATHIAS')
greeting(lower_cased_name, 'MATHIAS')
