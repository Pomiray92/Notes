
fruit_colors = {
    "apple": "red",
    "berries": "blue"
}


# for i, v in fruit_colors.items():
#     print(i)
#     print(v)
#     print("#########")
    


# for a_tuple in fruit_colors.items():
#     # print(a_tuple)
#     # unpacking
#     x, y = a_tuple
#     print(x)
#     print(y)
#     print("#########")



# list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

# """Designing a calender system for human!! (programmers count from zero, but human do not)
# "Monday is day 1",  "Tuesday is day 2", etc. """

# for index, day in enumerate(list_of_days, start=1):
#     print(f"{day.capitalize()} is day {index}")



books = [
    {"cost": 10, "name": 'Python 2'},
    {"cost": 1, "name": 'Best tourism sites in Napoli'},
    {"cost": 5, "name": 'Basket Weaving for Pros'},
    {"cost": 8, "name": 'Java for dummies'},
]
# print(sorted(books, key=lambda book: book['cost']))

# readable!
func = lambda book: book['cost']
print(sorted(books, key=func))

func = lambda book: book['name']
print(sorted(books, key=func))
