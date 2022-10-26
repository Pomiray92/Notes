# any()  &    all()

# # all() Returns True only if all items are True otherwise False

# print(all(("some content", "")))      # False
# print(all(("some content")))          # True
# print(all((1, 2)))                    # True



# # any() Returns True if one of the item is True otherwise False

# print(any((1, 2)))                      # True
# print(any((1, None)))                   # True
# print(any((None, None)))                # False


# netflix_subscribers = [
#     {"name": "Fausto", "paid": False},
#     {"name": "Jacque", "paid": False},
#     {"name": "Pasco", "paid": False},
#     {"name": "Wessam", "paid": False},
#     {"name": "Emily", "paid": False},
# ]

# paid = []
# for user in netflix_subscribers:
#     if user['paid']:
#         paid.append(user)
# # logic @ boolean 
# print(len(paid), len(netflix_subscribers))
# have_all_paid = len(paid) == len(netflix_subscribers)

# have_all_paid = all([u['paid'] for u in netflix_subscribers])
# print(have_all_paid)



# # map
# # Give you a list, and you transform the content of that list(mutable iterable)

# _-----------------------------------------_ # 

# names = ["jacque doe", "peer doe", "mirjam doe", "shaban doe"]

# all_name_capitalize = map(lambda name : name.title(), names)
# all_name_capitalize = map(str.title, names)
# def custom(name):
#     split_name = name.split(" ")
#     full_string = " "
#     for n in split_name:
#         full_string += n.capitalize + " "
#     return full_string

# all_name_capitalize = map(custom, names)

# print(list(all_name_capitalize))


# _-----------------------------------------_ # 


# # filter Method

# names = ["reiner", "peter", "john"]

# for name in names.copy():
#     if name.endswith("er"):
#         names.remove(name)
        
# print(names)

# names = filter(lambda names: not name.endswith("er"), names)
# print(list(names))


# _------remove jacque from list of dict----------_ #

names = [
    {'name': 'jacque doe'},
    {'name': 'peer doe'},
    {'name': 'mirjam doe'},
    {'name': 'shaban doe'}
    ]

names = filter(lambda name_dict: not name_dict["name"].startswith("jacque"), names)
print(list(names))