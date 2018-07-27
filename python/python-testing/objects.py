lilly_dict = {"name": "Lilly",
        "age": 18,
        "pets": False,
        "hair_color": 'Black'}


class Person(object):
    def __init__(self, name, age, pets, hair_color):
        self.name = name
        self.age = age
        self.pets = pets
        self.hair_color = hair_color
        self.hungry = True

    def eat(self, food):
        print('I am eating ' + food)
        self.hungry = False

    def __str__(self):
        return 'Name: ' + self.name

lilly = Person(
    name = "Lilly",
    age = 18,
    pets = False,
    hair_color = "Black")

david = Person(
    name = "David",
    age = 16,
    pets = False,
    hair_color = "Black")


print(lilly.name)
print(lilly.hungry)
print(lilly.eat("banana"))
print(david.name)
