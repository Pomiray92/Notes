


# def outer():
#     def inner():
#         print("Hello, I am inner")
#     return inner                                  # have not executed it!

# o = outer()
# print(o)
# o()
# outer() 

# Closures func return func

# sometimes closures can take in argument

# def outer(name):
#     def inner():
#         print(f"Hello {name}, I am inner")
#     return inner                                  # have not executed it!!
#     # return inner()                                # return a VALUE have not executed it!                                

# outer("Shaban")()

# division case


# def check_division(func):
    
#     def inner(a,b):
#         if b == 0:
#             print("You cannot divide by zero")
#             return # "You cannot divide by zero"
#         return func(a, b)
#     return inner
    

# # division case
# def divide(a, b):
#     # if b == 0:
#     #     print("")
#     #     return "You cannot divide by zero"
#     return a / b

# divide = check_division(divide)
# print(divide(4, 2))
# print(divide(4, 0))


# practical use-cases
# API - a way of accessing data from one location (URL (website))
# Testing of code (Automation tests)
# Application Programming Interface
# - CLI (command line interface)
# - GUI (graphical user interface)


# def make_upper(func): # We expect the func
#     def inner():
#         return func().title()
    
#     return inner


# @make_upper
# def greetings():
    
#     return "hi there"

# print(greetings())

# def capitalize(name):
#     return f"{name.title()}"

# def make_title_in_word(function):
#     # print("first")
#     def inner(name): # the argument of the inner function are the same argument as the func we pass
#         # print(name, "in inner func")
#         # return function(name) # not changed yet
#         return function(name).title()
#     return inner

# def add_mr(func):
#     # print("second")
#     def inner(name):
#         # print(name, "Line 92")
#         name = f"Mr/Mrs {name}"
#         return func(name)
#     return inner

# @add_mr
# @make_title_in_word
# def greet_some_humans(name):
#     return "Good morning " + name

# print(greet_some_humans("wojciech doe"))

#
#
#     from screenshots
#
#



#---------------------------------LISTS-------------------------------#




# names = ["peter doe", "peer doe", "mary doe", "tom doe"]
# capital_names1 = []


# for i in names:
#     capital_names1.append(i.title())

# print(capital_names1)

    
# capital_names = [   n.capitalize() for n in names   ]

# print(capital_names)

# # filter out all names that start with "p"
# no_ps = [n.title() for n in names if not n.startswith("p")]
# print(no_ps)

# # another method
# no_ps = [n.title() for n in names if ("p") not in n]
# print(no_ps)




#----------------------------FUNC----------------------------#


# def add_mr(func):
#     def inner(*args):
#         full_str = ""
#         for s in args:
#             full_str += s + " "
#         #name = f"Mr/Mrs {args}"
#         name = f"Mr/Mrs {' '.join([ n.title() for n in args])}"
#         return func(name)
#     return inner


# @add_mr
# def greet_some_humans():
#     pass




#----------------------------LAMBDA FUNC---------------------------#

# add = lambda a, b: a + b
# print(add(1, 2))

# subtract = lambda c, d: c - d
# print(subtract(15, 7))

# # to str, add Mr/Ms to name
# add_str = lambda name, prefix: f"{prefix} {name}"  # func anonymous

# # # another stile
# # def add_str1(prefix, name):
# #     return f"{prefix} {name}"
    
# print(add_str("Shaban", "Mr"))

# database = {"female": ["Shabanita"], "male": ["Shabanino"]}

# add_str = lambda **kwargs: f"{'Ms' if kwargs['gender'] == 'female' else 'Mr'} {kwargs['name']}"
# print(add_str("Shabanita")) 


# Screenshots to compleat top LAMBDA FUNC

#-----------------------------FUNC call Func---------------------#


# def capitalize_name(func):
#     return lambda name: func(name).upper()


# @capitalize_name
# def greet(name):
#     return name
# print(greet("Test"))



# make func complicated under

def capitalize_name(func):
    inner = lambda *args: func(*args).title()
    return inner


@capitalize_name
def greet(**args):
    return " ".join()

print(greet("Test"))