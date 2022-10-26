def greeting_factory(type):
    if type == 'informal':
        def informal_greeting(name):
            return f'Hi {name}'
        
        return informal_greeting
    elif type == 'formal':
        def formal_function(name):
            return f'Hello {name}'

        return formal_function
    else:
        def simple_greeting(name):
            return f'Hi'
        return simple_greeting


greeting = greeting_factory('formal')
print(greeting('mathias'))
