class Person:
    def __init__(self, age, birth_place):
        self.age = age
        self.birth_place = birth_place

    def get_birth_place(self):
        return self.birth_place
    def print_person(self):
        print(f'Age: {self.age} , Birthplace: {self.birth_place}')
wesley = Person(29,'Costa Mesa')

wesley.print_person()