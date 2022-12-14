from Notes_26_10 import Person

class Student(Person):
    # no constructor 
    pass

class StudentClimber(Person):
    def __init__(self, first_name, last_name, gender, legs, third_eye):
        Person.__init__(self, first_name, last_name, gender, legs)
        # super().__init__(first_name, last_name, gender, legs)
        self.third_eye = third_eye

    def climb(self):
        return f"I, {self.first_name}, prefer to climb Mt. Everest"

if __name__ == '__main__':
    s1 = Student('Peer', 'Doe', 'Other')
    s2 = StudentClimber("Shaban", "Doe", "Male", 2, True)
    # print(s1.run('Berlin', 'Hamburg'))
    # print(s1)
    print(s2.climb())

