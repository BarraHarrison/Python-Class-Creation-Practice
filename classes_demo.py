# Practicing making classes in PY
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old.")

# Creating an instance of the prson class
person_one = Person("Johnny B", 38)
person_one.greet()

person_two = Person("Johnny Smacks", 30)
person_two.greet()