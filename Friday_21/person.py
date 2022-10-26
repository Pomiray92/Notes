# what problems does class solve?



# Modeling problems or scenarios



person_name = "Peer"
person_location = "Dortmund"
person_activities = ["climbing", "hiking"]
person = {
    "name": "Peer",
    "location": "Dortmund"
}


class Person:
    # dunder methods --> double underscore methods 
    # # name = "Peer"
    # self mean the "entity"--> self refers to the instance of the class
    # "
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"{self.name}"
    
    def greeting(self, name):
        return f"Good Morning, my name is {self.name}. Hello {name}"

           def greeting_v2(self, instance):
 return f"Good Morning, my name is {self.name}. Hello {instance.name}"
    
# "function"

a = Person("Peer")
b = Person("Somon")

# c = Person("Some")
# list_of_instance = [Person("A"), Person("B")]
# print(list_of_instance)
# # dot notation
# print(a.name)
# print(b.name)
# print(c.name)
print(a.greeting("Shaban"))
print(a.greeting_v2(b))
