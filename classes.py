# Method is a function in Python
# Classes use Pascal Case
# Here we have created an animal object
class Animal:
    def __init__(self, name, species, number_of_legs=4):  # Constructor with a default value for number_of_legs
        self.name = name
        self.species = species
        self.number_of_legs = number_of_legs

    def make_sound(self):  # Add self as the first parameter
        print("Grrrr")

    def eat_food(self):  # Add self as the first parameter
        print("nom nom")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am a {self.species}")

# Create an instance of Animal
john_the_dog = Animal("John", "dog")
john_the_dog.greet()

jessie_the_cat = Animal("Jessie", "cat")
jessie_the_cat.greet()

# Outputs: Hello, my name is John and I am a dog




# animal_dictionary = {
#     "name": "John",
#     "species": "Dog",
#     "number of legs": 4
# }