"""
Python class practice.
"""


class MyClass:
    """This class does x."""

    var = 5  # class attribute

    def do_smt(self):
        """This function does something. It is a method."""
        #  some method.


class Book:
    """Class about books"""

    material = "paper"  # class attribute
    cover = "paperback"  # class attribute
    all_books = []  # class attribute


#  Class attributes are defined within the class but outside of any methods.
#  Their value is the same for all instances of the class so consider them
#  as the "default" values for all objects.

#  Access class attributes using the dot notation with name of the class.

# print(Book.cover)
# print(Book.material)
# print(Book.all_books)

#  An instance of a class has access to its attributes and methods
#  Creating an instance of the "Book" class and assigning it to a variable:

# my_book = Book()  # Note parentheses after class name.
# print(my_book.cover)


class River:
    """Rivers"""
    all_rivers = []  # list of all rivers

    def __init__(self, name, length):
        self.name = name
        self.length = length
        River.all_rivers.append(self)  # add current river to the list of all rivers

    def get_info(self):
        """Prints name and length of river"""
        print(f"The length of the {self.name} is {self.length} km")


volga = River("Volga", 3530)
seine = River("Seine", 776)
nile = River("Nile", 6852)


class Pet:
    """ pets """
    kind = "mammal"
    n_pets = 0
    pet_names = []

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.legs = 4


tom = Pet("cat", "Tom")
avocado = Pet("dog", "Avocado")
ben = Pet("goldfish", "Benjamin")

tom.pet_names.append(tom.name)
avocado.pet_names.append(avocado.name)
ben.pet_names.append(ben.name)


class Ship:
    """Ship. Attributes are name, capacity and cargo."""

    def __init__(self, name, capacity):
        self.captain = None
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self):
        """Prints message '{ship} has sailed!'"""
        print(f"{self.name} has sailed!")

    def convert_cargo(self):
        """
        Converts tons of cargo into kilograms.
        :return: cargo_kg
        """
        cargo_kg = self.cargo * 1000
        return cargo_kg

    def name_captain(self):
        print(f"{self.captain} is the captain of {self.name}")

    def load_cargo(self, weight):
        if weight <= self.free_space()
            self.cargo += weight
            print(f"Loaded {weight} tons")
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print(f"Unloaded {weight} tons")
        else:
            print("Cannot unload that much")

    def free_space(self):
        return self.capacity - self.cargo


black_pearl = Ship("Black Pearl", 800)
black_pearl.load_cargo(600)
black_pearl.unload_cargo(400)
black_pearl.load_cargo(700)
black_pearl.unload_cargo(300)