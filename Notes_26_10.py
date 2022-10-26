# Identify what is common?

# "Base case" 

# Attributes / fields
#===================================##
# first_name
# last_name
# gender (3)
# legs
# identification
# shoe_size

# Methods
#========
# Talk
# run
# drink
# study
# etc.


class Person:
    
    def __init__(self, first_name: str, last_name: str, gender: str, legs: int =2):
        
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.legs = legs
        
    def talk(self):
        return "Leverage agile framework to provide a robust syno..."
    
    # colons: semi-colons;
    def run(self, destination: str, origin: str) ->str:
        return f"I am {self.first_name} running towards {destination} away from {origin}"
    
    def cry(self, date) -> str:
        if date == "Today":
            return "We shall cry today"
        elif date == "monday":
            return "TGIm"
        elif self.legs < 2:
            return "Ouch"
        else:
            return "Not enough tears today"
        
    
    def full_name(self):
        return f"This is my name {self.first_name} {self.last_name}"
        
     

p1 = Person("Fausto", "Doe", "Other")
p2 = Person("Emily", "Doe", "Female", 1)
p3 = Person("Reza", "Doe", "Male")

print(p1.full_name())   

print(p1.run("Bristol", "Napoli"))

print(p1.cry("Today"))
